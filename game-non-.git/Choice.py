#!/usr/bin/env python3
"""
空白毕业典礼 - Choice.py
交互式选择引擎

用法:
    python Choice.py                      # 显示当前场景并让玩家选择
    python Choice.py --choice <N>         # 非交互式选择
    python Choice.py --status             # 显示当前状态
    python Choice.py --goto <node_id>     # 跳转到指定节点 (仅用于测试)
"""

import os
import sys
import subprocess
import shutil

GAME_ROOT = os.path.dirname(os.path.abspath(__file__))
NODES_DIR = os.path.join(GAME_ROOT, "nodes")
NOTE_FILE = os.path.join(GAME_ROOT, "Note.md")
CHOICE_ENGINE = os.path.join(GAME_ROOT, "Choice.py")

NODE_MAP = {
    "node_01": "空白早晨",
    "node_02": "神秘的信",
    "node_03": "教室走廊",
    "node_04": "小夏的出现",
    "node_05": "动摇的心",
    "node_06": "图书馆角落",
    "node_07": "社团活动室",
    "node_08": "宿舍夜晚",
    "node_09": "樱花树下",
    "node_10": "暴雨之日",
    "node_11": "被遗忘的约定",
    "node_12": "秘密的笔记本",
    "node_13": "小夏的眼泪",
    "node_14": "碎片拼凑",
    "node_15": "真相浮现",
    "node_16": "毕业典礼",
    "node_17": "最后的选择",
    "node_18": "BE: 醒来",
    "node_19": "Sweet: 握住的手",
    "node_20": "交汇",
    "node_21": "BE: 空白之后",
    "node_22": "BE: 独自一人",
    "node_23": "Sweet: 新的开始",
    "node_24": "Meta: 署名",
    "node_25": "结束",
}

