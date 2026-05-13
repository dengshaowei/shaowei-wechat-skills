# 少威公众号 Skill 迁移清单

## 1. 只迁“固定格式渲染”

### 必带
- `skills/shaowei-wechat-writer/`
- `docs/shaowei-wechat-style-guide.md`

### 建议带
- `docs/shaowei-wechat-sop.md`

### 不必带
- 生图相关 skill
- 微信发布相关 skill

---

## 2. 只迁“中文白板教授图生图能力”

### 必带
- `skills/shaowei-wechat-image-generator/`

### 建议带
- `skills/shaowei-wechat-illustrator/`
- `docs/shaowei-wechat-sop.md`
- 当前可用图片接口配置说明（迁移时按目标环境重配，不直接硬编码密钥）

### 不必带
- `wechat-article-publisher`
- 全文总 pipeline

---

## 3. 只迁“配图闭环”

### 必带
- `skills/shaowei-wechat-illustrator/`
- `skills/shaowei-wechat-image-generator/`
- `skills/shaowei-wechat-image-pipeline/`

### 如果目标仍是微信公众号，再带
- `skills/wechat-article-publisher/`

### 建议带
- `docs/shaowei-wechat-sop.md`
- `docs/shaowei-wechat-caption-styles.md`
- `docs/shaowei-wechat-style-guide.md`

---

## 4. 迁“内容 → 排版 → 草稿箱”基础闭环

### 必带
- `skills/shaowei-wechat-article/`
- `skills/shaowei-wechat-writer/`
- `skills/wechat-article-publisher/`
- `skills/shaowei-wechat-pipeline/`

### 建议带
- `docs/shaowei-wechat-style-guide.md`
- `docs/shaowei-wechat-sop.md`

### 可不带
- 配图相关 skill

---

## 5. 迁“整套公众号生产系统”

### 必带 skill
- `skills/shaowei-wechat-suite/`
- `skills/shaowei-wechat-article/`
- `skills/shaowei-wechat-writer/`
- `skills/shaowei-wechat-illustrator/`
- `skills/shaowei-wechat-image-generator/`
- `skills/shaowei-wechat-image-pipeline/`
- `skills/shaowei-wechat-pipeline/`
- `skills/wechat-article-publisher/`

### 必带文档
- `docs/shaowei-wechat-style-guide.md`
- `docs/shaowei-wechat-sop.md`
- `docs/shaowei-wechat-caption-styles.md`

### 建议一起迁移
- 当前已验证的 request / response / output 路径约定说明
- 图注版本约定（V1 / V2 / V3 / V4）
- 文章类型 → 配图策略矩阵

---

## 6. 迁移注意事项

### 配置与密钥
- skill 可以迁移
- 但接口密钥、微信配置、目标环境路径不要直接硬编码复用
- 迁移时要按新环境重新配置

### 平台差异
- 如果目标不是微信公众号，可保留前面几层，只替换发布层
- 如果目标平台支持不同排版能力，保留 writer 的结构规则，适配输出层即可

### 最佳实践
- 底层 skill 分开保留
- 上层 pipeline 单独保留
- suite 作为总入口一起迁移
