#!/usr/bin/env python3
"""
空白毕业典礼 - 节点17: 最后的选择
Choice.py - 选择脚本
分支: branch_be / branch_sweet
"""

import sys

NODE_ID = "node_17"
NODE_NAME = "最后的选择"


def display_scene():
    print("=" * 50)
    print("【节点17】最后的选择")
    print("=" * 50)
    print()
    print("小夏站在你面前，阳光照在她的脸上。")
    print("她的眼神里有期待，也有一丝恐惧。")
    print()
    print("'如果你想知道全部真相，我可以告诉你。'")
    print("'但那可能会很痛苦……'")
    print()
    print("她顿了顿。")
    print("'或者，我们可以重新开始。'")
    print()
    print("你会怎么做？")
    print()


def get_choices():
    return {
        1: {"text": "告诉我真相", "target": "node_18"},
        2: {"text": "我已经累了，算了吧", "target": "node_18"},
        3: {"text": "我们重新开始吧", "target": "node_19"},
        4: {"text": "带我去看樱花", "target": "node_19"},
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
        choice = int(input("请输入你的选择 (1-4): "))
        result = handle_choice(choice)
        if result:
            print(f"\n下一步将在 {result} 继续...")
    except ValueError:
        print("请输入有效的数字。")


if __name__ == "__main__":
    main()
