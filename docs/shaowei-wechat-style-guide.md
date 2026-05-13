# 少威公众号固定写作与渲染规范

> 适用范围：后续所有少威公众号文章默认按此模式执行，除非用户明确提出新的调整。
> 当前基准版本：2026-04-25 凌晨，经《为什么有了大模型之后，还需要 Agent？》反复校准确认。

---

## 一、总原则

后续所有公众号文章，默认同时遵守这三层：

1. **渲染格式固定**
2. **文风结构固定**
3. **收尾模板固定**

不要再每次重新猜格式。

如果后续有局部新增要求，只增量修改对应模块，不要整体推翻。

---

## 二、唯一格式基准

默认参考基准：

- 已发布样文：`https://mp.weixin.qq.com/s/_i_ZURjB-MqTAx0r1LmCvA`
- 已校准稿件：`/Users/dengdengdeng/.openclaw/workspace/drafts/why-agent-after-llm-v2.1-template.md`
- 旧版预览样式参考：`/Users/dengdengdeng/.openclaw/workspace/很多人聊-ai-第一步就聊错了-ai-ai产品-ai行业-根本不是一回事-wechat-preview.html`

如果抽象描述与真实样文冲突，以真实样文和已校准稿件为准。

---

## 三、标题区规则

### 1. 标题
- 文章标题正常显示
- 不在正文重复标题

### 2. 标题下编号框
标题下方必须紧接编号框，不要写成普通裸文本。

固定样式：

```html
<p align="center" style="margin: 14px 0 24px 0;">
  <span style="display:inline-block;padding:8px 18px;background:#FFF7E6;border:1px solid #F3D9A4;border-radius:8px;color:#5F5130;font-size:15px;line-height:1.8;">
    No.xx
  </span>
</p>
```

规则：
- 居中
- 浅黄底
- 有细边框
- 有圆角
- 标题下直接接编号框
- 若用户未指定编号，保留 `No.xx`

---

## 四、正文整体渲染规则

### 1. 正文基础段落样式
普通正文统一使用：

```html
<p style="margin:0.95em 0;line-height:1.92;font-size:16px;color:#2b2f38;text-align:justify;letter-spacing:0.01em;text-indent:0;">正文内容</p>
```

特点：
- 16px 字号
- 行高 1.92
- 深灰字色
- 两端对齐
- 无首行缩进
- 段距统一

### 2. 断句规则
这是强约束。

后续默认：
- 一句话说完就隔开
- 不要一大段话堆在一起
- 一层意思一段
- 转折句单独成段
- 结论句单独成段

禁止：
- 一段里塞四五句
- 把解释、举例、结论混在同一个大段里
- 写得像论文，不像公众号

---

## 五、标题层级规则

### 1. 一级标题
一级结构统一使用红标块：

```html
<h2 style="margin:1.45em 0 0.72em;padding:0.46em 0.72em;font-size:1.2em;line-height:1.45;color:#7a1f1f;font-weight:800;background:#fff2f2;border-left:4px solid #ef4444;border-radius:4px;">一、一级标题</h2>
```

特点：
- 浅红底
- 左侧红竖条
- 深红色文字
- 加粗
- 与正文有明显层级区分

### 2. 次级标题
需要二级拆分时，可使用轻量小标题。

适用于：
- 一个大节下再拆 3-4 个小点
- 结构讲解类文章

但不要把所有层级都做成同样重的红标块。

---

## 六、重点句规则

重点句统一用浅黄高亮 + 深色加粗。

模板：

```html
<strong style="font-weight:800;color:#9a3412;background:#fff3d6;padding:0 2px;border-radius:3px;">重点句</strong>
```

适用场景：
- 核心判断
- 关键转折
- 金句
- 一段的结论句
- 文末“最后想说”里的关键落点

### 额外明确规则
用户已确认：

- **正文最后“最后想说”这个部分，一般一定会有重点。**
- 如果有明确收束句、核心判断句、最终落点句，要按此规则做重点标注。

但注意：
- 不要一段全都高亮
- 一节里重点不要过密
- 高亮是为了聚焦，不是为了满屏装饰

---

## 七、举列内容模板

后续正文中的列举，不要只会硬拆成一句一行。

需要根据内容类型，在两种方式中选择：

### 形式 A：一句一行轻列举
适合：
- 节奏轻
- 内容短
- 想保留呼吸感
- 更像一行一行往下读

示例：

```html
<p style="...">拆解任务。</p>
<p style="...">调用工具。</p>
<p style="...">持续反馈。</p>
```

### 形式 B：卡片式列表
适合：
- 一组并列信息需要一起看
- 读者需要快速扫点
- 内容本身就是能力项、步骤项、问题项、维度项

模板：

