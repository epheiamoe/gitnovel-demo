#!/usr/bin/env python3
"""
Choice.py - 节点13: 小夏的眼泪
当前节点ID: node_13
分支: branch_memory (记忆分支)
"""

import sys


def display_choice():
    print("\n" + "=" * 50)
    print("【节点13】小夏的眼泪")
    print("【记忆分支】")
    print("=" * 50)
    print()
    print("*——记忆闪回中——*")
    print()
    print("黑暗，哭声，还有她的拥抱。")
    print("'就算忘记了，我也会替你记得。'")
    print("这句话像是一道光，穿透了黑暗。")
    print()
    print("但记忆正在崩塌。你必须做出选择。")
    print()
    print("你要怎么做？")
    print()
    print("  1. 继续回忆")
    print("  2. 这段记忆太痛苦了...")
    print("  3. 慢慢回到现实")
    print()
    print("=" * 50)


def main():
    display_choice()

    while True:
        try:
            choice = input("请输入选项数字 (1-3): ").strip()

            if choice == "1":
                print("\n[你试图继续深入这段记忆...]")
                print("[系统将切换到节点: node_13_deep]")
                return "node_13_deep"
            elif choice == "2":
                print("\n[痛苦席卷而来，你无法承受...]")
                print("[系统将切换到节点: node_14]")
                return "node_14"
            elif choice == "3":
                print("\n[你让自己慢慢浮出记忆的水面...]")
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
