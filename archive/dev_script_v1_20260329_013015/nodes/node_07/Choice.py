#!/usr/bin/env python3
"""
空白毕业典礼 - 节点7: 社团活动室
Choice.py - 选择脚本
"""

import sys

NODE_ID = "node_07"
NODE_NAME = "社团活动室"


def display_scene():
    print("=" * 50)
    print("【节点7】社团活动室")
    print("=" * 50)
    print()
    print("那张跨年夜的合影里，她的眼神装满了星星。")
    print("而你低头看着她，温柔得像是在看整个世界。")
    print()
    print("但那些温柔的记忆，为什么会被封印？")
    print()
    print("你会怎么做？")
    print()


def get_choices():
    return {
        1: {"text": "仔细看看这张照片，寻找更多细节", "target": "node_07"},
        2: {"text": "翻翻桌上的文件", "target": "node_08"},
        3: {"text": "看看墙上还有什么", "target": "node_08"},
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
