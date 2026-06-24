# 项目目录结构

```
hu-xishu-system/
├── api/                   # Vercel 入口
│   ├── index.py
│   └── index.html
├── core/                  # 核心引擎
│   ├── config.py
│   ├── knowledge.py        # 30+ 方剂
│   ├── engine.py          # 辨证引擎
│   └── llm.py             # LLM 客户端
├── ui/                    # Streamlit 界面
│   └── app.py
├── data/                  # 数据
│   ├── books/
│   ├── cases/
│   ├── lectures/
│   └── vector_db/
├── prompts/               # 提示词
├── scripts/               # 工具
├── docs/                  # 文档
├── requirements.txt
├── install.sh / install.bat
└── start.sh / start.bat
```
