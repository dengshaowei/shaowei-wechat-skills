---
name: shaowei-wechat-pipeline
description: 将少威的公众号完整流程串起来：从用户提供初稿、提纲、碎片想法或网页链接开始，先调用内容生成层整理文章，再调用固定格式渲染层完成定稿；当用户要求配图、生图、中文白板教授图或图文一体化交付时，再接入配图规划层与生图闭环，最后交给发布层做预览检查并推送到微信公众号草稿箱。适用于“按我昨天那篇格式改写后发到草稿箱”“从初稿到公众号草稿一条龙处理”“把图也一起搞定”“把这套流程固定成可复用 SOP”等场景。
---

# Shaowei Wechat Pipeline

## Canonical Format Baseline

默认格式基准不是抽象规则，而是以下三套已确认基准：

- 已发布样文：`https://mp.weixin.qq.com/s/_i_ZURjB-MqTAx0r1LmCvA`
- 已迁移规范：`../shaowei-wechat-suite/references/docs/shaowei-wechat-style-guide.md`
- 已迁移精细 SOP：`../shaowei-wechat-suite/references/docs/shaowei-wechat-sop.md`

如果抽象描述与真实样文冲突，以真实样文和本地规范为准。

## Skill Composition

这个 pipeline 当前默认编排以下 skill：

1. `shaowei-wechat-article`：内容生成层
2. `shaowei-wechat-writer`：固定格式渲染 / 定稿层
3. `wechat-article-publisher`：预览 / 草稿箱发布层

用户一旦要求配图、生图、讲解图、白板教授图或图文一体化交付，就把以下三层接入为**正式子链路**：
- `shaowei-wechat-illustrator`：配图规划层
- `shaowei-wechat-image-generator`：生图执行层
- `shaowei-wechat-image-pipeline`：配图闭环层（规划 → 生图 → 上传素材 → 回填正文 → 重发草稿）

如果运行环境没有完整 skill 机制，也应保持主流程顺序不变：
- 先生成内容
- 再做固定格式渲染
- 如用户要求配图，则插入配图闭环
- 最后预览并发布

## Workflow

1. 接收用户提供的初稿、提纲、碎片想法、本地 Markdown 或链接
2. 先调用内容生成层整理文章，形成中间稿
3. 再调用固定格式渲染层，把中间稿转成少威确认过的公众号成品格式
4. 默认补齐固定尾注
5. 判断是否触发配图闭环；以下任一情况默认触发：
   - 用户明确说“配图 / 生图 / 图文一体化 / 把图也一起搞定”
   - 用户要求中文白板教授图、讲解图、关系图
   - 文章属于解释型 / 方法型 / 拆解型，且配图能明显增强理解
6. 如启用配图，默认优先考虑“开头总览图 + 中段关系图 + 结尾映射图”三段式结构，并调用：
   - `shaowei-wechat-illustrator`
   - `shaowei-wechat-image-generator`
   - `shaowei-wechat-image-pipeline`
7. 做一次本地预览 / dry-run 检查
8. 确认渲染结构无明显偏差后，调用发布层推送到微信公众号草稿箱

## Optional Extension

配图能力现在不是“未来再接”，而是**用户一旦点名就立即接入的标准分支**。

插入位置在“固定格式渲染层”和“预览检查”之间：

- `shaowei-wechat-illustrator`：判断哪里需要图、该配什么图
- `shaowei-wechat-image-generator`：执行真实生图
- `shaowei-wechat-image-pipeline`：上传微信素材、回填正文、重发草稿

其中，解释型 / 方法型 / 拆解型文章，默认优先判断是否需要 **中文白板教授图**，而不是无字氛围图。

## Rendering Rules To Enforce

默认强制执行以下格式：

- 标题下必须紧接居中浅黄编号框 `No.xx`
- 正文必须保持短段落，不写成大段密文
- 一级标题必须使用浅红底 + 左侧竖条的红标块
- 重点句必须使用浅黄高亮 + 深色加粗
- 列举内容按场景选择轻列举或卡片式列表，不要全文只有一种列举形式
- “最后想说”部分一般必须有一个明确重点句，并做高亮
- 结尾固定使用居中长分隔线 + 居中 `End`
- 固定尾注必须按确认版分行排布，不要压成一整坨
- 如果使用配图，**图片解释不要写进正文段落**，默认改成图片下方简短图注
- 图注默认优先使用 `图 1｜xxx` 这种短格式

## Output Requirements

发布前必须检查：

- 标题下编号是否是居中浅黄编号框，而非普通文本
- 正文是否保持短段落节奏
- 一级标题是否已经转成红标块
- 关键判断句是否有必要的高亮，而不是完全没有或过密
- 列举内容是否选对表现形式
- `End` 前是否存在居中长分隔线
- `End` 是否单独居中
- 固定尾注是否按确认版分行

## Important Constraint

用户说“按我的格式”“按前天那篇”“按上一篇的渲染”，都默认指向上述样文 + 本地规范，不再重新猜测格式。
