# Cloudflare Pages 部署指南（手机端一步搞定）

> 本项目已经做好 **Cloudflare Pages 静态托管** 配置，注册好 GitHub + Cloudflare 后，
> 5 分钟可上线一个 `https://hu-xishu-system.pages.dev` 的网址，手机直接可访问。

---

## 一、为什么选 Cloudflare Pages

| 优势 | 说明 |
|---|---|
| 🆓 完全免费 | 无限带宽、无限请求、自定义域名 |
| 🌍 全球 CDN | 200+ 城市节点，国内访问延迟 150-300ms |
| 🔒 自动 HTTPS | 一键 SSL，无需配置证书 |
| 🚀 Git 自动部署 | 推代码即部署，3 分钟生效 |
| 📱 移动端友好 | 完美支持手机浏览器 |

---

## 二、你需要准备的（一次性 5 分钟）

### 1. 注册 GitHub
1. 手机/电脑访问 https://github.com/signup
2. 邮箱 + 密码 + 用户名（**建议就用 `wang730827`**，跟你 Gitee 一致）
3. 验证邮件 → 完成注册
4. **创建 Personal Access Token**：
   - 右上头像 → **Settings** → **Developer settings** → **Personal access tokens** → **Tokens (classic)**
   - **Generate new token (classic)**
   - Note: `hu-xishu-push`
   - Expiration: `No expiration`
   - Scopes: 勾 **`repo`**
   - 点 **Generate token**
   - **复制 `ghp_xxxx...` 那串字符**（关掉页面就再也看不到）

### 2. 把 GitHub 用户名 + Token 发给我
我立刻把所有 36 个项目文件推到你的 GitHub 仓库 `wang730827/hu-xishu-system`。

### 3. 注册 Cloudflare（用 GitHub 登录）
1. 手机/电脑访问 https://dash.cloudflare.com/sign-up
2. 用 **GitHub 账号** 直接登录（一键授权）
3. 登录后会自动进入 Cloudflare 控制台

---

## 三、部署到 Cloudflare Pages（3 步）

### 第 1 步：创建 Pages 项目
1. Cloudflare 控制台 → 左侧 **Workers & Pages** → **Create application** → **Pages** 标签 → **Connect to Git**
2. 选择 **GitHub** → 授权 Cloudflare 访问你的仓库
3. 选中 `wang730827/hu-xishu-system` 仓库 → **Begin setup**

### 第 2 步：配置构建设置
| 字段 | 填写 |
|---|---|
| **Project name** | `hu-xishu-system`（会得到 `hu-xishu-system.pages.dev`） |
| **Production branch** | `main` |
| **Framework preset** | 选择 **None**（纯静态站点） |
| **Build command** | 留空 |
| **Build output directory** | 留空（项目根目录就是静态文件） |

### 第 3 步：部署
- 点 **Save and Deploy**
- 等待 2-3 分钟，状态变为 **Success**
- 点击生成的网址：`https://hu-xishu-system.pages.dev`
- 🎉 手机直接访问即可使用

---

## 四、域名自定义（可选，免费）

Cloudflare Pages 自带 `*.pages.dev` 域名，如果你想用自己的域名：

1. Cloudflare Pages → 你的项目 → **Custom domains** → **Set up a custom domain**
2. 输入你已有的域名（例如 `huxishu.yourdomain.com`）
3. 按照提示在域名 DNS 添加 CNAME 记录
4. Cloudflare 自动签发 SSL，5 分钟内生效

> 国内访问速度优化：可以选 Cloudflare 优选 IP（手动改 hosts），将延迟从 300ms 降到 100ms。

---

## 五、文件结构（项目里有什么）

```
hu-xishu-system/
├── index.html             # 移动端友好的辨证问诊界面（前端入口）
├── data/
│   └── formulas.json      # 218 首方剂数据（前端直接加载）
├── core/                  # Python 后端源码（本地开发用）
│   ├── knowledge.py       # 方剂库
│   ├── engine.py          # 辨证引擎
│   ├── llm.py             # 大模型接入
│   └── config.py
├── prompts/               # 胡希恕人设 + 六经规则 + 方剂速查
│   ├── huxishu_persona.md
│   ├── six_meridian_rules.md
│   ├── formula_reference.md
│   └── consultation_flow.md
├── scripts/               # PDF 导入 + 向量库
│   ├── import_pdf.py
│   └── build_vector_db.py
├── docs/                  # 完整文档
├── ui/                    # Streamlit 本地版 UI
├── api/                   # Vercel Serverless API（备选）
├── vercel.json            # Vercel 部署配置
├── requirements.txt       # Python 依赖
├── README.md              # 项目说明
└── CLOUDFLARE_DEPLOY.md   # 本文档
```

> **Cloudflare Pages 部署的版本**只用前 3 个文件就够运行（前端的 `index.html` + `data/formulas.json`）。  
> 其余是 **Python 本地开发版 / Vercel 备选版 / 文档**。

---

## 六、常见问题

### Q1：手机访问慢怎么办？
A：在手机 WiFi 设置里把 DNS 改为 `1.1.1.1`（Cloudflare DNS），可以加速。  
或访问 [Cloudflare 优选 IP 工具](https://www.cloudflare.com/zh-cn/ips/) 手动指定 IP。

### Q2：CF Pages 免费额度多少？
A：无限流量、无限请求，每月 500 次构建（个人用不完）。

### Q3：可以绑定自己的域名吗？
A：可以。Settings → Custom domains → 跟着提示做，5 分钟。

### Q4：代码更新后会自动部署吗？
A：会。GitHub 仓库 `main` 分支收到 push，CF Pages 自动重新部署，2-3 分钟生效。

### Q5：能不能加 LLM 问诊（DeepSeek/Qwen）？
A：可以。下一步扩展：
- 把 `core/llm.py` 改成 Cloudflare Workers（JS 版）
- 或挂一个外部 LLM API（在 index.html 加个 API Key 输入框）

### Q6：Gitee 仓库还要保留吗？
A：建议保留，作为国内镜像备份。Gitee 不能 Pages，但仓库本身还能用。

---

## 七、进阶：开启 Cloudflare Analytics

部署成功后，Cloudflare 自动开启 Web Analytics，可以在 Pages 项目里看到：
- 访问量、地理位置、来源
- 加载性能、错误率

---

## 八、故障排查

| 现象 | 原因 | 解决 |
|---|---|---|
| 打开页面空白 | `data/formulas.json` 没上传 | 检查仓库根目录有 `data/formulas.json` |
| 加载方剂失败 | 路径不对 | 确认 `index.html` 第 ~50 行写的是 `./data/formulas.json` |
| 部署失败 | 构建命令没留空 | Build command 留空、Build output 留空 |
| 自定义域名打不开 | DNS 没生效 | 等 5-30 分钟 DNS 传播 |

---

> 部署完成后，请把网址告诉我，我帮你做一次端到端问诊测试。
