#!/usr/bin/env python3
"""
空白毕业典礼 - 节点25: 结束
Choice.py - 选择脚本
分支: both_branches
"""

import sys

NODE_ID = "node_25"
NODE_NAME = "结束"


def display_scene():
    print("=" * 50)
    print("【节点25】结束")
    print("=" * 50)
    print()
    print("谢谢你玩完了这个故事。")
    print()
    print("屏幕下方是你的名字。")
    print("光标在跳动，等待你的选择。")
    print()
    print("'游戏结束了吗？'")
    print("'还是……刚刚开始？'")
    print()


def get_choices():
    return {
        1: {"text": "[重新开始]", "target": "node_01"},
        2: {"text": "[结束游戏]", "target": "END"},
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
        if target == "END":
            print("=" * 50)
            print("感谢游玩《空白毕业典礼》")
            print("=" * 50)
            print()
            print("一个关于记忆、失去和重新开始的故事。")
            print()
            print("谢谢你陪我们走完这个故事。")
            print("也许，下次再见。")
            print()
        else:
            print(f"→ 返回: {target}")
            print("=" * 50)
            print()
            print("故事重新开始了。")
            print("但这一次，你知道了一切。")
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
        if result and result != "END":
            print(f"\n下一步将在 {result} 继续...")
    except ValueError:
        print("请输入有效的数字。")


if __name__ == "__main__":
    main()