CHOICES = {
    "node_01": {
        1: {"text": "去104教室看看", "target": "node_02"},
        2: {"text": "就在这里等一会儿", "target": "node_01"},
        3: {"text": "随便走走", "target": "node_03"},
    },
    "node_02": {
        1: {"text": "小夏是谁？", "target": "node_03"},
        2: {"text": "继续看信的内容", "target": "node_04"},
        3: {"text": "在教室里找找其他东西", "target": "node_05"},
    },
    "node_03": {
        1: {"text": "仔细看看照片里的两个人", "target": "node_04"},
        2: {"text": "继续往礼堂方向走", "target": "node_06"},
        3: {"text": "找找其他照片", "target": "node_05"},
    },
    "node_04": {
        1: {"text": "你是谁？", "target": "node_05"},
        2: {"text": "我们...认识吗？", "target": "node_05"},
        3: {"text": "（沉默地看着她）", "target": "node_05"},
    },
    "node_05": {
        1: {"text": "谢谢你...能告诉我我们是怎么认识的吗？", "target": "node_06"},
        2: {"text": "毕业典礼...我们要做什么？", "target": "node_06"},
        3: {"text": "我想一个人静静", "target": "node_06"},
    },
    "node_06": {
        1: {"text": "找找有没有其他留下的东西", "target": "node_07"},
        2: {"text": "坐下来试着回忆", "target": "node_07"},
        3: {"text": "继续探索图书馆", "target": "node_08"},
    },
    "node_07": {
        1: {"text": "仔细看看这张照片", "target": "node_08"},
        2: {"text": "翻翻桌上的文件", "target": "node_09"},
        3: {"text": "看看墙上还有什么", "target": "node_09"},
    },
    "node_08": {
        1: {"text": "想办法打开日记本", "target": "node_09"},
        2: {"text": "仔细看这张照片", "target": "node_09"},
        3: {"text": "在房间里找找钥匙", "target": "node_09"},
    },
    "node_09": {
        1: {"text": "去树后面的亭子看看", "target": "node_10"},
        2: {"text": "继续在湖边走走", "target": "node_14"},
        3: {"text": "回到礼堂找小夏", "target": "node_14"},
    },
    "node_10": {
        1: {"text": "试着继续回忆", "target": "node_11"},
        2: {"text": "抓住那个画面不放", "target": "node_11"},
        3: {"text": "回到现实", "target": "node_14"},
    },
    "node_11": {
        1: {"text": "继续回忆那个约定", "target": "node_12"},
        2: {"text": "回忆那之后的场景", "target": "node_12"},
        3: {"text": "回到现实", "target": "node_14"},
    },
    "node_12": {
        1: {"text": "试着回忆更多", "target": "node_13"},
        2: {"text": "想起来那个本子在哪里", "target": "node_13"},
        3: {"text": "回到现实", "target": "node_14"},
    },
    "node_13": {
        1: {"text": "继续回忆", "target": "node_14"},
        2: {"text": "这段记忆太痛苦了...", "target": "node_14"},
        3: {"text": "慢慢回到现实", "target": "node_14"},
    },
    "node_14": {
        1: {"text": "告诉小夏你记起来的事", "target": "node_15"},
        2: {"text": "问小夏到底发生了什么", "target": "node_15"},
        3: {"text": "继续听她说什么", "target": "node_15"},
    },
    "node_15": {
        1: {"text": "这到底是什么？！", "target": "node_16"},
        2: {"text": "我签过这个东西？", "target": "node_16"},
        3: {"text": "我不想知道真相了", "target": "node_16"},
    },
    "node_16": {
        1: {"text": "和小夏一起上台", "target": "node_17"},
        2: {"text": "留在座位上", "target": "node_17"},
        3: {"text": "冲上台拉住小夏的手", "target": "node_17"},
    },
    "node_17": {
        1: {"text": "告诉我真相", "target": "node_18"},
        2: {"text": "我已经累了，算了吧", "target": "node_18"},
        3: {"text": "我们重新开始吧", "target": "node_19"},
        4: {"text": "带我去看樱花", "target": "node_19"},
    },
    "node_18": {
        1: {"text": "那些记忆...是真的吗？", "target": "node_21"},
        2: {"text": "小夏呢？", "target": "node_21"},
        3: {"text": "我想一个人待会儿", "target": "node_21"},
    },
    "node_19": {
        1: {"text": "抱紧她", "target": "node_20"},
        2: {"text": "我们回家吧", "target": "node_20"},
        3: {"text": "（沉默，只是握紧了手）", "target": "node_20"},
    },
    "node_20": {
        1: {"text": "继续往前走", "target": "node_24"},
        2: {"text": "回头看看", "target": "node_24"},
    },
    "node_21": {
        1: {"text": "试着搜索那个名字", "target": "node_22"},
        2: {"text": "把照片删掉", "target": "node_22"},
        3: {"text": "就这样活着吧", "target": "node_22"},
    },
    "node_22": {
        1: {"text": "冲出门去某个地方", "target": "node_24"},
        2: {"text": "继续待在这里", "target": "node_24"},
        3: {"text": "（没有任何反应）", "target": "node_24"},
    },
    "node_23": {
        1: {"text": "去看樱花吧", "target": "node_20"},
        2: {"text": "今天就在家待着", "target": "node_20"},
        3: {"text": "我想写日记了", "target": "node_20"},
    },
    "node_24": {
        1: {"text": "继续往下看", "target": "node_25"},
        2: {"text": "关掉这个文件", "target": "node_25"},
        3: {"text": "去找小夏问清楚", "target": "node_25"},
    },
    "node_25": {
        1: {"text": "[重新开始]", "target": "node_01"},
        2: {"text": "[结束游戏]", "target": None},
    },
}

SPECIAL_NODES = {
    "node_10": {"branch": "branch_memory", "desc": "记忆碎片"},
    "node_11": {"branch": "branch_memory", "desc": "记忆碎片"},
    "node_12": {"branch": "branch_memory", "desc": "记忆碎片"},
    "node_13": {"branch": "branch_memory", "desc": "记忆碎片"},
    "node_18": {"branch": "branch_be", "desc": "BE结局线"},
    "node_21": {"branch": "branch_be", "desc": "BE结局线"},
    "node_22": {"branch": "branch_be", "desc": "BE结局线"},
    "node_19": {"branch": "branch_sweet", "desc": "Sweet结局线"},
    "node_23": {"branch": "branch_sweet", "desc": "Sweet结局线"},
}

NODE_NAME_TO_ID = {v: k for k, v in NODE_MAP.items()}


def get_current_node():
    scene_file = os.path.join(GAME_ROOT, "Scene.md")
    if not os.path.exists(scene_file):
        return "node_01"
    try:
        with open(scene_file, "r", encoding="utf-8") as f:
            first_line = f.readline().strip()
        for name, node_id in NODE_NAME_TO_ID.items():
            if name in first_line:
                return node_id
    except:
        pass
    return "node_01"


