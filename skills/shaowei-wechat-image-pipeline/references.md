# Shaowei Wechat Image Pipeline References

## 1. 配图闭环执行模板

### Step A：确定是否启用配图闭环
优先启用的文章类型：
- 解释型
- 方法型
- 拆解型
- 认知辨析型
- 需要“图本身承担解释作用”的文章

通常不强启用的文章类型：
- 极短内容
- 纯情绪表达且图片无法提供额外信息
- 纯公告型信息

---

## 2. 文章类型 → 配图策略矩阵

### A. 解释型文章
默认图数：3 张
默认结构：
1. 开头总览图
2. 中段关系图
3. 结尾映射图

优先模式：
- 中文白板教授图
- 带文字关系图
- 讲解图

### B. 方法型文章
默认图数：2-3 张
默认结构：
1. 方法总览图
2. 步骤拆解图
3. 结尾提醒 / 常见误区图（可选）

优先模式：
- 中文白板教授图
- 流程图
- 结构拆解图

### C. 故事型 / 情绪型文章
默认图数：1-2 张
默认结构：
1. 开头场景图
2. 结尾情绪图（可选）

优先模式：
- 场景图
- 情绪图
- 生活感插图

### D. 成长复盘型文章
默认图数：2-3 张
默认结构：
1. 开头主题图
2. 中段结构图 / 对照图
3. 结尾升维图

优先模式：
- 结构图
- 对照图
- 情绪收束图

---

## 3. 中文白板教授图专用规则

### 必须满足
- 图里有可读中文文字
- 有箭头 / 方框 / 关系线 / 分组 / 层级
- 有主标题、3-5 个核心模块、关键结论 / 落点
- 使用适度色彩区分模块和重点
- 白底或浅底
- 像老师讲课板书，但不要画成真实白板照片或教室场景
- 图本身承担解释任务

### 明确禁止
- 抽象装饰图
- 无文字概念图
- 海报感排版
- 纯氛围图
- 英文占主导
- 只画一个白板或教室
- 只有 2-3 个简单框、信息量太低
- 文字太小、太密、不可读

### 推荐结构
- 中心主题 + 分支
- 左右映射
- 上下流程
- 三因素闭环
- 条件因果图
- 漏斗 / 阶梯 / 金字塔 / 飞轮 / 四象限
- 产品价值链路：问题 -> 能力 -> 机制 -> 结果
- 文档转白板：背景 -> 核心观点 -> 关键结构 -> 行动建议

---

## 4. 命令模板

### 4.1 request 文件模板
```json
{
  "model": "gpt-image-2",
  "prompt": "<完整 prompt>",
  "size": "1536x1024",
  "quality": "high",
  "n": 1
}
```

### 4.2 生图 curl 模板
```bash
curl --http1.1 \
  --max-time 650 \
  --connect-timeout 30 \
  --location \
  --request POST "${BASE_URL}/v1/images/generations" \
  --header "Authorization: Bearer ${API_KEY}" \
  --header "Content-Type: application/json" \
  --data-binary "@${REQUEST_JSON}" \
  --output "${RESPONSE_JSON}"
```

当前少威已验证可用的默认基准：
- `BASE_URL=https://new.depot.de5.net`
- `OPENAI_BASE_URL=https://new.depot.de5.net/v1`
- 模型：`gpt-image-2`

安全约束：
- `API_KEY` / `OPENAI_API_KEY` 不要明文写进 skill 文件
- 默认通过当前 shell 环境、私有配置或运行时注入

网络约束（已实测）：
- 如果系统代理开启，`POST /v1/images/generations` 可能被中断
- 默认应优先使用无代理直连模式

推荐无代理调用方式：
```bash
HTTPS_PROXY= HTTP_PROXY= ALL_PROXY= NO_PROXY='*' \
curl --http1.1 \
  --max-time 650 \
  --connect-timeout 30 \
  --location \
  --request POST "${BASE_URL}/v1/images/generations" \
  --header "Authorization: Bearer ${API_KEY}" \
  --header "Content-Type: application/json" \
  --data-binary "@${REQUEST_JSON}" \
  --output "${RESPONSE_JSON}"
```

### 4.3 base64 解码模板
```python
import json, base64, pathlib
p = pathlib.Path(RESPONSE_JSON)
out = pathlib.Path(OUTPUT_PNG)
data = json.loads(p.read_text())
arr = data.get('data') or []
item = arr[0] if arr else {}
b64 = item.get('b64_json') or item.get('base64') or item.get('image_base64')
out.write_bytes(base64.b64decode(b64))
```

### 4.4 微信素材上传模板
```python
requests.post(
  'https://api.weixin.qq.com/cgi-bin/material/add_material',
  params={'access_token': token, 'type': 'image'},
  files={'media': (filename, open(filename, 'rb'), 'image/png')}
)
```

### 4.5 重发草稿模板
```bash
python3 skills/wechat-article-publisher/scripts/publish_wechat.py \
  <markdown-file> \
  --config skills/wechat-article-publisher/config.json \
  --template viral
```

---

## 5. 路径与命名约定

### request 文件
- `.tmp/ai-cover.request.json`
- `.tmp/ai-concept.request.json`
- `.tmp/ai-ending.request.json`

### response 文件
- `.tmp/image-responses/cover.response.json`
- `.tmp/image-responses/concept.response.json`
- `.tmp/image-responses/ending.response.json`

### 输出图片目录
- 普通白板图：`.tmp/generated-images-whiteboard/`
- 中文白板教授图：`.tmp/generated-images-chinese-board/`

### 文件命名
- `ai-cover-*.png`
- `ai-concept-*.png`
- `ai-ending-*.png`

---

## 6. 图注样式版本表

### Caption V1：普通简短图注
形式：
- 图下方一行灰色小字
- 居中
- 不强调

适合：
- 常规版本
- 用户只要求“简短”

### Caption V2：明显居中图注
形式：
- 图下方一行更明显的居中文字
- 留白更统一

适合：
- 用户要求“更居中”“更明显”

### Caption V3：居中胶囊图注
形式：
- 胶囊样式
- 白底 / 半透明底
- 贴近图片下沿

适合：
- 希望图注更像贴纸 / 标题条

### Caption V4：视觉右移补偿图注
形式：
- 在 V3 基础上，按微信观感做右移补偿
- 必要时不同图片分别补偿

适合：
- 用户明确说“看起来不够居中”
- 微信实际渲染与理论居中有偏差

---

## 7. 发布前检查清单

### 正文检查
- [ ] 标题使用 frontmatter `title:`，未重复写正文标题
- [ ] 标题下编号框存在
- [ ] 正文短段落成立
- [ ] 一级标题红标块正常
- [ ] 重点句高亮正常
- [ ] `End` 与尾注正常

### 图片检查
- [ ] 图片已真实生成
- [ ] 图片风格符合当前模式
- [ ] 中文白板教授图包含文字与箭头
- [ ] 图片 URL 为微信素材 URL，不是本地路径
- [ ] 图片位置插入正确
- [ ] 图注格式符合当前版本

### 发布检查
- [ ] 使用 `python3`
- [ ] 发布脚本返回 `success: true`
- [ ] 记录最新 `draft_media_id`
- [ ] 保留 preview 文件路径

---

## 8. 当前默认偏好（已从真实交互确认）

- 解释型文章优先中文白板教授图
- 不要把解释图片的话写进正文
- 图注默认单独放图片下方
- 图注优先短格式：`图 1｜xxx`
- 图注样式可按微信观感做补偿，不死守理论居中
- 默认只发草稿箱，不直接正式发布
