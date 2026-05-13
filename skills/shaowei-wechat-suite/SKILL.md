---
name: shaowei-wechat-suite
description: 少威公众号完整技能体系总入口。用于组织和说明一套可复用、可迁移、可组合的公众号生产流水线，包括内容生成、固定格式渲染、配图规划、生图执行、微信素材上传、正文回填、图注样式控制与公众号草稿箱发布。适用于希望把公众号写作 SOP 沉淀成可迁移 skill 套件，并在 OpenClaw 或其他 agent / 软件中复用的场景。
---

# Shaowei Wechat Suite

## Purpose

这个 skill 不负责直接写文章或发布。

它的作用是：
- 作为少威公众号体系的总说明入口
- 定义整套 skill 的职责边界与串联顺序
- 说明哪些模块适合单独迁移，哪些模块适合整套迁移
- 为 OpenClaw 与其他软件提供统一复用方案

## Current Structure

这套能力当前不是一个“大一统 skill”，而是：

- **底层能力分开沉淀**
- **上层 pipeline 负责编排**
- **suite 负责总入口、迁移说明与组合关系**

也就是说：
- 可以单独迁移某一个 skill
- 可以迁移某一段子流程
- 也可以整套打包迁移

## Skill Map

### A. 原子能力层

1. `shaowei-wechat-article`
   - 内容生成层
   - 负责把初稿、提纲、碎片想法整理成完整公众号正文

2. `shaowei-wechat-writer`
   - 固定格式渲染层
   - 负责按少威确认过的公众号格式进行排版、重点强化、尾注收尾

3. `shaowei-wechat-illustrator`
   - 配图规划层
   - 负责判断哪里适合插图、每张图承担什么作用、该用什么图类型

4. `shaowei-wechat-image-generator`
   - 生图执行层
   - 负责写 prompt、调用 OpenAI-compatible 图片接口、保存真实图片文件

5. `wechat-article-publisher`
   - 微信发布层
   - 负责 dry-run、草稿箱推送、可选正式发布

### B. 流程编排层

6. `shaowei-wechat-image-pipeline`
   - 配图闭环层
   - 负责：配图规划 → 生图执行 → 上传微信素材 → 回填正文 → 重发草稿

7. `shaowei-wechat-pipeline`
   - 全文闭环总控层
   - 负责：内容生成 → 固定格式渲染 → 配图闭环（可选）→ 草稿箱发布

## Current Recommended Workflow

### 最小内容闭环
1. `shaowei-wechat-article`
2. `shaowei-wechat-writer`
3. `wechat-article-publisher`

### 配图闭环
1. `shaowei-wechat-illustrator`
2. `shaowei-wechat-image-generator`
3. `shaowei-wechat-image-pipeline`
4. `wechat-article-publisher`

### 全量闭环
1. `shaowei-wechat-article`
2. `shaowei-wechat-writer`
3. `shaowei-wechat-illustrator`
4. `shaowei-wechat-image-generator`
5. `shaowei-wechat-image-pipeline`
6. `wechat-article-publisher`
7. `shaowei-wechat-pipeline`

## Migration Modes

### 模式 1：单个能力迁移
适用于：
- 只想迁移“固定格式渲染”
- 只想迁移“中文白板教授图生图能力”
- 只想迁移“微信发布能力”

做法：
- 只带对应 skill + 它依赖的 reference / docs

### 模式 2：子流程迁移
适用于：
- 只迁移“配图 → 生图 → 上传微信 → 回填正文”
- 只迁移“内容生成 → 排版 → 草稿箱发布”

做法：
- 带一组相关 skill + 对应 pipeline

### 模式 3：整套迁移
适用于：
- 想把少威公众号完整生产体系搬到别的 agent / 软件

建议携带：
- 全部 skill
- 本 skill 已打包的 `references/docs/shaowei-wechat-style-guide.md`
- 本 skill 已打包的 `references/docs/shaowei-wechat-sop.md`
- 本 skill 已打包的 `references/docs/shaowei-wechat-caption-styles.md`

## Shared Baselines

整套体系共享以下基准：

- 已发布样文：`https://mp.weixin.qq.com/s/_i_ZURjB-MqTAx0r1LmCvA`
- 已迁移格式规范：`references/docs/shaowei-wechat-style-guide.md`
- 已迁移精细 SOP：`references/docs/shaowei-wechat-sop.md`
- 已迁移图注样式表：`references/docs/shaowei-wechat-caption-styles.md`
- 已迁移迁移清单：`references/docs/shaowei-wechat-migration-checklist.md`
- 已迁移架构图与调用顺序：`references/docs/shaowei-wechat-architecture.md`

如果抽象口头描述与已确认样文冲突，以样文和本地规范为准。

## Migration Shortcuts

如果只迁移某一部分，优先参考：
- `references/docs/shaowei-wechat-migration-checklist.md`
- `references/docs/shaowei-wechat-architecture.md`

最常见的三种迁移方式：
- **只迁生图**：带 `shaowei-wechat-image-generator` 为主
- **只迁配图闭环**：带 `illustrator + image-generator + image-pipeline`
- **迁整套**：带全部 skill + style guide + sop + caption styles + migration checklist + architecture

迁移原则：
- 底层 skill 分开保留
- pipeline 单独保留
- suite 作为总入口一起迁移

## Current Confirmed Preferences

当前已经沉淀下来的偏好包括：

- 解释型 / 方法型 / 拆解型文章，优先判断是否使用 **中文白板教授图**
- 中文白板教授图默认是“教授白板板书风格的知识图解”，不是现实白板照片
- 中文白板教授图必须有文字、箭头、方框、分组、关系线、适度色彩和 3-5 个核心模块
- 图片解释不要写进正文段落
- 图片说明默认单独放在图片下方
- 图注默认优先短格式：`图 1｜xxx`
- 图注样式允许按微信渲染观感做补偿，不死守理论居中
- 默认只发草稿箱，不直接正式发布

## When To Use This Skill

当用户在做以下任一类事情时，应优先参考本 skill：

- 想把公众号流程做成长期复用 SOP
- 想把公众号能力迁移到别的 agent / 软件
- 想理解每个公众号 skill 的职责边界
- 想知道应该整体打包还是分层迁移
- 想扩展公众号体系，例如后续增加选题库、封面能力、更多图注样式或更多生图模式
