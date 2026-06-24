"""向量库构建"""
import sys
from pathlib import Path
ROOT = Path(__file__).parent.parent.resolve()
sys.path.insert(0, str(ROOT))

import argparse
from loguru import logger
from core.config import BOOKS_DIR, CASES_DIR, LECTURES_DIR, VECTOR_DB_DIR


def build():
    import chromadb
    client = chromadb.PersistentClient(path=str(VECTOR_DB_DIR))
    collection = client.get_or_create_collection("huxishu_kb")

    docs, metas, ids = [], [], []
    for source, dir_path in [("books", BOOKS_DIR), ("cases", CASES_DIR), ("lectures", LECTURES_DIR)]:
        if not dir_path.exists():
            continue
        for md in dir_path.glob("*.md"):
            content = md.read_text(encoding="utf-8")
            chunks = content.split("\n\n")
            for i, c in enumerate(chunks):
                if len(c) > 50:
                    docs.append(c[:1000])
                    metas.append({"source": source, "file": md.name})
                    ids.append(f"{source}_{md.stem}_{i}")

    if docs:
        collection.add(documents=docs, metadatas=metas, ids=ids)
        logger.info(f"Built with {len(docs)} chunks")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--build", action="store_true")
    args = parser.parse_args()
    if args.build:
        build()
