# 少威公众号 Skill 一页式迁移手册

## 目标

把当前这套公众号能力迁移到其他 agent / 软件里，同时尽量保留：
- 写作 SOP
- 固定格式
- 文风规则
- 流程顺序

当前默认迁移对象是：**无生图 / 无自动配图版本**。

---

## 一、先带走哪些东西

### 必带
- `skills/shaowei-wechat-suite/`
- `skills/shaowei-wechat-article/`
- `skills/shaowei-wechat-writer/`
- `skills/shaowei-wechat-pipeline/`
- `docs/shaowei-wechat-style-guide.md`
- `docs/shaowei-wechat-style-guide-quick.md`

### 选带
- `skills/wechat-article-publisher/`
  - 只有你在新环境还要直接推公众号时才带
- `skills/shaowei-wechat-illustrator/`
  - 后续配图层完善后再正式启用

### 推荐直接用的打包文件
- Core 包：`shaowei-wechat-skills-core-20260428.tar.gz`
- Full 包：`shaowei-wechat-skills-full-20260428.tar.gz`

---

## 二、迁移时最关键的规则

不管换到哪里，都要保留这几个核心规则：

1. 默认按已发布样文格式执行
2. 标题下必须有居中浅黄编号框 `No.xx`
3. 正文必须短段落
4. 一级标题必须红标块
5. 重点句必须浅黄高亮 + 深色加粗
6. 结尾必须有居中分隔线 + `End`
7. 固定尾注必须保留
8. 用户已有 SOP 时，优先按用户 SOP

---

## 三、迁移顺序

### 第一步：先迁 core
先搬：
- suite
- article
- writer
- pipeline
- style guide

这样最快能保住：
- 写稿能力
- 排版能力
- 流程逻辑

### 第二步：再看新平台支不支持发布
如果新平台也能跑脚本、配配置、接微信接口，再迁：
- `wechat-article-publisher`

如果不支持，就先不迁发布层。

### 第三步：同步长期规则
把公众号相关长期规则同步到新环境：
- 文风
- 尾注
- 样文链接
- 渲染规则
- 当前闭环结构

---

## 四、不同软件怎么放

### 情况 A：新环境支持 skill / agent 文件夹
做法：
- 直接复制 skill 目录
- 保留目录结构
- 把 style guide 一起带过去
- 再按新平台要求调整触发描述或 metadata

### 情况 B：新环境只支持 Prompt / Instruction
做法：
- `shaowei-wechat-article` → 作为内容生成规则
- `shaowei-wechat-writer` → 作为排版规则
- `shaowei-wechat-pipeline` → 作为流程顺序说明
- `shaowei-wechat-style-guide.md` → 作为统一格式规范

### 情况 C：新环境只支持单段提示词
做法：
只提炼这三部分：
1. 文风规则
2. 排版规则
3. 执行顺序

不要把所有 skill 原文整坨塞进去。

---

## 五、发布层怎么判断要不要迁

### 要迁
如果你希望新环境：
- 直接预览公众号效果
- 直接推公众号草稿箱
- 直接接微信接口

### 先不用迁
如果你只是想让新环境：
- 写文章
- 排版
- 按你的格式出成品稿

这时只迁 core 就够了。

---

## 六、迁移后怎么验收

先不要拿正式文章做测试。

用一篇随便的测试稿检查：
- 编号框在不在
- 红标标题在不在
- 高亮句在不在
- End 和尾注对不对
- 整体读起来像不像你现在这版

只要这 5 项没跑偏，说明迁移基本成功。

---

## 七、以后怎么维护最稳

每次你改公众号规则，最好同时更新：

1. `docs/shaowei-wechat-style-guide.md`
   - 规则主源
2. 对应 skill
   - 可执行 SOP
3. `MEMORY.md`
   - 长期记忆确认项

这样以后不管迁到哪里，都不容易乱。

---

## 八、一句话结论

迁移时，真正要保住的是：
**你的 SOP、你的格式、你的文风、你的流程。**

最可能因平台变化而重做的是：
**发布器。**
