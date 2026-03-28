#!/usr/bin/env python3
"""
空白毕业典礼 - 节点24: Meta: 署名
Choice.py - 选择脚本
分支: both_branches
"""

import sys

NODE_ID = "node_24"
NODE_NAME = "Meta: 署名"


def display_scene():
    print("=" * 50)
    print("【节点24】Meta: 署名")
    print("=" * 50)
    print()
    print("屏幕的光芒照在你脸上。")
    print("你的名字就在文档的第一行。")
    print("小夏站在门口，购物袋垂在身侧，看着你。")
    print()
    print("'你在看什么？'她问。")
    print()
    print("你会怎么做？")
    print()


def get_choices():
    return {
        1: {"text": "继续往下看", "target": "node_25"},
        2: {"text": "关掉这个文件", "target": "node_25"},
        3: {"text": "去找小夏问清楚", "target": "node_25"},
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
