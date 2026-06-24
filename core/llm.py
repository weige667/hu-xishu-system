"""LLM 客户端（可选）"""
import httpx
from .config import settings


class LLMClient:
    def __init__(self):
        self.provider = settings.llm_provider
        self.api_key = settings.llm_api_key
        self.base_url = settings.llm_base_url
        self.model = settings.llm_model

    def is_available(self):
        if self.provider == "mock":
            return False
        if self.provider == "ollama":
            return True
        return bool(self.api_key)

    def chat(self, messages, system_prompt=""):
        if not self.is_available():
            return "【LLM 未启用】演示版"

        if self.provider == "ollama":
            return self._chat_ollama(messages, system_prompt)
        return self._chat_openai(messages, system_prompt)

    def _chat_openai(self, messages, system_prompt):
        try:
            from openai import OpenAI
            kw = {"api_key": self.api_key}
            if self.base_url:
                kw["base_url"] = self.base_url
            client = OpenAI(**kw)
            full = []
            if system_prompt:
                full.append({"role": "system", "content": system_prompt})
            full.extend(messages)
            r = client.chat.completions.create(
                model=self.model, messages=full, temperature=0.7, max_tokens=2000
            )
            return r.choices[0].message.content
        except Exception as e:
            return f"LLM Error: {e}"

    def _chat_ollama(self, messages, system_prompt):
        try:
            full = []
            if system_prompt:
                full.append({"role": "system", "content": system_prompt})
            full.extend(messages)
            r = httpx.post(f"{settings.ollama_host}/api/chat",
                json={"model": settings.ollama_model, "messages": full, "stream": False}, timeout=60)
            return r.json()["message"]["content"]
        except Exception as e:
            return f"Ollama Error: {e}"


llm_client = LLMClient()