```html
<ul style="margin:0.98em 0;padding:0.82em 1em 0.82em 1.62em;line-height:1.86;color:#2d3445;background:#fffdf8;border-radius:8px;border:1px solid #ffe8c4;box-shadow:0 2px 10px rgba(251,146,60,0.08);list-style-position:outside;list-style-type:disc;">
  <li style="margin:0.28em 0;font-size:16px;line-height:1.82;text-indent:0;">第一条</li>
  <li style="margin:0.28em 0;font-size:16px;line-height:1.82;text-indent:0;">第二条</li>
</ul>
```

### 选择原则
- 若是一组完整并列项，优先考虑卡片式列表
- 若是为了保持轻盈节奏，优先一句一行
- 不要通篇只有一种列举方式

---

## 八、文风规则

后续所有公众号文章，在满足渲染格式的前提下，文风默认按少威固定方式执行。

### 1. 开头
- 从生活感、现实感、反差感切入
- 避免一上来就讲概念
- 先把读者带进场景

### 2. 中段
常见结构：
- 生活切口
- 技术拆解
- 抽象升维
- 落到选择 / 成长 / 现实判断

### 3. 表达风格
- 理性但有温度
- 不要学术腔
- 不要空洞鸡汤
- 善于把技术问题翻译成普通人能理解的话
- 多用短段落，降低阅读压力

### 4. 收尾
- 一般会回到更高一层的判断
- 最后常落在：选择、成长、行动、现实理解
- 最后一节通常留一个互动问题或开放讨论口

---

## 九、结尾区规则

### 1. 分隔线和 End
结尾固定使用：

```html
<p align="center" style="margin:36px 0 8px 0;letter-spacing:0.08em;color:#6b7280;">────────────</p>
<p align="center" style="margin:0 0 28px 0;color:#6b7280;">End</p>
```

已确认规则：
- 分隔线是一长条
- 居中显示
- `End` 单独一行
- `End` 居中显示
- 这是固定收尾，不再改成左对齐

### 2. 固定尾注排版
尾注以后默认按用户最终确认的排版执行：

```html
<p style="margin:1.1em 0 0.6em 0;line-height:1.9;font-size:15px;color:#4b5563;text-align:left;">🌟 关于我：ENFJ-A | 终身成长者 | 务实的理想主义者</p>

<p style="margin:0.6em 0;line-height:1.9;font-size:15px;color:#4b5563;text-align:left;">📝 在这里，我们可以一起探讨：</p>

<p style="margin:0.25em 0;line-height:1.9;font-size:15px;color:#4b5563;text-align:left;">🤖 具身智能转行：我的实战经验与行业观察；</p>

<p style="margin:0.25em 0;line-height:1.9;font-size:15px;color:#4b5563;text-align:left;">📅 个人成长规划：如何拆解目标，让理想落地；</p>

<p style="margin:0.25em 0 0.6em 0;line-height:1.9;font-size:15px;color:#4b5563;text-align:left;">✨ 生活感悟复盘：自我突破与相信的力量。</p>

<p style="margin:0.6em 0 0.25em 0;line-height:1.9;font-size:15px;color:#4b5563;text-align:left;">请相信，我们每个人都与众不同，也终将实现自己的愿望。</p>

<p style="margin:0.25em 0 0.6em 0;line-height:1.9;font-size:15px;color:#4b5563;text-align:left;">保持联系 🔗 让我们一起记录，一起向上生长 🌱</p>

<p style="margin:0.6em 0 0.25em 0;line-height:1.9;font-size:15px;color:#4b5563;text-align:left;">围观朋友圈：dengdengdengdeng4101（备注：公众号）</p>

<p style="margin:0.25em 0 0 0;line-height:1.9;font-size:15px;color:#4b5563;text-align:left;">小红书/即刻：少威shaowei</p>
```

规则说明：
- 不要把尾注压成一整坨
- 也不要拆得太碎导致失去整体感
- 按用户最终确认的这版分行方式执行

---

## 十、非协商项（默认不再来回改）

后续默认坚持：

- 不把 `No.xx` 写成普通裸文本
- 不把正文改成大段密文
- 不忽略红标一级标题
- 不忽略重点高亮
- 不忽略卡片式列表与轻列举的区分
- 不把 `End` 改掉位置
- 不随意改固定尾注内容和分行
- 用户说“按我的格式”，优先按本规范，不再重新猜

---

## 十一、实际执行建议

以后处理少威公众号文章，默认流程：

1. 先完成内容写作/改写
2. 再按本规范做排版
3. 检查：
   - 是否有编号框
   - 是否有红标一级标题
   - 是否有必要的重点高亮
   - 是否有合适的列举形式
   - “最后想说”是否标出了重点
   - `End` 和分隔线是否居中
   - 固定尾注是否按确认版排好
4. 再推草稿箱

---

## 十二、一句话记忆版

少威公众号固定模式 =

**标题下编号框 + 短段落 + 红标一级标题 + 浅黄重点高亮 + 轻列举/卡片列表按需切换 + “最后想说”必须有重点 + 居中分隔线与 End + 固定尾注按确认版分行。**
