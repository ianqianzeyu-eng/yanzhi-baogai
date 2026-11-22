<div align="center">

# yanzhi-baogai · 颜值上限爆改 Skill

**把短视频里爆火的「我能看到你的颜值上限」，拆成一套可复用、可解释、合规的 AI 工作流。**
**Turn the viral "I can see your beauty ceiling" trend into a reusable, explainable, and compliant AI workflow.**

![license](https://img.shields.io/badge/license-MIT-green.svg)
![platform](https://img.shields.io/badge/platform-WorkBuddy%20%7C%20CodeBuddy%20%7C%20Coze%20%7C%20Claude-blue.svg)
![doubao](https://img.shields.io/badge/豆包-智能体可用-orange.svg)
![python](https://img.shields.io/badge/python-3.8%2B-yellow.svg)
![status](https://img.shields.io/badge/status-stable-brightgreen.svg)

[中文](#中文介绍) · [English](#english) · [多平台支持](#多平台支持--multi-platform)

</div>

---

<a name="中文介绍"></a>

## 中文介绍

一个跨平台技能：照片诊断 → 双分数评估 → 优先级改造清单 → AI 改造预览 → 前后对比图 → 短视频脚本。**原生支持 WorkBuddy / CodeBuddy / 扣子 Coze / Claude 等 SKILL.md 平台，豆包 App 也能通过智能体提示词使用。**

灵感来自抖音博主「微波炉（形象改造）」的全部可见作品拆解，结合公开的人脸美学、色彩诊断与摄影资料整理。详见 [`references/creator-research.md`](references/creator-research.md) 与 [`references/assessment-framework.md`](references/assessment-framework.md)。

> 分数仅作娱乐向参考，不构成客观评价或医美建议。所有 AI 生成内容必须显式标识。

### 功能亮点

| 功能 | 说明 |
| --- | --- |
| 六因子视觉诊断 | 骨相比例、五官表情、皮肤状态、头面修饰、穿搭色彩、镜头光影 |
| 双分数模型 | 当前呈现分 vs 颜值上限分，自动算出改造空间与收益最高的三项杠杆 |
| 三档改造清单 | 0 成本立刻做 / 一周内低成本 / 长期高投入，按收益÷成本排序 |
| AI 改造预览 | 图生图提示词库，保留身份特征，强制显式 AI 标识 |
| 前后对比图 | 预览图生成后自动拼接原图 + 预览图，带双分数、箭头与 AI 声明，可直接当封面 |
| 临时数据自动清理 | 每次运行开头自动清除上次的人像图片；图片只存本地、永不提交 GitHub |
| 短视频脚本 | 3 秒钩子、口播句库、分镜、CTA、话题标签，以及发布前合规清单 |

### 快速开始

说出触发词即可，例如：

- 「帮我看看这张照片的颜值上限，并写个爆改视频脚本。」
- 「我要做一期颜值上限爆改，给我改造清单和标题。」
- 「生成这张照片的 AI 爆改预览，注意加 AI 标识。」

Agent 会自动读取本 Skill，按需加载 references，并在生成图片前询问确认（图像生成会额外消耗积分）。

### 安装

```bash
git clone https://github.com/ianqianzeyu-eng/yanzhi-baogai.git yanzhi-baogai
cp -r yanzhi-baogai ~/.workbuddy/skills/
```

Windows PowerShell：

```powershell
git clone https://github.com/ianqianzeyu-eng/yanzhi-baogai.git yanzhi-baogai
Copy-Item -Recurse yanzhi-baogai "$env:USERPROFILE\.workbuddy\skills\"
```

安装后重启会话，或直接说出触发词即可。

### 脚本工具

```bash
# 评分（输出 current / ceiling / gap / top_levers）
python scripts/score.py --input examples/sample-input.json

# 生成前后对比图（需 pip install pillow）
python scripts/make_comparison.py \
  --before 原图.jpg --after 预览图.png \
  --output generated-images/yanzhi-before-after.png \
  --current 7.4 --ceiling 8.0

# 清理临时人像图片（Skill 每次运行开头会自动执行一次）
python scripts/cleanup.py            # 删除全部
python scripts/cleanup.py --dry-run  # 只看不删
python scripts/cleanup.py --keep 1   # 保留最新一张
```

---

<a name="english"></a>

## English

A cross-platform skill that turns the viral *"I can see your beauty ceiling"* trend into a **reusable, explainable, and compliant** workflow: photo diagnosis → dual-score assessment → prioritized makeover plan → AI preview → before/after comparison → short-video script. Works natively on WorkBuddy / CodeBuddy / Coze / Claude (SKILL.md), and on Doubao App via a ready-to-paste bot prompt.

Inspired by a full breakdown of the Douyin creator 「微波炉（形象改造）」's visible works, combined with public research on facial aesthetics, color analysis, and photography. See [`references/creator-research.md`](references/creator-research.md) and [`references/assessment-framework.md`](references/assessment-framework.md).

> Scores are for entertainment only — not an objective evaluation or medical advice. All AI-generated content must be explicitly labeled.

### Features

| Feature | Description |
| --- | --- |
| Six-factor diagnosis | Bone structure, features & expression, skin, head & styling, outfit & color, camera & lighting |
| Dual-score model | Current look vs. beauty ceiling, with automatic gap and top-3 highest-ROI levers |
| Three-tier action plan | Do now (free) / This week (low cost) / Long term, sorted by benefit ÷ cost |
| AI makeover preview | Image-to-image prompt library, identity preserved, explicit AI labeling enforced |
| Before/after image | Auto-merges original + preview with scores, arrow, and AI notice — ready as a thumbnail |
| Auto-clean temp data | Clears last run's portraits at startup; images stay local and are never committed to GitHub |
| Short-video script | 3-second hook, speak lines, storyboard, CTA, hashtags, and a pre-publish compliance checklist |

### Quick Start

Just say a trigger phrase, for example:

- "Check the beauty ceiling of this photo and write a makeover video script."
- "I'm making a beauty-ceiling makeover — give me a plan and a title."
- "Generate an AI makeover preview of this photo, with an AI label."

The agent loads the skill and references on demand, and will ask for confirmation before generating images (image generation uses extra credits).

### Installation

```bash
git clone https://github.com/ianqianzeyu-eng/yanzhi-baogai.git yanzhi-baogai
cp -r yanzhi-baogai ~/.workbuddy/skills/
```

Windows PowerShell:

```powershell
git clone https://github.com/ianqianzeyu-eng/yanzhi-baogai.git yanzhi-baogai
Copy-Item -Recurse yanzhi-baogai "$env:USERPROFILE\.workbuddy\skills\"
```

Restart your session after installation, or just say a trigger phrase.

### Utility Scripts

```bash
# Score (outputs current / ceiling / gap / top_levers)
python scripts/score.py --input examples/sample-input.json

# Before/after image (requires pip install pillow)
python scripts/make_comparison.py \
  --before original.jpg --after preview.png \
  --output generated-images/yanzhi-before-after.png \
  --current 7.4 --ceiling 8.0

# Clean temp portraits (auto-run at each skill startup)
python scripts/cleanup.py            # delete all
python scripts/cleanup.py --dry-run  # preview only
python scripts/cleanup.py --keep 1   # keep the newest
```

---

<a name="多平台支持"></a>

## 多平台支持 / Multi-platform

同一套方法论，两种接入方式：SKILL.md 原生平台 + 豆包智能体。

| 平台 | 接入方式 | 说明 |
| --- | --- | --- |
| WorkBuddy / CodeBuddy | 安装到 `~/.workbuddy/skills/` | 完整功能，含脚本 |
| 扣子 Coze / Claude Code / Cursor 等 | 上传 `yanzhi-baogai.zip` 技能包 | 原生 SKILL.md 格式，扣子见 [指南](platforms/coze/README.md) |
| **豆包 App** | 复制智能体提示词 + 上传知识库 | 见 [豆包指南](platforms/doubao/README.md) |

### 豆包 App 快速上手
1. 豆包 → 创建 AI 智能体，名称填「颜值上限爆改师」。
2. 把 [`platforms/doubao/persona-prompt.md`](platforms/doubao/persona-prompt.md) 中 `==== 开始 ====` 到 `==== 结束 ====` 的内容复制到「设定描述」。（评分公式已内置，无需脚本）
3. 可选：把 [`platforms/doubao/knowledge-base.txt`](platforms/doubao/knowledge-base.txt) 上传到智能体知识库，回答更专业。
4. 发布后发照片 + 说「帮我看看颜值上限」即可。

> 豆包 App 不能运行本地 Python 脚本，因此评分与脚本能力以提示词形式内置；前后对比图需用图片工具自行拼接。

### Add to Doubao (English)
Create a Doubao bot, paste the persona prompt from `platforms/doubao/persona-prompt.md` into the persona field, optionally upload `knowledge-base.txt` to its knowledge base, then publish.

---

## 目录结构 / Structure

```
yanzhi-baogai/
├── SKILL.md                     # 触发条件、工作流、硬性规则 / triggers, workflow, rules
├── references/
│   ├── creator-research.md      # 抖音博主作品拆解 / creator content breakdown
│   ├── assessment-framework.md  # 六因子标准与研究局限 / six-factor standards & limits
│   ├── prompt-library.md        # 图生图提示词模板 / img2img prompt templates
│   ├── script-templates.md      # 短视频分镜与口播 / storyboard & speak lines
│   └── compliance.md            # AI 标识与伦理清单 / AI labeling & ethics
├── scripts/
│   ├── score.py                 # 确定性评分 / deterministic scoring
│   ├── make_comparison.py       # 前后对比图 / before-after image
│   └── cleanup.py               # 临时图片清理 / temp image cleanup
├── assets/report-template.md    # 诊断报告模板 / report template
├── examples/                    # 完整示例 / full examples
├── platforms/                   # 跨平台适配 / cross-platform adapters
│   ├── coze/README.md           # 扣子 Coze 技能包导入指南
│   └── doubao/
│       ├── README.md            # 豆包智能体搭建指南
│       ├── persona-prompt.md    # 可复制的豆包人设提示词（自包含公式）
│       └── knowledge-base.txt   # 豆包知识库上传文本
├── LICENSE                      # MIT
└── .gitignore
```

## 与其他 Skill 联动 / Integrations

`buddy-image-processing`（图像预处理）· ImageGen（图生图预览）· `humanizer` / `human-writing`（口播口语化）

## 合规声明 / Compliance

遵循《人工智能生成合成内容标识办法》（2025-09-01 施行）：生成内容需显式标识；处理他人肖像需获得授权；分数为娱乐向表达。详见 [`references/compliance.md`](references/compliance.md)。
Complies with China's *Measures for Labeling AI-Generated Content* (effective 2025-09-01): generated content must be explicitly labeled, portraits require consent, and scores are for entertainment only.

## License

MIT
