# 技术架构

## 概述

游戏使用 **Git 作为时空引擎**，每个故事节点存储为一个 Git commit，分支代表不同故事线。

## Git 时空引擎

### 核心原理

| Git 概念 | 游戏对应 |
|----------|----------|
| commit | 一个故事节点 |
| branch | 一条故事线 |
| tag | 节点的唯一标识 |
| git checkout | 时空跳转 |

### 工作方式

1. **节点存储**: 每个节点的内容（Scene.md, Story.md 等）直接存入 Git commit
2. **分支切换**: 不同故事线使用不同 branch
3. **节点跳转**: 通过 `git checkout <tag>` 读取特定节点
4. **状态持久化**: .state.json 记录当前节点和分支

### 分支结构

```
main ──────────────────────────── node_01 → node_02 → ... → node_16
  │                                    (分叉点)
  ├── branch_memory ── node_10 → node_11 → node_12 → node_13
  │
  ├── branch_be ────── node_17_be → node_18 → ... → node_25 (END)
  │
  └── branch_sweet ─── node_17_sweet → node_19 → ... → node_25 (END)
```

## Choice.py 引擎

### 核心函数

| 函数 | 功能 |
|------|------|
| `load_state()` | 从 .state.json 加载游戏状态 |
| `save_state()` | 保存游戏状态到 .state.json |
| `git_show(ref, file)` | 从 Git tag 读取文件内容 |
| `git_checkout(ref)` | 切换到指定 commit/branch |
| `load_current_node()` | 加载当前节点数据 |
| `display_node()` | 显示场景和故事 |
| `handle_choice()` | 处理玩家选择 |

### 数据流

```
玩家选择 → handle_choice() → 更新 state
                              ↓
                         git_checkout() → 切换分支/节点
                              ↓
                         save_state() → 写入 .state.json
```

## .state.json 状态文件

```json
{
  "current_node": "node_19",
  "current_branch": "branch_sweet",
  "history": ["node_02", "node_04", "node_19"],
  "visited_nodes": ["node_02", "node_04", "node_19"]
}
```

| 字段 | 描述 |
|------|------|
| current_node | 当前所在节点 ID |
| current_branch | 当前所在分支 |
| history | 节点访问历史 |
| visited_nodes | 已访问的节点列表 |

## 文件格式

### Scene.md
场景描写，包括地点、环境、可见物品等。

### Story.md
故事叙述内容，描述当前发生的事情。

### Note.md
线索笔记，记录玩家发现的线索和待解之谜。

### choices.json
选项列表，格式：
```json
[
  {"text": "去104教室看看", "target": "node_02"},
  {"text": "留在原地", "target": "node_01"}
]
```

## 跨平台支持

Choice.py 自动处理 Windows 控制台编码：
```python
if sys.platform == 'win32':
    import io
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')
    sys.stdin = io.TextIOWrapper(sys.stdin.buffer, encoding='utf-8', errors='replace')
```
