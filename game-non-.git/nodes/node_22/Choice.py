#!/usr/bin/env python3
"""
空白毕业典礼 - 节点22: BE: 独自一人
Choice.py - 选择脚本
分支: branch_be
"""

import sys

NODE_ID = "node_22"
NODE_NAME = "BE: 独自一人"


def display_scene():
    print("=" * 50)
    print("【节点22】BE: 独自一人")
    print("=" * 50)
    print()
    print("雨还在下。")
    print("你的眼泪已经干了，但那种空洞的感觉还在。")
    print("窗外的世界灰蒙蒙的，像是隔着一层纱。")
    print()
    print("你会怎么做？")
    print()


def get_choices():
    return {
        1: {"text": "冲出门去某个地方", "target": "node_24"},
        2: {"text": "继续待在这里", "target": "node_24"},
        3: {"text": "（没有任何反应）", "target": "node_24"},
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
