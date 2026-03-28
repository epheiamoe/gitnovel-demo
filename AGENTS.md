# 空白毕业典礼 (Blank Graduation)
## 基于文件系统的互动小说 - 开发文档

---

## 项目概述

**类型**: 交互式叙事游戏 (Interactive Fiction)
**核心机制**: 文件系统 + Git 分支作为时空逻辑
**目标**: 玩家通过探索文件夹层级、阅读 Markdown 文件、运行 Python 脚本做选择，体验一个"失忆毕业典礼"的百合故事

---

## 架构设计

### 核心概念

- **story/** = 开发目录，作者编写故事的地方（YAML + Markdown）
- **game/** = 最终可运行的游戏，无需 story/ 即可运行
- **Git** = 时空引擎，每个 commit = 一个节点
- **分支** = 不同故事线（main, branch_be, branch_sweet 等）

### 工作流程

```
1. 开发阶段：编辑 story/ 下的 YAML 文件
2. 构建阶段：python build.py → 生成 git commits
3. 游玩阶段：python Choice.py → 通过 git checkout 穿越时空
```

---

## 目录结构

```
demo/
├── AGENTS.md                 # 本文档
├── story/                    # 开发目录（作者编辑）
│   ├── main/
│   │   ├── node_01.yaml
│   │   ├── node_02.yaml
│   │   └── ...
│   ├── branch_memory/
│   ├── branch_be/
│   └── branch_sweet/
├── build.py                  # 构建脚本
└── game/                    # 最终可运行的游戏
    ├── Choice.py           # 主引擎
    ├── .state.json         # 游戏状态
    └── .git/              # Git 时空引擎
                          # (commit 内容 = 节点 Scene.md/Story.md)
```

**重要**：游玩时只需要 `game/` 目录，`story/` 只是备份/开发参考。

---

## 故事源文件格式 (YAML)

每个节点是一个 `.yaml` 文件：

```yaml
node_id: node_01
scene: |
  # 场景：空白早晨
  
  毕业典礼会场，昏暗的休息室角落...
  
story: |
  你不知道自己睡了多久...
  
choices:
  - text: 去104教室看看
    target: node_02           # 同分支跳转
  - text: 留在原地
    target: node_01           # 循环
  - text: 随便走走
    target: main:node_03      # 显式指定分支

note: |
  ## 线索笔记
  ...
```

---

## Git 时空结构

### 分支定义
```
main              # 主线剧情 (node_01-09, 14-16)
branch_memory     # 记忆闪回 (node_10-13)
branch_be         # BE结局线 (node_17_be, 18, 21, 22, 24, 25)
branch_sweet      # Sweet结局线 (node_17_sweet, 19, 20, 23, 24, 25)
```

### 跳转格式
- 同分支: `target: node_XX`
- 跨分支: `target: branch_name:node_XX`
- 结束: `target: END`

### Git 操作
- 每个节点是一个 commit
- 节点内容直接存在 git commit 里（不需要物理文件）
- 分支切换使用 `git checkout <branch>`
- 节点跳转使用 `git checkout <tag>`
- 使用 tags 标记节点 (node_01, node_02, ...)

---

## 构建流程

```bash
# 1. 编辑 story/ 目录下的 yaml 文件
# 2. 运行构建
cd demo/story
python build.py

# 3. 运行游戏（不需要 story/）
cd ../game
python Choice.py
```

---

## Choice.py 使用方法

```bash
# 交互式选择
python Choice.py

# 命令行选择
python Choice.py --choice 1

# 查看状态
python Choice.py --status

# 跳转（需要分支前缀）
python Choice.py --goto branch_sweet:node_25
```

---

## 已测试的路径

### Sweet 结局路径
```
node_01 → node_02 → node_03 → node_04 → node_05 → 
node_06 → node_07 → node_08 → node_09 → node_14 → 
node_15 → node_16 → branch_sweet:node_17_sweet → 
node_19 → node_20 → node_23 → node_20 → node_24 → node_25 → END
```

---

## 已知问题

1. [已修复] ~~migrate.py 解析不完整~~ → 部分 Choice.py 格式需要手动修复
2. [已修复] ~~--goto 不支持无分支前缀~~ → 需要使用 `branch:node` 格式
3. [设计意图] 部分节点存在循环设计：某些选项会循环到同一节点

---

## 开发进度

- [x] 创建 AGENTS.md
- [x] 设计故事脚本（25个节点）
- [x] 创建 story/ 目录结构
- [x] 编写 build.py 构建脚本
- [x] 生成 Choice.py 引擎
- [x] 构建 Git 仓库结构（每个 commit = 一个节点）
- [x] 测试 Sweet 路径可通
- [x] 测试 BE 路径可通
- [x] Choice.py 从 git commit 读取内容
- [x] game/ 目录可独立运行

---

## 备份位置

- `archive/game_v1_file_copy_20260329_013015/` - 旧版本（文件复制）
- `archive/game_v2_git_20260329_020539/` - Git驱动版本
- `archive/game_latest_*/` - 最新备份

---

*最后更新: 2026-03-29*
