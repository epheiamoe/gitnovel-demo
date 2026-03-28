#!/usr/bin/env python3
"""
空白毕业典礼 - 节点23: Sweet: 新的开始
Choice.py - 选择脚本
分支: branch_sweet
"""

import sys

NODE_ID = "node_23"
NODE_NAME = "Sweet: 新的开始"


def display_scene():
    print("=" * 50)
    print("【节点23】Sweet: 新的开始")
    print("=" * 50)
    print()
    print("阳光透进窗帘，咖啡香弥漫在空气里。")
    print("小夏弯着腰，额头抵着你的额头，笑得很温柔。")
    print()
    print("'今天，我们去哪里？'")
    print()
    print("你会怎么做？")
    print()


def get_choices():
    return {
        1: {"text": "去看樱花吧", "target": "node_20"},
        2: {"text": "今天就在家待着", "target": "node_24"},
        3: {"text": "我想写日记了", "target": "node_24"},
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
