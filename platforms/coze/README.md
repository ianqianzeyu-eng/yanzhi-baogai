# 在扣子 Coze 中使用 / Use in Coze

扣子（Coze，字节旗下，与豆包同生态）**原生支持 `SKILL.md` 技能包**，本仓库的标准技能文件夹可以直接导入，无需改造。

Coze natively supports the `SKILL.md` skill format — this repository's standard skill folder imports directly, no conversion needed.

---

## 导入步骤 / Steps

1. 打开 **扣子编程** [code.coze.cn](https://code.coze.cn) → 进入「**技能 (Skills)**」标签。
2. 点「**上传技能包**」，上传本仓库根目录打包的 `yanzhi-baogai.zip`（Skill + references + scripts + assets 全包含）。
   - 也可以先在 GitHub 页面点 Code → Download ZIP 下载整个仓库压缩包上传。
   - 系统会自动解析结构、检查安全性；格式不规范时扣子 AI 会协助补全。
3. 在预览区用一句话测试触发，例如「帮我看看这张照片的颜值上限」。
4. 点右上角「**部署**」，等待部署完成。
5. 在 **扣子对话** 输入框敲 `/`，从技能列表选中 `yanzhi-baogai` 即可使用。

---

## 说明 / Notes

- 技能包里的 `scripts/*.py` 可在扣子编程的代码环境中运行；`references/` 会在对话中按需加载（渐进式披露）。
- 开发、部署好的技能目前**仅支持在扣子对话中使用**，扣子编程里开发的智能体/工作流暂不能调用技能（以平台当前文档为准）。
- 若上传报「格式不规范」，把 `.zip` 解压后确认根目录第一层就有 `SKILL.md`，再重新压缩上传。

> 参考官方文档：<https://docs.coze.cn/guides_skill_overview> · <https://docs.coze.cn/guides_skill_faq>
