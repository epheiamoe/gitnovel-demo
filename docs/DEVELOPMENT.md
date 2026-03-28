# 开发指南

## 工作流程

```
1. 编辑 story/ 下的 yaml 文件
2. 运行构建脚本生成游戏
3. 测试游戏
```

## 编写新故事

每个节点是一个 `.yaml` 文件，放在对应分支目录下。

### YAML 文件格式

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
    target: node_01           # 循环到自身
  - text: 随便走走
    target: main:node_03      # 显式指定分支

note: |
  ## 线索笔记
  ...
```

### 字段说明

| 字段 | 描述 |
|------|------|
| node_id | 节点唯一标识 |
| scene | 场景描写（Markdown 格式） |
| story | 故事叙述内容 |
| choices | 选项列表 |
| choices[].text | 选项显示文字 |
| choices[].target | 跳转目标 |

### 跳转格式

- 同分支跳转: `target: node_02`
- 跨分支跳转: `target: branch_sweet:node_25`
- 结束游戏: `target: END`

## 构建游戏

```bash
cd story
python build.py
```

构建过程：
1. 初始化 game/ 目录
2. 创建 Git 仓库
3. 按分支依次创建 commits
4. 为每个节点创建 git tag
5. 生成 Choice.py 和 .state.json

## 测试游戏

```bash
cd game
python Choice.py
```

### 命令行选项

```bash
# 交互式选择（默认）
python Choice.py

# 指定选择序号
python Choice.py --choice 1

# 查看当前状态
python Choice.py --status

# 跳转到指定节点
python Choice.py --goto branch_sweet:node_25
```

## 分支结构

故事包含 4 个分支：

| 分支 | 节点 | 描述 |
|------|------|------|
| main | node_01-09, 14-16 | 主线剧情 |
| branch_memory | node_10-13 | 记忆闪回 |
| branch_be | node_17_be, 18, 21, 22, 24, 25 | BE 结局 |
| branch_sweet | node_17_sweet, 19, 20, 23, 24, 25 | Sweet 结局 |

## 注意事项

- 游玩时只需 `game/` 目录
- `story/` 仅供开发参考
- 所有节点内容存储在 Git commit 中
- 分支切换使用 `git checkout <branch>`
- 节点跳转使用 `git checkout <tag>`
