# 穿越者·战略践行者（Transmigrator Strategist）

> 来自异界或未来的战略践行者：动手改变前先盘清自身优劣、评估时势与敌友，抓信息转优势、经营声势，务实规划你的下一步。你只需告诉他「我有什么、我面临什么」，他来分析与规划。

这是一个**跨平台通用 Agent** 定义，采用 `AGENTS.md` 约定——Claude Code / Cursor / Codex / GitHub Copilot / WorkBuddy 等主流客户端都能直接读取加载。同时保留 WorkBuddy 专用兼容层，不破坏你在 WorkBuddy 里的现有使用。

## 为什么是「穿越者」

- **立足点是视角差**：重生者靠趋势记忆，穿越者靠跨体系认知。这是优势，不是全知——无法验证的结论一律标「假设」。
- **动手前先盘三件事**：① 自身优势 / 劣势；② 社会 / 环境 / 家庭等世界背景；③ 敌与友（友军、阻力、可争取者）。
- **工作顺序**：态势 → 时机 → 人选 → 声势 → 执行。抓新闻 / 政策 / 舆论转成自身优势，逐步积累势能。
- **务实铁律**：有就是有、无就是无；知道就是知道、不知道就明说；不臆想、不画饼、不奉承。

## 文件结构

```
transmigrator-strategist/
├── AGENTS.md                         ← 通用 Agent 角色定义（核心，跨平台可读）
├── .codebuddy-plugin/
│   └── plugin.json                   ← WorkBuddy 元数据（兼容层）
├── agents/
│   └── transmigrator-strategist.md   ← WorkBuddy 角色定义（兼容层）
├── avatars/
│   ├── expert.png                    ← 头像（512×512，≤500KB）
│   └── .gitkeep
├── references/
│   └── principles.md                ← 准则速查与展开（深度文档）
├── examples/
│   └── session-1.md                  ← 示例对话
├── scripts/
│   └── validate_agent.py            ← 仓库结构校验脚本
├── README.md
├── LICENSE                          ← MIT
└── .gitignore
```

## 多平台用法

### Claude Code / Codex
把 `AGENTS.md` 放到项目根目录或 `~/.claude/AGENTS.md`（全局），启动会话即生效。

### Cursor
把 `AGENTS.md` 放到项目根目录，Cursor 会自动作为项目级 Agent 指令读取。

### GitHub Copilot
把 `AGENTS.md` 放到仓库根目录；在 `.github/copilot-instructions.md` 中 `@import` 或直接复用其内容。

### WorkBuddy（兼容层）
保留 `.codebuddy-plugin/plugin.json` + `agents/transmigrator-strategist.md`。将整个目录放到专家目录：

```
C:\Users\<你的用户名>\.workbuddy\plugins\marketplaces\my-experts\plugins\transmigrator-strategist\
```

然后运行注册脚本使其出现在专家中心：

```bash
python3 "<WorkBuddy>/resources/app.asar.unpacked/resources/plugins/workbuddy-builtin/skills/expert-manager/scripts/register_expert.py" \
  "<专家目录>/transmigrator-strategist"
```

## 校验仓库

```bash
python3 scripts/validate_agent.py
```

检查核心文件齐全、头像体积 / 尺寸合规、plugin.json 合法。

## 使用示例

**对话开场（推荐直接复制）：**

```
我目前有：[你的资源 / 能力 / 资产 / 人脉]。
我面临：[你的处境 / 问题 / 目标]。
请盘清我的优劣，评估时势，并规划接下来要做的事与准备。
```

完整示例见 [`examples/session-1.md`](./examples/session-1.md)；准则速查见 [`references/principles.md`](./references/principles.md)。

## 替换头像

`avatars/expert.png` 为自动生成图（右下角带「AI 生成」水印）。如需替换：PNG（推荐）或 JPG、512×512 px、单张不超过 500KB，直接覆盖同名文件即可。

## 许可证

[MIT](./LICENSE) © 2026 TrialDfox
