# Git 驱动的互动小说（demo）

**这只是一个测试的简单demo，用来测试这个概念的可行性，它其实几乎没有什么可玩性。而且它是用AI开发的。**

**这是个demo！非常不完善（但应该可以正常玩）。只是验证想法，故事也是AI写的。**

TODO：让Choice.py实现得更优雅一点

## 游玩条件

- Git

- Python

- Markdown 阅读器（推荐Marktext）

## 游玩方法

[下载releases中的文件](https://github.com/epheiamoe/gitnovel-demo/releases)

解压

> 因为显然git仓库里面不能嵌套git仓库，但游戏本身又是一个特殊git仓库，所以只能这样了。您可以在`dev_script/nodes`看到一模一样的完整的原始脚本，`game`文件夹只是把它们用git组合了起来。如果您希望在线查看`game`仓库的效果，`game-non-.git`目录是移除了.git的版本，它显然无法游玩，只有开始部分的内容。

文件资源管理器进入`game`目录，

终端：

```bash
cd game
```

使用Markdown 阅读器打开下面几个文件：

- Scene.md

- Story.md

- Note.md

为了游戏体验，请不要查看Choice.py！

使用Markdown 阅读器阅读上面的文件。

在终端执行

```bash
python Choice.py
```

做出命运的选择吧~

输入你选择的编号，会自动通过git 切换到对应文件夹。

刷新你的Markdown 阅读器阅读新的文本内容。

## 其他说明

`dev_script`目录是原始故事脚本

## 许可证

CC0，随便拿去用吧
