#!/usr/bin/env python3
"""
空白毕业典礼 - 节点3: 教室走廊
Choice.py - 选择脚本
"""

import sys

NODE_ID = "node_03"
NODE_NAME = "教室走廊"


def display_scene():
    print("=" * 50)
    print("【节点3】教室走廊")
    print("=" * 50)
    print()
    print("你站在那张照片前，心跳还没有平复。")
    print("那个一闪而过的画面——白色的墙壁、消毒水的气味——")
    print("像是一根刺，扎在你记忆的空白处。")
    print()
    print("你会怎么做？")
    print()


def get_choices():
    return {
        1: {"text": "仔细看看照片里的两个人", "target": "node_03"},
        2: {"text": "继续往礼堂方向走，去找小夏", "target": "node_04"},
        3: {"text": "找找其他照片", "target": "node_03"},
    }


def show_choices():
    choices = get_choices()
    for num, choice in choices.items():
        print(f"  [{num}] {choice['text']}")


def handle_choice(choice_num):
    choices = get_choices()
    if choice_num in choices:
        target = choices[choice_num]["target"]
        print()
        print(f"→ 前往: {target}")
        print("=" * 50)
        return target
    else:
        print("无效的选择。")
        return None


def main():
    display_scene()
    show_choices()
    print()

    try:
        choice = int(input("请输入你的选择 (1-3): "))
        result = handle_choice(choice)
        if result:
            print(f"\n下一步将在 {result} 继续...")
    except ValueError:
        print("请输入有效的数字。")


if __name__ == "__main__":
    main()
