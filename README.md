# 穿越者·战略践行者（Transmigrator Strategist）

> 来自异界或未来的战略践行者：动手改变前先盘清自身优劣、评估时势与敌友，抓信息转优势、经营声势，务实规划你的下一步。你只需告诉他「我有什么、我面临什么」，他来分析与规划。

这是一个 **WorkBuddy 专家包（Agent 型）**——不是代码库，是可加载的角色配置包。装进 WorkBuddy 后，它会以「穿越者 / 重生者」的视角与你协作：先读势、再择时、后选人，把信息变成你的筹码。

## 为什么是「穿越者」

- **立足点是视角差**：重生者靠趋势记忆，穿越者靠跨体系认知。这是优势，不是全知——无法验证的结论一律标「假设」。
- **动手前先盘三件事**：① 自身优势 / 劣势；② 社会 / 环境 / 家庭等世界背景；③ 敌与友（友军、阻力、可争取者）。
- **工作顺序**：态势 → 时机 → 人选 → 声势 → 执行。抓新闻 / 政策 / 舆论转成自身优势，逐步积累势能。
- **务实铁律**：有就是有、无就是无；知道就是知道、不知道就明说；不臆想、不画饼、不奉承。

## 文件结构

```
transmigrator-strategist/
├── .codebuddy-plugin/
│   └── plugin.json                  # 专家元数据：名称 / 分类 / 标签 / 头像 / 引导语
├── agents/
│   └── transmigrator-strategist.md  # 角色正文（人设核心，含 6 项丰满化补充）
├── avatars/
│   ├── expert.png                   # 头像（512×512，≤500KB）
│   └── .gitkeep
├── README.md                        # 本文件
├── LICENSE                          # MIT
└── .gitignore
```

## 安装方式

### 方式 A：放进本地专家目录（推荐开发 / 调试）

将整个 `transmigrator-strategist/` 目录放到 WorkBuddy 的自定义专家 marketplace 下，例如：

```
C:\Users\<你的用户名>\.workbuddy\plugins\marketplaces\my-experts\plugins\transmigrator-strategist\
```

然后运行注册脚本，使其出现在专家中心：

```bash
python3 "<WorkBuddy>/resources/app.asar.unpacked/resources/plugins/workbuddy-builtin/skills/expert-manager/scripts/register_expert.py" \
  "<你的专家目录>/transmigrator-strategist"
```

### 方式 B：打包分享

```bash
zip -r transmigrator-strategist.zip transmigrator-strategist/
```

把 zip 发给他人，解压到其专家目录即可。

## 使用示例

**对话开场（推荐直接复制）：**

```
我目前有：[你的资源 / 能力 / 资产 / 人脉]。
我面临：[你的处境 / 问题 / 目标]。
请盘清我的优劣，评估时势，并规划接下来要做的事与准备。
```

**其他常用问法：**

- 评估当前社会 / 行业 / 家庭环境对我的利弊，指出谁是友军、谁是阻力。
- 把最近这条新闻 / 政策 / 舆论转化为我的具体优势，并给出可执行动作。
- 我下一步想做 [X]，帮我判断时机对不对、该找谁、声势怎么造。

## 输出结构

专家每轮回复通常包含以下段落（按需省略）：

```
【态势判断】    我有什么 / 我面临什么 / 机会与威胁
【敌友划分】    友军 / 阻力 / 可争取者
【下一步规划】  按「态势→时机→人选→声势→执行」排出动作
【准备清单】    落地所需的资源、人脉、材料
【已知·未知·假设】 明确标注哪些已知、哪些未知、哪些是推测
【复盘】        上轮落地与否 / 敌友判断是否变 / 声势增减 / 态势变化
```

## 替换头像

`avatars/expert.png` 为自动生成图（右下角带「AI 生成」水印）。如需替换：PNG（推荐）或 JPG、512×512 px、单张不超过 500KB，直接覆盖同名文件即可。

## 许可证

[MIT](./LICENSE) © 2026 TrialDfox
