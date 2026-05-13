# 少威公众号 Skill 迁移清单

## 一、建议一起迁移的核心 skill

### 1. 总说明入口
- `skills/shaowei-wechat-suite/`

作用：
- 说明整套 skill 的架构
- 定义职责边界
- 作为跨平台复用的总入口

### 2. 内容生成层
- `skills/shaowei-wechat-article/`

作用：
- 把初稿 / 问答 / 提纲 / 碎片想法整理成完整公众号文章中间稿

### 3. 固定格式渲染层
- `skills/shaowei-wechat-writer/`

作用：
- 按少威固定公众号格式渲染成定稿

### 4. 总控编排层
- `skills/shaowei-wechat-pipeline/`

作用：
- 把内容生成 → 渲染定稿 → 预览发布串起来

## 二、可选迁移项

### 5. 发布层
- `skills/wechat-article-publisher/`

说明：
- 如果目标环境仍然要直接推微信公众号草稿箱，建议一起迁移
- 如果目标环境只需要写稿和排版，不一定要迁移这一层
- 如果目标环境的发布方式不同，这一层通常要做适配

### 6. 配图扩展层
- `skills/shaowei-wechat-illustrator/`

说明：
- 当前不是默认闭环的一部分
- 后续配图能力完善后可再正式启用

## 三、建议一起带走的共享规范文件

### 7. 公众号固定格式规范
- `docs/shaowei-wechat-style-guide.md`
- `docs/shaowei-wechat-style-guide-quick.md`

作用：
- 作为整套 skill 的统一格式基准
- 避免迁移后只带了 skill，没带规则源文件

## 四、建议一起带走的长期记忆基准

### 8. 长期记忆中的公众号规则
建议至少同步这些内容到新环境：
- 公众号文风规则
- 固定尾注
- 已发布样文链接
- 已确认渲染规则
- 当前默认闭环结构

如果新环境也有 memory 机制，建议把这些条目同步进去。

## 五、迁移优先级建议

### 最小可用迁移包
适合“先搬过去能写能排版”：
- `shaowei-wechat-suite`
- `shaowei-wechat-article`
- `shaowei-wechat-writer`
- `shaowei-wechat-pipeline`
- `shaowei-wechat-style-guide.md`
- `shaowei-wechat-style-guide-quick.md`

### 完整迁移包
适合“尽量保留现在这套能力”：
- 上述全部
- `wechat-article-publisher`
- `shaowei-wechat-illustrator`
- 与公众号相关的长期记忆条目

## 六、一句话结论

最该迁移的是：
**SOP、格式规范、文风规则、流程编排。**

最可能需要因平台变化而适配的是：
**发布层。**
