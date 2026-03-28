#!/usr/bin/env python3
"""
空白毕业典礼 - 节点21: BE: 空白之后
Choice.py - 选择脚本
分支: branch_be
"""

import sys

NODE_ID = "node_21"
NODE_NAME = "BE: 空白之后"


def display_scene():
    print("=" * 50)
    print("【节点21】BE: 空白之后")
    print("=" * 50)
    print()
    print("手机屏幕亮着。")
    print("照片里的两个人笑着，像是在嘲笑你的健忘。")
    print()
    print("你盯着那个笑容，试图想起什么。")
    print("但什么都想不起来。")
    print()
    print("你会怎么做？")
    print()


def get_choices():
    return {
        1: {"text": "试着搜索那个名字", "target": "node_22"},
        2: {"text": "把照片删掉", "target": "node_22"},
        3: {"text": "就这样活着吧", "target": "node_22"},
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
