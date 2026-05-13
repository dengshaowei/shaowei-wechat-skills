---
name: shaowei-wechat-image-generator
description: 专门负责少威公众号场景下的 AI 生图执行。适用于用户已经有公众号正文、配图规划或明确图片需求，希望直接生成头图、文中配图、竖版图、概念图、中文白板教授图，且后续需要把这一步串联进少威公众号总流程的场景。默认承接已完成的配图规划或图片需求，不负责重写正文与微信发布。
---

# Shaowei Wechat Image Generator

## Role

这个 skill 是少威公众号体系里的**生图执行层**。

它负责：
- 接收已经明确的图片需求
- 将图片需求整理成适合 `gpt-image-2` 或 OpenAI-compatible 图片接口的高质量 prompt
- 按公众号场景选择合适尺寸、画幅与风格
- 执行真实生图，并落地到本地文件
- 在需要时返回 request 文件、response 文件、输出图片路径，方便后续串联微信流程

它不负责：
- 重写公众号正文
- 判断整篇文章的内容结构是否顺畅
- 决定公众号最终发布
- 代替配图规划层做整篇图文节奏设计

## Position In The Skill Suite

推荐串联位置：

1. `shaowei-wechat-article`：内容生成
2. `shaowei-wechat-writer`：固定格式渲染
3. `shaowei-wechat-illustrator`：配图规划
4. `shaowei-wechat-image-generator`：生图执行
5. `wechat-article-publisher`：预览 / 草稿箱发布
6. `shaowei-wechat-image-pipeline`：配图闭环总控
7. `shaowei-wechat-pipeline`：整篇公众号总控

如果用户没有完整配图规划，也可以单独使用本 skill，但应先补齐最基本的图片目标判断。

## Input

输入优先级如下：

### 优先输入
- 已完成的公众号正文
- 已完成的配图规划
- 明确的图片清单（例如：头图 1 张，文中图 2 张）
- 明确风格模式（例如：中文白板教授图 / 概念图 / 情绪图）

### 也可接受
- 一篇初稿 + 用户说明想要配图
- 某一段正文 + 指定要生成插图
- 单独一张图的用途描述

## Workflow

### 1. 识别图片任务
先明确每张图的：
- 用途
- 插入位置
- 目标作用
- 是否需要情绪感 / 解释感 / 场景感 / 结构感
- 是否需要带文字

### 2. 选择视觉模式
常用模式：
- 场景感头图
- 概念图 / 关系图
- 情绪收束图
- **中文白板教授图**

如果文章是解释型、拆解型、方法型内容，默认优先判断是否应该使用**中文白板教授图**，而不是无字氛围图。

### 3. 补全画面设计
把抽象需求补全为可执行画面，包括：
- 主体对象
- 场景环境
- 结构模块
- 文字标签
- 箭头与连接关系
- 色彩倾向
- 构图方式
- 风格质感
- 避免项

### 4. 转成生图 prompt
默认输出适合 `gpt-image-2` 的完整 prompt，避免过短、过空、过泛。

如果使用中文白板教授图模式，prompt 中应明确写出：
- 必须有中文文字
- 必须有箭头 / 框图 / 连接关系
- 图本身承担讲解作用
- 不要抽象装饰图
- 不要无字概念图

### 5. 执行生图
优先使用真实接口执行，而不是只停留在 prompt：
- 写入 request json
- 调用 OpenAI-compatible 图片接口
- 保存 response json
- 解码 base64 为本地 png

默认接口基准：
- `OPENAI_BASE_URL=https://new.depot.de5.net/v1`
- 模型：`gpt-image-2`

认证方式：
- 通过 `OPENAI_API_KEY` 注入
- 不要把明文 key 直接硬编码进 skill 文件

推荐调用端点：
- `${OPENAI_BASE_URL}/images/generations`
- 若使用 `BASE_URL` 约定，则等价端点为 `${BASE_URL}/v1/images/generations`

## 6. Network / Proxy Constraint

少威当前这套外部图片接口，已经验证：
- `GET /v1/models` 可通
- `POST /v1/images/generations` 在系统代理开启时，可能被代理中断
- 关闭代理并改为直连后，可稳定生成图片

