# 少威公众号 Skill 架构图与调用顺序

## 1. 架构分层

### 第一层：原子能力层
这些 skill 可以单独迁移、单独复用。

- `shaowei-wechat-article`
  - 职责：内容生成 / 中间稿整理
  - 平台绑定：低

- `shaowei-wechat-writer`
  - 职责：固定格式渲染 / 定稿
  - 平台绑定：低

- `shaowei-wechat-illustrator`
  - 职责：配图规划
  - 平台绑定：低

- `shaowei-wechat-image-generator`
  - 职责：生图执行
  - 平台绑定：中
  - 依赖：图片接口可用

- `wechat-article-publisher`
  - 职责：微信草稿箱发布
  - 平台绑定：高（微信）

---

### 第二层：流程编排层
这些 skill 用来把原子能力串起来。

- `shaowei-wechat-image-pipeline`
  - 职责：配图闭环
  - 典型链路：配图规划 → 生图 → 上传微信素材 → 回填正文 → 重发草稿

- `shaowei-wechat-pipeline`
  - 职责：全文闭环
  - 典型链路：内容生成 → 固定格式渲染 → 配图闭环（可选）→ 草稿箱发布

---

### 第三层：套件入口层
- `shaowei-wechat-suite`
  - 职责：总入口、迁移说明、组合关系、默认基线
  - 不负责直接执行生产动作

---

## 2. 依赖关系图

### 内容闭环依赖
`shaowei-wechat-article`
→ `shaowei-wechat-writer`
→ `wechat-article-publisher`

### 配图闭环依赖
`shaowei-wechat-illustrator`
→ `shaowei-wechat-image-generator`
→ `shaowei-wechat-image-pipeline`
→ `wechat-article-publisher`

### 全量闭环依赖
`shaowei-wechat-article`
→ `shaowei-wechat-writer`
→ `shaowei-wechat-illustrator`
→ `shaowei-wechat-image-generator`
→ `shaowei-wechat-image-pipeline`
→ `wechat-article-publisher`
→ `shaowei-wechat-pipeline`

说明：
- `shaowei-wechat-pipeline` 是总控视角，不是必须最后物理执行的脚本，而是整体流程编排定义。
- `shaowei-wechat-suite` 不参与执行链，只负责说明和迁移入口。

---

## 3. 调用顺序图

### A. 最小内容闭环
1. 输入初稿 / 提纲 / 想法
2. `shaowei-wechat-article` 整理正文
3. `shaowei-wechat-writer` 转成固定公众号格式
4. `wechat-article-publisher` dry-run / 草稿箱发布

### B. 配图闭环
1. 输入已成稿文章
2. `shaowei-wechat-illustrator` 规划配图
3. `shaowei-wechat-image-generator` 写 prompt + 调接口生图
4. `shaowei-wechat-image-pipeline` 上传素材、回填正文、重发草稿
5. `wechat-article-publisher` 输出最新草稿

### C. 全量生产闭环
1. 输入初稿
2. 内容整理
3. 固定格式渲染
4. 判断是否启用配图闭环
5. 配图规划
6. 生图执行
7. 上传素材
8. 回填正文
9. 设置图注样式
10. 重发草稿箱
11. 最终检查

---

## 4. 平台绑定分析

### 平台无关 / 易迁移
- `shaowei-wechat-article`
- `shaowei-wechat-writer`
- `shaowei-wechat-illustrator`

### 中度平台相关
- `shaowei-wechat-image-generator`
  - 与具体图片接口有关
  - 但不强绑定微信

### 高度平台绑定
- `wechat-article-publisher`
  - 强绑定微信公众号接口

### 半绑定流程层
- `shaowei-wechat-image-pipeline`
  - 上游不强绑定
  - 但“上传素材 + 回填正文 + 重发草稿”这部分绑定微信

---

## 5. 迁移优先级建议

### 如果目标平台不是微信公众号
优先迁移：
- `article`
- `writer`
- `illustrator`
- `image-generator`

替换：
- `wechat-article-publisher`
- `image-pipeline` 中与微信素材/草稿箱相关的下游动作

### 如果目标平台仍是微信公众号
整套可直接迁移，但需重新配置：
- 微信 app_id / app_secret
- 图片接口 base_url / api_key
- 新环境路径

---

## 6. 推荐理解方式

把这套体系理解成：

- `article / writer / illustrator / image-generator / publisher` = 零部件
- `image-pipeline / wechat-pipeline` = 装配线
- `suite` = 总装说明书

这样后续迁移、拆分、复用时，不容易乱。
