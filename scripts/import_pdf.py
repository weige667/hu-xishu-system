"""PDF 导入工具"""
import sys
from pathlib import Path
ROOT = Path(__file__).parent.parent.resolve()
sys.path.insert(0, str(ROOT))

import argparse
from loguru import logger
from core.config import BOOKS_DIR, CASES_DIR, LECTURES_DIR


def extract_pdf(pdf_path, output_dir):
    import pdfplumber
    output_file = output_dir / (pdf_path.stem + ".md")
    logger.info(f"Processing: {pdf_path.name}")
    text_content = []
    with pdfplumber.open(pdf_path) as pdf:
        for i, page in enumerate(pdf.pages):
            text = page.extract_text()
            if text:
                text_content.append(f"## Page {i+1}\n\n{text}\n")
    with open(output_file, "w", encoding="utf-8") as f:
        f.write(f"# {pdf_path.stem}\n\n" + "".join(text_content))
    logger.info(f"  -> {output_file.name}")


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--type", choices=["books", "cases", "lectures"], default="books")
    parser.add_argument("--pdf")
    parser.add_argument("--all", action="store_true")
    args = parser.parse_args()

    target = {"books": BOOKS_DIR, "cases": CASES_DIR, "lectures": LECTURES_DIR}[args.type]
    target.mkdir(parents=True, exist_ok=True)

    if args.pdf:
        extract_pdf(Path(args.pdf), target)
    elif args.all:
        for pdf in list(target.glob("*.pdf")) + list(target.glob("*.PDF")):
            extract_pdf(pdf, target)
    else:
        print("Usage: python import_pdf.py --type books --all")


if __name__ == "__main__":
    main()
