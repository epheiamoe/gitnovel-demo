#!/usr/bin/env python3
"""
空白毕业典礼 - 节点6: 图书馆角落
Choice.py - 选择脚本
"""

import sys

NODE_ID = "node_06"
NODE_NAME = "图书馆角落"


def display_scene():
    print("=" * 50)
    print("【节点6】图书馆角落")
    print("=" * 50)
    print()
    print("阳光照在那张旧课桌上，尘埃在光柱中缓缓飘落。")
    print("2019.09.01 —— 那是你们故事开始的日子。")
    print("而'最后一个周三'……像是被什么力量抹去了。")
    print()
    print("你会怎么做？")
    print()


def get_choices():
    return {
        1: {"text": "找找有没有其他留下的东西", "target": "node_06"},
        2: {"text": "坐下来试着回忆更多", "target": "node_07"},
        3: {"text": "继续探索图书馆", "target": "node_07"},
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
