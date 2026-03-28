#!/usr/bin/env python3
"""
空白毕业典礼 - 节点20: 交汇
Choice.py - 选择脚本
分支: both_branches
"""

import sys

NODE_ID = "node_20"
NODE_NAME = "交汇"


def display_scene():
    print("=" * 50)
    print("【节点20】交汇")
    print("=" * 50)
    print()
    print("阳光温暖，花瓣轻柔。")
    print("小夏站在你身边，手轻轻握在你的手心里。")
    print()
    print("无论哪个结局，你们都站在这里。")
    print("过去的一切——甜蜜的、痛苦的、真实的、虚幻的——")
    print("都沉淀在这里。")
    print()
    print("你会怎么做？")
    print()


def get_choices():
    return {
        1: {"text": "继续往前走", "target": "node_23"},
        2: {"text": "回头看看", "target": "node_21"},
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
        choice = int(input("请输入你的选择 (1-2): "))
        result = handle_choice(choice)
        if result:
            print(f"\n下一步将在 {result} 继续...")
    except ValueError:
        print("请输入有效的数字。")


if __name__ == "__main__":
    main()
