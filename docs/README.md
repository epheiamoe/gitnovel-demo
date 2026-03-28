# 空白毕业典礼 (Blank Graduation)

基于文件系统的交互式叙事游戏。

## 项目简介

- **项目名称**: 空白毕业典礼 (Blank Graduation)
- **项目类型**: 交互式叙事游戏 (Interactive Fiction)
- **核心机制**: 文件系统 + Git 分支作为时空逻辑
- **一句话描述**: 玩家通过探索文件夹层级、阅读 Markdown 文件、做选择，体验一个"失忆毕业典礼"的百合故事

## 快速开始

```bash
# 进入游戏目录
cd game

# 启动游戏（交互式）
python Choice.py

# 命令行模式选择
python Choice.py --choice 1

# 查看当前状态
python Choice.py --status

# 跳转至指定节点
python Choice.py --goto branch_sweet:node_25
```

## 故事分支

| 分支 | 描述 |
|------|------|
| main | 主线剧情 (node_01-09, 14-16) |
| branch_memory | 记忆闪回 (node_10-13) |
| branch_be | BE 结局线 |
| branch_sweet | Sweet 结局线 |

## 开发

如需开发新故事，参考 [DEVELOPMENT.md](DEVELOPMENT.md)。

## 技术架构

参考 [TECHNICAL.md](TECHNICAL.md)。
