# Shaowei WeChat Skills

少威公众号生产 Skill 套件，用于把初稿、提纲、碎片想法或链接内容整理成公众号文章，并按固定样式完成排版、配图、生图和微信公众号草稿箱发布。

## What Is Included

- `shaowei-wechat-suite`: 总入口，说明整套 Skill 的职责边界、迁移方式和组合关系。
- `shaowei-wechat-article`: 内容生成层，把初稿或碎片想法整理成公众号正文。
- `shaowei-wechat-writer`: 固定格式渲染层，按少威公众号样式定稿。
- `shaowei-wechat-illustrator`: 配图规划层，判断文章哪里适合插图。
- `shaowei-wechat-image-generator`: 生图执行层，默认使用 `gpt-image-2`。
- `shaowei-wechat-image-pipeline`: 配图闭环层，负责规划、生图、上传素材和回填正文。
- `shaowei-wechat-pipeline`: 全文闭环总控，串联写作、排版、配图和草稿箱发布。
- `wechat-article-publisher`: 微信发布层，支持 dry-run 预览和创建草稿。

## Rendering Rules

当前发布脚本已经支持少威固定格式里的关键规则：

- `No.xx` 或 `> [!NOTE] / > No.xx` 会自动渲染成居中浅黄编号框。
- `viral` 模式下，如果文章开头有编号框，首段正文不会再被自动卡片化。
- 二级标题使用浅红底和左侧竖条样式。
- 重点句使用浅黄高亮和深色加粗。
- 图片使用微信素材 URL 回填，图注建议使用 `图 1｜xxx`。

## Image Style

解释型、方法型、拆解型文章默认优先使用“教授白板板书风格”的知识图解：

- 不是现实白板照片。
- 白底或浅底。
- 有中文主标题、3-5 个核心模块、箭头、方框、关系线和适度色彩。
- 图本身承担解释任务，而不只是装饰。

默认 OpenAI-compatible 图片接口：

```text
OPENAI_BASE_URL=https://new.depot.de5.net/v1
POST /images/generations
model=gpt-image-2
```

API key 不应写入 Skill 文件或仓库，请通过环境变量或本地私有配置注入。

## WeChat Setup

复制配置示例：

```bash
cp skills/wechat-article-publisher/config.example.json skills/wechat-article-publisher/config.json
```

然后填写：

- `wechat.app_id`
- `wechat.app_secret`
- `wechat.author`

`config.json` 已加入 `.gitignore`，不要提交真实密钥。

## Usage

安装依赖：

```bash
python3 skills/wechat-article-publisher/scripts/publish_wechat.py --install
```

预览：

```bash
python3 skills/wechat-article-publisher/scripts/publish_wechat.py examples/embodied-ai-data-wall-wechat.md --dry-run
```

创建微信公众号草稿：

```bash
python3 skills/wechat-article-publisher/scripts/publish_wechat.py examples/embodied-ai-data-wall-wechat.md
```

运行渲染测试：

```bash
python3 skills/wechat-article-publisher/scripts/test_publish_rendering.py
```

## Notes

这个仓库不包含真实微信密钥、OpenAI-compatible API key、临时 response 文件或本地生成图片。示例文章中的图片 URL 是已上传到微信素材库后的公开素材地址，用于展示完整 Markdown 结构。
