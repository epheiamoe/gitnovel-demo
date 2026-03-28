#!/usr/bin/env python3
"""
空白毕业典礼 - 节点8: 宿舍夜晚
Choice.py - 选择脚本
"""

import sys

NODE_ID = "node_08"
NODE_NAME = "宿舍夜晚"


def display_scene():
    print("=" * 50)
    print("【节点8】宿舍夜晚")
    print("=" * 50)
    print()
    print("那张照片里，两个小孩子笑得像是整个世界都属于他们。")
    print("'和小夏的第十年'——十年，从青梅竹马到恋人。")
    print("而现在，你连她是谁都不记得了。")
    print()
    print("但那本锁着的日记本里……也许藏着所有的答案。")
    print()
    print("你会怎么做？")
    print()


def get_choices():
    return {
        1: {"text": "想办法打开日记本", "target": "node_09"},
        2: {"text": "仔细看这张照片", "target": "node_08"},
        3: {"text": "在房间里找找其他线索", "target": "node_09"},
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
