#!/usr/bin/env python3
"""
空白毕业典礼 - 节点19: Sweet: 握住的手
Choice.py - 选择脚本
分支: branch_sweet
"""

import sys

NODE_ID = "node_19"
NODE_NAME = "Sweet: 握住的手"


def display_scene():
    print("=" * 50)
    print("【节点19】Sweet: 握住的手")
    print("=" * 50)
    print()
    print("樱花在风中飞舞。")
    print("小夏靠在你肩上，眼泪还挂在睫毛上，却在微笑。")
    print("你们的手交握在一起，谁都没有说话。")
    print()
    print("夕阳把一切都染成了金色。")
    print()
    print("你会怎么做？")
    print()


def get_choices():
    return {
        1: {"text": "抱紧她", "target": "node_20"},
        2: {"text": "我们回家吧", "target": "node_20"},
        3: {"text": "（沉默，只是握紧了手）", "target": "node_20"},
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
