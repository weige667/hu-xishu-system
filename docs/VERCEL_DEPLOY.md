# Vercel 部署指南

## 一、为什么选 Vercel
- 100GB 流量/月 免费
- 自动 HTTPS
- 全球 CDN
- 零配置

## 二、部署步骤

### 1. 注册 Vercel
访问 https://vercel.com/，用 GitHub 账号注册

### 2. 导入项目
- Add New → Project
- 选 Gitee 仓库
- 框架：Other
- Install Command: pip install -r requirements.txt

### 3. 部署
点 Deploy，等待 1-3 分钟

### 4. 访问
https://你的项目名.vercel.app/

## 三、配置 LLM（可选）

添加环境变量：
```
LLM_PROVIDER=openai
OPENAI_API_KEY=sk-your-key
OPENAI_BASE_URL=https://api.deepseek.com/v1
LLM_MODEL=deepseek-chat
```

## 四、常见问题

### Q: 国内访问慢？
A: Vercel 国内访问不稳定，建议用 Cloudflare Workers 或阿里云

### Q: 免费额度够用吗？
A: 100GB 流量，个人使用绰绰有余
