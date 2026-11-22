# yanzhi-baogai · 颜值上限爆改 Skill

一个可安装的 WorkBuddy / CodeBuddy 技能：把短视频里流行的「我能看到你的颜值上限」玩法，拆成**可复用、可解释、合规**的工作流——照片诊断 → 双分数评估 → 优先级改造清单 → AI 改造预览 → 短视频脚本。

灵感来自抖音博主「微波炉（形象改造）」的全部可见作品拆解，结合公开的人脸美学、色彩诊断与摄影资料整理。详见 [`references/creator-research.md`](references/creator-research.md) 与 [`references/assessment-framework.md`](references/assessment-framework.md)。

> 分数仅作娱乐向参考，不构成客观评价或医美建议。所有 AI 生成内容必须显式标识。

## 功能

- 六因子视觉诊断：骨相比例、五官表情、皮肤状态、头面修饰、穿搭色彩、镜头光影。
- 双分数模型：当前呈现分 vs 颜值上限分，自动算出改造空间与收益最高的三项杠杆。
- 三档改造清单：0 成本立刻做 / 一周内低成本 / 长期高投入。
- AI 改造预览：图生图提示词库，保留身份特征，强制显式 AI 标识。
- **前后对比图**：预览图生成后自动拼接原图 + 预览图，带双分数、箭头与 AI 声明，可直接当封面。
- **临时数据自动清理**：每次运行开头自动清除上次的人像图片；图片只存本地、永不提交 GitHub，保护隐私。
- 短视频脚本：3 秒钩子、口播句库、分镜、CTA、话题标签，以及发布前合规清单。

## 安装

### WorkBuddy / CodeBuddy（用户级）

```bash
git clone https://github.com/ianqianzeyu-eng/ianqianzeyu.git yanzhi-baogai
cp -r yanzhi-baogai ~/.workbuddy/skills/
```

Windows PowerShell：

```powershell
git clone https://github.com/ianqianzeyu-eng/ianqianzeyu.git yanzhi-baogai
Copy-Item -Recurse yanzhi-baogai "$env:USERPROFILE\.workbuddy\skills\"
```

安装后重启会话，或直接说出触发词即可。

## 用法

直接对 Agent 说：

- 「帮我看看这张照片的颜值上限，并写个爆改视频脚本。」
- 「我要做一期颜值上限爆改，给我改造清单和标题。」
- 「生成这张照片的 AI 爆改预览，注意加 AI 标识。」

Agent 会自动读取本 Skill，按需加载 references，并在生成图片前询问确认（图像生成会额外消耗积分）。

### 只用评分脚本

```bash
python scripts/score.py --input examples/sample-input.json
```

输入各维度 0-10 分，输出 current / ceiling / gap / top_levers 的 JSON。

### 手动生成前后对比图

```bash
python scripts/make_comparison.py \
  --before 原图.jpg --after 预览图.png \
  --output generated-images/yanzhi-before-after.png \
  --current 7.4 --ceiling 8.0
```

需先安装 Pillow：`pip install pillow`。输出带双分数与 AI 声明。

### 手动清理临时图片

```bash
python scripts/cleanup.py            # 删除 generated-images/ 下所有图片
python scripts/cleanup.py --dry-run  # 只看不删
python scripts/cleanup.py --keep 1   # 保留最新一张
```

Skill 每次运行开头会自动执行一次清理，无需手动调用。

## 目录结构

```
yanzhi-baogai/
├── SKILL.md                     # 触发条件、工作流、硬性规则
├── references/
│   ├── creator-research.md      # 抖音博主作品拆解与文案公式
│   ├── assessment-framework.md  # 六因子公开标准与研究局限
│   ├── prompt-library.md        # 图生图提示词模板
│   ├── script-templates.md      # 短视频分镜与口播模板
│   └── compliance.md            # AI 标识与伦理清单
├── scripts/
│   ├── score.py                 # 确定性评分脚本
│   ├── make_comparison.py       # 前后对比图生成（需 Pillow）
│   └── cleanup.py               # 临时人像图片清理
├── assets/
│   └── report-template.md       # 诊断报告模板
├── examples/
│   ├── sample-input.json
│   └── sample-output.md
├── LICENSE
└── .gitignore
```

## 与其他 Skill 的联动

- `buddy-image-processing`：原图去杂物、抠图、人像增强。
- 图像生成工具（如 ImageGen）：图生图改造预览。
- `humanizer` / `human-writing`：口播稿口语化改写。

## 合规声明

本项目遵循《人工智能生成合成内容标识办法》（2025-09-01 施行）：生成内容需带显式标识，不得删除或篡改标识；处理他人肖像需获得授权；分数为娱乐向表达，不得用于外貌羞辱或效果承诺。详见 [`references/compliance.md`](references/compliance.md)。

## License

MIT
