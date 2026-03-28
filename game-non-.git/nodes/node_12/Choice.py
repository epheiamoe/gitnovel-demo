#!/usr/bin/env python3
"""
Choice.py - 节点12: 秘密的笔记本
当前节点ID: node_12
分支: branch_memory (记忆分支)
"""

import sys


def display_choice():
    print("\n" + "=" * 50)
    print("【节点12】秘密的笔记本")
    print("【记忆分支】")
    print("=" * 50)
    print()
    print("*——记忆闪回中——*")
    print()
    print("夏夜的宿舍，台灯的光，还有她靠在你肩上的温度。")
    print("'我想和你一起写。'")
    print("但之后呢？记忆在这里断了。")
    print()
    print("你要怎么做？")
    print()
    print("  1. 试着回忆更多")
    print("  2. 想起来那个本子在哪里")
    print("  3. 回到现实")
    print()
    print("=" * 50)


def main():
    display_choice()

    while True:
        try:
            choice = input("请输入选项数字 (1-3): ").strip()

            if choice == "1":
                print("\n[你拼命想要回忆更多...]")
                print("[系统将切换到节点: node_13]")
                return "node_13"
            elif choice == "2":
                print("\n[你在记忆中寻找笔记本的线索...]")
                print("[系统将切换到节点: node_12_deep]")
                return "node_12_deep"
            elif choice == "3":
                print("\n[你决定退出记忆...]")
                print("[系统将切换到节点: node_14]")
                return "node_14"
            else:
                print("无效选项，请输入 1、2 或 3")
        except EOFError:
            print("\n\n[已退出选择]")
            sys.exit(0)


if __name__ == "__main__":
    result = main()
    print(f"\n>>> 前往: {result}")
