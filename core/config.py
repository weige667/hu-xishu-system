"""配置"""
import os
from pathlib import Path

ROOT_DIR = Path(__file__).parent.parent.resolve()
DATA_DIR = ROOT_DIR / "data"
BOOKS_DIR = DATA_DIR / "books"
CASES_DIR = DATA_DIR / "cases"
LECTURES_DIR = DATA_DIR / "lectures"
VECTOR_DB_DIR = DATA_DIR / "vector_db"
HISTORY_DB = DATA_DIR / "history.db"
PROMPTS_DIR = ROOT_DIR / "prompts"


class Settings:
    llm_provider: str = "mock"
    llm_api_key: str = ""
    llm_base_url: str = ""
    llm_model: str = "gpt-3.5-turbo"
    ollama_host: str = "http://localhost:11434"
    ollama_model: str = "qwen2.5:14b"
    app_name: str = "胡希恕经方辨证系统"
    app_version: str = "1.0.0"
    debug: bool = True


settings = Settings()


def ensure_dirs():
    for d in [DATA_DIR, BOOKS_DIR, CASES_DIR, LECTURES_DIR, VECTOR_DB_DIR]:
        d.mkdir(parents=True, exist_ok=True)
