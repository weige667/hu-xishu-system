# 使用说明

## 演示版 vs 完整版

| 特性 | 演示版 | 完整版（需 LLM） |
|------|--------|------------------|
| 启动 | 立即可用 | 需配置 API |
| 知识库 | 30+ 胡希恕核心方 | 30+ 方 + LLM |
| 成本 | 0 元 | 每月 1-3 元（DeepSeek） |

## 问诊三种模式
1. **多轮问诊** - 模仿胡希恕逐步抓主症
2. **快速辨证** - 直接输入症状
3. **完整病历** - 按四诊格式填写

## 添加胡希恕 PDF 资料
1. 把 PDF 放到 data/books/
2. 运行: python scripts/import_pdf.py --type books --all
3. （可选）构建向量库: python scripts/build_vector_db.py --build

## 配置 LLM

### DeepSeek（推荐）
1. https://platform.deepseek.com/ 注册
2. 充值最低 1 元
3. 创建 API Key
4. 复制 .env.example 为 .env 并填入

### 通义千问
1. https://dashscope.aliyun.com/
2. 配置 LLM_PROVIDER=openai
3. OPENAI_BASE_URL=https://dashscope.aliyuncs.com/compatible-mode/v1