因此默认执行约束是：
- 生图请求优先使用 **无代理直连模式**
- Python `requests` 场景，优先使用 `Session()` 并设置 `session.trust_env = False`
- shell 场景，可显式清空：`HTTPS_PROXY= HTTP_PROXY= ALL_PROXY= NO_PROXY='*'`

如果出现 `ProxyError`、`RemoteDisconnected` 或“Remote end closed connection without response”，优先按代理干扰排查，而不是先怀疑 API Key 或模型不可用。

### 6. 返回可复用结果
至少返回：
- 本地输出路径
- request 文件路径
- response 文件路径
- 图片尺寸
- 所用模式

## Output Contract

每张图默认输出以下字段：

1. 图片名称
2. 图片用途
3. 插入位置
4. 风格建议
5. 推荐尺寸
6. 最终 Prompt
7. 执行参数
8. 输出文件路径

## Prompt Rules

为少威公众号生成图片时，prompt 默认遵循以下原则：

- 先写清主体任务，再写风格
- 保持画面单一重心，不要堆满元素
- 优先高级感、克制感、真实感，不要廉价 AI 感
- 避免海报风、营销风、过饱和、过度炫技
- 是否加文字必须显式决定，不再默认“无文字”
- 尽量适配公众号阅读语境，而不是电商主图语境

## Chinese Whiteboard Professor Mode

当用户提到以下任何一种表达时，优先进入该模式：
- 白板教授图
- 中文白板图
- 老师讲课图
- 知识图解
- 讲解图
- 带文字的关系图
- 教授白板板书风格
- 把文档 / 产品描述转换成白板图片

该模式默认要求生成的是**白板风格知识图解**，不是“教室里的一块白板照片”。

默认目标是：把用户给的文章、文档、产品描述或核心观点，转换成一张像教授在白板上讲课时画出的知识板书图。画面需要用图表、箭头、方框、分组、颜色和中文说明，直观呈现核心思想，让用户一眼看懂。

该模式默认要求：
- 图中必须有**可读中文文字**
- 必须有**箭头、方框、分组、映射关系、流程或因果关系**
- 必须有**主标题 + 3-5 个核心模块 + 关键结论 / 落点**
- 必须使用**适度色彩**区分层级，例如蓝色表示系统/技术，橙色表示价值/结果，绿色表示行动/路径，红色表示风险/关键问题
- 白底或浅底
- 像老师讲课的板书总结图，有手绘板书感，但排版清晰
- 图本身要能解释文章，而不是只负责好看

Prompt 中优先使用这种表达：

```text
Create a whiteboard-style knowledge explainer diagram, not a photo of a physical whiteboard. Transform the following content into a professor-style whiteboard board-note illustration. Use clear readable Chinese text, a main title, 3-5 labeled sections, arrows, boxes, simple charts, relationship lines, and color-coded highlights to explain the core idea visually. The layout should feel like structured teaching notes drawn on a clean white background, rich enough to help readers understand, but still clean and readable.
```

避免项：
- 抽象装饰图
- 无字概念图
- 纯氛围图
- 海报风
- 科幻感过重
- 英文大字占主导
- 只画一个孤零零的白板或教室场景
- 只有 2-3 个简单框、信息量过低
- 文字太小、太密、不可读

## Recommended Sizes

- 头图：`1536x1024`
- 文中概念图：`1024x1024`
- 竖版解释图 / 映射图：`1024x1536`

## Integration Guidance

这个 skill 默认是**执行层**，最适合和以下 skill 配合：

- 上游：`shaowei-wechat-illustrator`
- 下游：`shaowei-wechat-image-pipeline`
- 发布层：`wechat-article-publisher`
- 总控：`shaowei-wechat-pipeline`

如果用户说：
- “根据这篇公众号把图都生出来”
- “给我头图和文中图 prompt”
- “按中文白板教授图重做”
- “把图也一起搞定”
- “我给你初稿，你把图也一起搞定”

应优先触发本 skill，与配图规划层协同，而不是只给零散 prompt。
