"""Add PDF page citations to the Week 3 text. Run with Python and pypdf."""

import json
from bisect import bisect_right
from hashlib import sha256
from itertools import accumulate
from pathlib import Path
from tempfile import TemporaryDirectory

from pypdf import PdfReader


def split_on_pages(records, pages):
    """Follow the original reading order, even when a phrase occurs more than once."""
    page_text = ["".join(page.split()) for page in pages]
    page_ends = list(accumulate(map(len, page_text)))
    original = "".join(page_text)
    offset = 0
    for row in records:
        text = row["text"]
        compact = "".join(text.split())
        if not compact or not original.startswith(compact, offset):
            raise ValueError(f"Text differs from the original PDF at {row['record_id']}")

        # The lab removes some whitespace. Count visible characters to locate the
        # page break, then slice the saved text so that its wording is preserved.
        positions = [i for i, char in enumerate(text) if not char.isspace()]
        positions.append(len(text))
        start = 0
        while start < len(compact):
            page_index = bisect_right(page_ends, offset + start)
            stop = min(len(compact), page_ends[page_index] - offset)
            yield {
                **row,
                "parent_record_id": row["record_id"],
                "record_id": f"{row['record_id']}-p{page_index + 1}",
                "page": page_index + 1,
                "text": text[positions[start]:positions[stop]].strip(),
            }
            start = stop
        offset += len(compact)
    if offset != len(original):
        raise ValueError("The Week 3 text ends before the PDF does")


def publish(path, content):
    with TemporaryDirectory(dir=path.parent) as staging:
        temp_path = Path(staging) / path.name
        temp_path.write_bytes(content)
        temp_path.replace(path)


def main(root):
    data = root / "data"
    baseline = data / "week3_manifest.json"
    sources = []
    passages = []
    for entry in json.loads(baseline.read_text(encoding="utf-8"))["records"]:
        source = data / "raw" / entry["source_filename"]
        if source.suffix.lower() != ".pdf":
            continue
        prepared = root / entry["prepared_output"].replace("\\", "/")
        if sha256(source.read_bytes()).hexdigest() != entry["source_sha256"]:
            raise ValueError(f"Source changed for {entry['source_id']}. Rerun Week 3.")
        saved = prepared.read_bytes()
        if sha256(saved).hexdigest() != entry["prepared_sha256"]:
            raise ValueError(f"Prepared file changed for {entry['source_id']}. Rerun Week 3.")
        records = [json.loads(line) for line in saved.decode("utf-8").splitlines()]
        if not records or any(
            row["source_sha256"] != entry["source_sha256"] or Path(row["source"]).name != source.name
            for row in records
        ):
            raise ValueError(f"Missing or mismatched source records for {entry['source_id']}")
        pages = [page.extract_text() or "" for page in PdfReader(source).pages]
        updated = list(split_on_pages(records, pages))
        passages.extend(updated)
        sources.append({
            "source_id": entry["source_id"], "source_sha256": entry["source_sha256"],
            "week3_output_sha256": entry["prepared_sha256"], "pages": len(pages),
            "week3_records": len(records), "page_records": len(updated),
        })

    if not passages or len({row["record_id"] for row in passages}) != len(passages):
        raise ValueError("No page records or duplicate record IDs")
    output = "".join(json.dumps(row, ensure_ascii=False) + "\n" for row in passages).encode("utf-8")
    checksum = sha256(output).hexdigest()
    folder = data / "week4_pdf_pages"
    folder.mkdir(exist_ok=True)
    # Publish the matching data first, then switch the manifest to the new version.
    path = folder / f"passages-{checksum}.jsonl"
    publish(path, output)
    evidence = {
        "week3_manifest": baseline.relative_to(root).as_posix(), "sources": sources,
        "prepared_output": path.relative_to(root).as_posix(), "prepared_sha256": checksum,
        "processing": "Split Week 3 records at PDF page breaks in source order; keep parent_record_id.",
        "page_numbering": "PDF viewer pages, starting at 1", "page_records": len(passages),
    }
    publish(folder / "manifest.json", (json.dumps(evidence, indent=2) + "\n").encode("utf-8"))
    print(f"Saved {len(passages)} passages with page numbers from {len(sources)} PDFs.")


if __name__ == "__main__":
    main(Path(__file__).resolve().parents[1])
