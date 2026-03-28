# 目录结构

```
demo/
├── AGENTS.md          # 开发文档（供 AI 使用）
├── README.md          # 项目说明
├── build.py           # 构建脚本
│
├── game/              # 最终可运行的游戏目录
│   ├── Choice.py      # 游戏引擎
│   ├── .state.json    # 游戏状态
│   ├── Scene.md       # 当前场景内容
│   ├── Story.md       # 当前故事内容
│   ├── Note.md        # 当前线索笔记
│   ├── choices.json   # 当前选择选项
│   └── .git/          # Git 时空引擎
│
├── story/             # 开发目录（作者编辑）
│   ├── build.py       # 构建脚本
│   ├── migrate.py     # 数据迁移脚本
│   ├── main/          # 主线剧情
│   │   ├── node_01.yaml
│   │   └── ...
│   ├── branch_memory/ # 记忆闪回分支
│   ├── branch_be/     # BE 结局分支
│   └── branch_sweet/  # Sweet 结局分支
│
├── archive/           # 备份目录
│   ├── game_v1_file_copy_*/
│   ├── game_v2_git_*/
│   └── game_latest_*/
│
└── release/           # 发布版本（待打包）
```

## 各目录说明

### game/ - 可运行的游戏目录

游玩时只需要此目录，包含：
- **Choice.py**: 游戏主引擎
- **.state.json**: 玩家进度状态
- **.git/**: Git 时空引擎，存储所有节点内容
- **Scene.md / Story.md / Note.md / choices.json**: 由 Git 驱动，自动加载

### story/ - 开发目录

供作者编写故事的目录，包含：
- 各分支的 `.yaml` 故事文件
- `build.py` 构建脚本

### archive/ - 备份目录

历史版本备份，按时间戳命名。

### release/ - 发布版本

待打包的发布版本目录。
