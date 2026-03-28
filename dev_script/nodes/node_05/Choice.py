#!/usr/bin/env python3
"""
空白毕业典礼 - 节点5: 动摇的心
Choice.py - 选择脚本
"""

import sys

NODE_ID = "node_05"
NODE_NAME = "动摇的心"


def display_scene():
    print("=" * 50)
    print("【节点5】动摇的心")
    print("=" * 50)
    print()
    print("樱花瓣落在你们之间的空隙里。")
    print("她的手轻轻触碰着你的手背，温热而小心翼翼。")
    print("她说：'我会陪着你。一直。'")
    print()
    print("你会怎么做？")
    print()


def get_choices():
    return {
        1: {"text": "谢谢你...能告诉我更多吗？", "target": "node_06"},
        2: {"text": "毕业典礼...我们要做什么？", "target": "node_06"},
        3: {"text": "我想一个人静静", "target": "node_06"},
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
