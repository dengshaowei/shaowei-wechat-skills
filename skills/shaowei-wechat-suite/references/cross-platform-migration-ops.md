# 少威公众号 Skill 跨软件迁移操作说明

## 适用场景

这份说明适合你把当前公众号 skill 体系迁移到：
- 其他 agent 系统
- Claude / Codex / Cursor / 其他 AI 软件
- 自己的知识库 / Prompt 库 / SOP 库

当前默认迁移对象是**无生图 / 无自动配图版本**。

---

## 一、你现在这套 skill 的核心结构

当前默认闭环：

1. `shaowei-wechat-article`
   - 内容生成
2. `shaowei-wechat-writer`
   - 固定格式渲染 / 定稿
3. `wechat-article-publisher`
   - 预览 / 草稿箱发布
4. `shaowei-wechat-pipeline`
   - 总控编排
5. `shaowei-wechat-suite`
   - 总说明入口

可选扩展：
- `shaowei-wechat-illustrator`
  - 配图规划层（当前不在默认主闭环）

---

## 二、迁移时先判断你要哪一种方式

### 方式 A：完整 skill 迁移
适合：
- 新环境也支持 skill / agent 文件夹
- 你希望尽量保留当前结构

你要带走：
- `shaowei-wechat-suite`
- `shaowei-wechat-article`
- `shaowei-wechat-writer`
- `shaowei-wechat-pipeline`
- `docs/shaowei-wechat-style-guide.md`
- `docs/shaowei-wechat-style-guide-quick.md`

如果新环境也能跑公众号发布脚本，再额外带：
- `wechat-article-publisher`

### 方式 B：Prompt / SOP 迁移
适合：
- 新环境不支持完整 skill 机制
- 你只想保留写作规则和流程

你要带走：
- 文风规则
- 排版规范
- 流程顺序
- 固定尾注
- 已发布样文链接

这时可以把：
- `shaowei-wechat-article` 当成“内容生成 SOP”
- `shaowei-wechat-writer` 当成“排版 SOP”
- `shaowei-wechat-pipeline` 当成“执行顺序说明”

---

## 三、最推荐的迁移步骤

### 第一步：用 core 包先迁移
优先使用这个包：
- `shaowei-wechat-skills-core-20260428.tar.gz`

原因：
- 最干净
- 不依赖发布器
- 迁移成本最低
- 先把写作和排版能力稳定搬过去

### 第二步：放到目标环境里
如果目标环境支持 skill 文件夹：
- 直接解压
- 把 `skills/` 下相关目录放到新环境的 skill 目录
- 把 `docs/` 下的格式规范一起放进去

如果目标环境不支持：
- 单独打开各个 `SKILL.md`
- 把关键内容提炼成该平台可用的 system prompt / project instruction / agent instruction

### 第三步：同步长期规则
至少把这些同步到新环境：
- 默认按已发布样文格式执行
- 标题下浅黄编号框
- 正文短段落
- 一级标题红标块
- 重点句浅黄高亮
- 居中分隔线 + End
- 固定尾注
- 用户已有 SOP 时优先按用户 SOP

### 第四步：做一次最小验证
迁移后，不要先上正式内容。

先让新环境生成一篇测试稿，检查：
- 编号框是否保留
- 红标标题是否保留
- 高亮句是否保留
- End 和尾注是否正确
- 整体节奏是否像你现在这版

---

## 四、迁移到不同类型软件时怎么落地

### 1. 迁移到支持 Skill / Agent 文件结构的软件
做法：
- 直接复制 skill 文件夹
- 保留目录结构
- 把规范文档一起带过去
- 根据新平台要求调整 metadata 或触发描述

重点：
- 先保证 `article`、`writer`、`pipeline` 能正常被读取
- `publisher` 看新平台能不能执行脚本，再决定是否接入

### 2. 迁移到 Claude / Codex / 通用大模型工作台
做法：
- 把 `shaowei-wechat-suite` 作为总说明
- 把 `shaowei-wechat-article` 做成“写文 instruction”
- 把 `shaowei-wechat-writer` 做成“排版 instruction”
- 把 `shaowei-wechat-style-guide.md` 当成共享 reference

推荐组织方式：
- 一个总 Prompt：说明这是少威公众号 SOP
- 一个内容生成 Prompt
- 一个排版 Prompt
- 一个规范文档

### 3. 迁移到不支持多文件、只支持单段提示词的软件
做法：
- 不要把全部 skill 原文一股脑塞进去
- 只提炼最关键的：
  - 文风规则
  - 排版规则
  - 固定尾注
  - 流程顺序

推荐压缩成三段：
1. 内容生成规则
2. 格式渲染规则
3. 执行顺序规则

---

## 五、发布层怎么处理

### 如果新环境也要直接推公众号
你需要迁移：
- `wechat-article-publisher`
- 配置文件
- 脚本依赖
- 微信接口权限

并检查：
- Python 依赖是否能装
- 配置路径是否需要重改
- 新环境是否允许本地脚本执行

### 如果新环境只负责写稿和排版
你可以先不迁移发布层。

这时只保留：
- `suite`
- `article`
- `writer`
- `pipeline`
- style guide

这样也已经能完整复用你最核心的公众号能力。

---

## 六、我建议你以后怎么维护

### 最稳的维护方式
以后每次你改规则，尽量同时改这三处：

1. `docs/shaowei-wechat-style-guide.md`
   - 作为格式规范主源
2. 对应 skill
   - 作为可执行 SOP
3. `MEMORY.md`
   - 作为长期记忆确认项

### 为什么要这样
因为：
- `style guide` 是规则源
- `skill` 是操作系统
- `memory` 是确认过的长期偏好

三者一致，迁移时最稳。

---

## 七、推荐你的实际用法

### 如果你只是想快速搬走
直接拿：
- core 包
- migration-checklist.md
- packaging-guide.md
- 这份操作说明

### 如果你想长期资产化
建议保留：
- full 包
- style guide
- MEMORY 里的公众号规则摘录
- 后续再补配图层和封面层

---

## 八、一句话总结

迁移时，最该保留的是：
**你的 SOP、你的格式、你的文风、你的流程。**

最需要按环境适配的是：
**发布器。**

所以你现在这套 skill，已经具备跨软件复用的基础；以后无论换平台，核心资产都不会丢。