def get_git_branch():
    try:
        result = subprocess.run(
            ["git", "branch", "--show-current"],
            cwd=GAME_ROOT,
            capture_output=True,
            text=True,
            encoding="utf-8",
        )
        return result.stdout.strip()
    except:
        return "unknown"


def get_git_commit():
    try:
        result = subprocess.run(
            ["git", "rev-parse", "--short", "HEAD"],
            cwd=GAME_ROOT,
            capture_output=True,
            text=True,
            encoding="utf-8",
        )
        return result.stdout.strip()
    except:
        return "unknown"


def load_note():
    if os.path.exists(NOTE_FILE):
        try:
            with open(NOTE_FILE, "r", encoding="utf-8") as f:
                return f.read()
        except:
            pass
    return ""


def checkout_node(node_id):
    node_dir = os.path.join(NODES_DIR, node_id)
    if not os.path.exists(node_dir):
        print(f"Error: Node {node_id} not found!")
        return False

    current_note = load_note()
    choice_engine_backup = None
    if os.path.exists(CHOICE_ENGINE):
        with open(CHOICE_ENGINE, "r", encoding="utf-8") as f:
            choice_engine_backup = f.read()

    for item in os.listdir(node_dir):
        if item == "Choice.py":
            continue
        src = os.path.join(node_dir, item)
        dst = os.path.join(GAME_ROOT, item)
        if os.path.isfile(src):
            shutil.copy2(src, dst)

    if choice_engine_backup:
        with open(CHOICE_ENGINE, "w", encoding="utf-8") as f:
            f.write(choice_engine_backup)

    print(f"\nSwitched to: {NODE_MAP.get(node_id, node_id)}")
    return True


def display_status():
    current = get_current_node()
    branch = get_git_branch()
    commit = get_git_commit()

    print("=" * 50)
    print("[Game Status]")
    print("=" * 50)
    print(f"Current Node: {current} ({NODE_MAP.get(current, 'Unknown')})")
    print(f"Branch: {branch}")
    print(f"Commit: {commit}")

    special = SPECIAL_NODES.get(current)
    if special:
        print(f"Special: {special['desc']}")

    print("=" * 50)


def display_scene():
    current = get_current_node()

    print("=" * 50)
    print(f"[{current.upper()}] {NODE_MAP.get(current, 'Unknown')}")
    print("=" * 50)

    scene_file = os.path.join(GAME_ROOT, "Scene.md")
    if os.path.exists(scene_file):
        with open(scene_file, "r", encoding="utf-8") as f:
            content = f.read()
            lines = content.split("\n")
            for line in lines[:40]:
                print(line)
            if len(lines) > 40:
                print("...")


def show_choices_for_node(node_id):
    if node_id not in CHOICES:
        print("No choices for current node.")
        return []

    choices = CHOICES[node_id]
    print("\nWhat will you do?\n")
    for num, choice in choices.items():
        if choice["target"]:
            print(f"  [{num}] {choice['text']}")
        else:
            print(f"  [{num}] {choice['text']} (END)")

    return list(choices.keys())


def handle_choice(choice_num):
    current = get_current_node()
    if current in CHOICES and choice_num in CHOICES[current]:
        target = CHOICES[current][choice_num]["target"]
        if target:
            checkout_node(target)
        else:
            print("\nThanks for playing Blank Graduation!")
            print("Game Over.")
        return target
    else:
        print(f"Error: Invalid choice {choice_num}")
        return None


def main():
    args = sys.argv[1:]

    if "--status" in args:
        display_status()
        return

    if "--goto" in args:
        idx = args.index("--goto")
        if idx + 1 < len(args):
            checkout_node(args[idx + 1])
        return

    if "--choice" in args:
        idx = args.index("--choice")
        if idx + 1 < len(args):
            try:
                choice_num = int(args[idx + 1])
                handle_choice(choice_num)
            except ValueError:
                print("Error: Please provide a valid number.")
        return

    display_scene()
    current = get_current_node()
    valid_choices = show_choices_for_node(current)

    if not valid_choices:
        return

    print()
    try:
        choice = input("Enter your choice: ").strip()
        choice_num = int(choice)
        if choice_num in valid_choices:
            handle_choice(choice_num)
        else:
            print(f"Please enter a number between 1-{max(valid_choices)}.")
    except ValueError:
        print("Please enter a valid number.")
    except EOFError:
        print("\n(Interactive mode: run python Choice.py directly)")


if __name__ == "__main__":
    main()
