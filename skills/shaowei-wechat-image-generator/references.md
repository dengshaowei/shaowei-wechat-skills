# Shaowei Wechat Image Generator References

如需以下内容，优先读取本文件：
- 中文白板教授图的细规则
- 已验证的接口字段
- request / response / 输出目录约定
- 公众号正文图片回填原则
- 可复用模式关键词

## 推荐模式清单

### 1. 中文白板教授图
适用：
- 解释型文章
- 方法拆解文
- 概念辨析文
- 需要“图本身就能讲清楚”的内容
- 产品描述 / 文档转图解
- 用户说“画成白板风格图”“教授白板板书风格”“帮我画一张白板”

核心要求：
- 图中必须有可读中文文字
- 必须有箭头、方框、连接关系、分组和层级
- 必须有主标题、3-5 个核心模块、关键结论 / 落点
- 必须用适度色彩区分模块和重点
- 白底或浅底
- 像老师讲课的板书总结图，但不要画成真实白板照片或教室场景
- 不是抽象装饰图

常见结构：
- 中心主题 + 三到五个分支
- 左右对照映射
- 流程递进
- 因果关系
- 条件闭环
- 漏斗 / 阶梯 / 金字塔 / 飞轮 / 四象限
- 产品价值链路：问题 -> 能力 -> 机制 -> 结果
- 文档转白板：背景 -> 核心观点 -> 关键结构 -> 行动建议

Prompt 必带约束：
- clear readable Chinese text
- arrows and labeled boxes
- whiteboard teaching diagram
- knowledge explainer graphic
- professor-style whiteboard board notes
- not a photo of a physical whiteboard
- main title and 3-5 labeled modules
- simple charts and relationship lines
- color-coded highlights
- not abstract decorative art
- not poster style
- not textless concept art

默认 prompt 骨架：

```text
Create a whiteboard-style knowledge explainer diagram, not a photo of a physical whiteboard. Transform the following content into a professor-style whiteboard board-note illustration.

Use clear readable Chinese text. Include:
1. A clear Chinese main title at the top
2. 3-5 labeled content modules
3. Arrows, boxes, grouping brackets, and relationship lines
4. Simple visual charts where useful, such as flow, funnel, matrix, flywheel, pyramid, or cause-effect map
5. Color-coded highlights: blue for concepts/technology, orange for value/results, green for action/path, red for risks/key questions
6. A short key takeaway at the bottom

The layout should feel like structured teaching notes drawn on a clean white background. It should be rich enough to help readers understand the core idea, but clean and readable. Avoid a realistic classroom scene, avoid an empty physical whiteboard, avoid poster-style composition, avoid decorative abstract art, avoid tiny unreadable text.

Content to transform:
<paste content here>
```

### 2. 关系图 / 概念图
适用：
- 多因素共同作用
- 系统关系解释
- 结构拆解

注意：
- 如果用户强调“要有文字”“像老师讲课”，应升级到“中文白板教授图”，不要只停留在无字关系图。
- 如果用户要求“白板风格”，默认理解为知识图解风格，不要生成真实白板场景。

### 3. 情绪收束图
适用：
- 文章结尾情绪承接
- 成长、选择、行动落点

注意：
- 当用户明确要求“解释图”或“讲解图”时，不要误用情绪图。

## 本次已验证的目录约定

- request 文件：`.tmp/ai-*.request.json`
- response 文件：`.tmp/image-responses/*.response.json`
- 白板图输出目录：`.tmp/generated-images-whiteboard/`
- 中文白板教授图输出目录：`.tmp/generated-images-chinese-board/`

## 本次已验证的接口方式

OpenAI-compatible images endpoint：
- `POST {BASE_URL}/v1/images/generations`
- `Authorization: Bearer <API_KEY>`
- `Content-Type: application/json`

少威当前已验证可用的默认图片服务基准：
- `BASE_URL=https://new.depot.de5.net`
- 图片生成完整端点：`https://new.depot.de5.net/v1/images/generations`
- 模型：`gpt-image-2`

推荐环境变量约定：
- `OPENAI_BASE_URL=https://new.depot.de5.net/v1`
- `OPENAI_API_KEY=<your_key>`

说明：
- `BASE_URL` 用于 curl / request 模板拼接
- `OPENAI_BASE_URL` 用于兼容 OpenAI SDK / OpenAI-compatible 调用习惯
- **不要把明文 API Key 直接写进 SKILL.md / references.md**；默认通过本机环境变量或本地私有配置注入

网络约束（已实测）：
- `GET /v1/models` 可正常返回
- `POST /v1/images/generations` 在系统代理开启时，可能报 `ProxyError` / `RemoteDisconnected`
- 关闭代理并直连后，可稳定生成图片

默认规避方式：
- Python `requests`：使用 `session = requests.Session(); session.trust_env = False`
- shell：显式设置 `HTTPS_PROXY= HTTP_PROXY= ALL_PROXY= NO_PROXY='*'`

返回中优先读取：
- `data[0].b64_json`
- 兼容字段：`base64` / `image_base64`

## 公众号正文回填原则

- 正文图片必须使用微信素材 URL
- 不要把本地 png 路径直接写进正文
- 上传素材后再替换正文图片 src

## 适合沉淀成模式名的关键词

- `chinese-whiteboard-professor`
- `knowledge-diagram-zh`
- `article-explainer-board`
