#!/usr/bin/env python3
"""
空白毕业典礼 - 节点1: 空白早晨
Choice.py - 选择脚本
"""

import sys

NODE_ID = "node_01"
NODE_NAME = "空白早晨"


def display_scene():
    print("=" * 50)
    print("【节点1】空白早晨")
    print("=" * 50)
    print()
    print("你缓缓站起身，手里紧握着那张皱巴巴的纸条。")
    print("周围的人声和音乐声交织在一起，但你的心里只想着那张纸条上的字——")
    print("'去礼堂前，先去104教室看看。'")
    print()
    print("你会怎么做？")
    print()


def get_choices():
    return {
        1: {"text": "去104教室看看", "target": "node_02"},
        2: {"text": "就在这里等一会儿", "target": "node_01"},
        3: {"text": "随便走走", "target": "node_03"},
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
