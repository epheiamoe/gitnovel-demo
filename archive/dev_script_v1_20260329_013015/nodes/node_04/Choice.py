#!/usr/bin/env python3
"""
空白毕业典礼 - 节点4: 小夏的出现
Choice.py - 选择脚本
"""

import sys

NODE_ID = "node_04"
NODE_NAME = "小夏的出现"


def display_scene():
    print("=" * 50)
    print("【节点4】小夏的出现")
    print("=" * 50)
    print()
    print("她就站在你面前，眼眶微红，泪痕未干。")
    print("阳光落在她的肩上，照亮了她的轮廓。")
    print("她说：'不管你记不记得我……我都会在这里等你。'")
    print()
    print("你会怎么做？")
    print()


def get_choices():
    return {
        1: {"text": "你是谁？", "target": "node_04"},
        2: {"text": "我们……认识吗？", "target": "node_04"},
        3: {"text": "（沉默地看着她）", "target": "node_05"},
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
