# 少威公众号 Skill 打包说明

## 目标

把当前这套公众号 skill 体系整理成一个可迁移、可备份、可在其他 agent / 软件中复用的打包目录。

## 当前推荐打包内容

### 必选
- `skills/shaowei-wechat-suite/`
- `skills/shaowei-wechat-article/`
- `skills/shaowei-wechat-writer/`
- `skills/shaowei-wechat-pipeline/`
- `docs/shaowei-wechat-style-guide.md`
- `docs/shaowei-wechat-style-guide-quick.md`

### 可选
- `skills/wechat-article-publisher/`
- `skills/shaowei-wechat-illustrator/`
- `MEMORY.md` 中与公众号相关的规则摘录

## 为什么这样打包

因为这套体系本质上分成两类：

### A. 平台无关资产
这些是最重要的：
- 写作 SOP
- 格式渲染规则
- 文风约束
- 流程编排方式

它们可以跨平台复用。

### B. 平台相关执行器
这部分通常需要按目标环境适配：
- 微信公众号发布脚本
- 本地配置
- 运行命令

## 迁移到其他环境时怎么用

### 情况 1：目标环境也支持 skill / agent 文件结构
直接复制这些目录和规范文件进去，再根据目标平台调整发布层。

### 情况 2：目标环境不支持完整 skill 机制
也可以拆开使用：
- 把 `shaowei-wechat-style-guide.md` 当成统一规则文档
- 把 `shaowei-wechat-article` 当成“内容生成 prompt / SOP”
- 把 `shaowei-wechat-writer` 当成“排版 prompt / SOP”
- 把 `shaowei-wechat-pipeline` 当成“流程说明文档”

## 发布层适配建议

如果新环境还要推公众号：
- 保留 `wechat-article-publisher`
- 检查脚本依赖、配置路径、微信接口权限
- 按新环境重新设置 `config.json`

如果新环境只负责写稿：
- 可以暂时不迁移 `wechat-article-publisher`
- 只保留内容层 + 排版层 + 总说明层

## 推荐打包产物

建议最终保留两个版本：

### 1. 最小可用包
只包含：
- suite
- article
- writer
- pipeline
- style guide

适合快速迁移、快速复用。

### 2. 完整包
包含：
- 最小可用包全部内容
- publisher
- illustrator
- 公众号相关长期记忆摘录

适合完整备份和长期资产沉淀。

## 建议命名

### 最小可用包
- `shaowei-wechat-skills-core-YYYYMMDD.tar.gz`

### 完整包
- `shaowei-wechat-skills-full-YYYYMMDD.tar.gz`

## 打包后建议验证

迁移前或迁移后，至少检查：
- 是否保留了样文链接基准
- 是否保留了格式规范文件
- 是否保留了尾注规则
- 是否保留了闭环结构说明
- 若迁移发布层，是否重新配置了公众号发布参数
