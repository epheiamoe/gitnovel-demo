#!/usr/bin/env python3
"""
空白毕业典礼 - 节点18: BE: 醒来
Choice.py - 选择脚本
分支: branch_be
"""

import sys

NODE_ID = "node_18"
NODE_NAME = "BE: 醒来"


def display_scene():
    print("=" * 50)
    print("【节点18】BE: 醒来")
    print("=" * 50)
    print()
    print("白色的病房，白色的天花板。")
    print("窗外的雨声淅淅沥沥。")
    print("医生刚刚离开，留下你一个人。")
    print()
    print("手中的文件上写着——")
    print("'创伤记忆已成功封印'")
    print()
    print("你会怎么做？")
    print()


def get_choices():
    return {
        1: {"text": "那些记忆...是真的吗？", "target": "node_21"},
        2: {"text": "小夏呢？", "target": "node_21"},
        3: {"text": "我想一个人待会儿", "target": "node_21"},
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
