#!/usr/bin/env python3
"""
空白毕业典礼 - 节点2: 神秘的信
Choice.py - 选择脚本
"""

import sys

NODE_ID = "node_02"
NODE_NAME = "神秘的信"


def display_scene():
    print("=" * 50)
    print("【节点2】神秘的信")
    print("=" * 50)
    print()
    print("你把信读了一遍又一遍。")
    print("'大一那年，在图书馆第一次见到你'——这句话像是某种密码，")
    print("在你空白的记忆里激起了一圈又一圈的涟漪。")
    print()
    print("你会怎么做？")
    print()


def get_choices():
    return {
        1: {"text": "小夏是谁？——尝试回忆", "target": "node_04"},
        2: {"text": "继续看信的内容——寻找更多线索", "target": "node_02"},
        3: {"text": "在教室里找找其他东西", "target": "node_03"},
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
