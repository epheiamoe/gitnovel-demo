#!/usr/bin/env python3
"""
Choice.py - 节点11: 被遗忘的约定
当前节点ID: node_11
分支: branch_memory (记忆分支)
"""

import sys


def display_choice():
    print("\n" + "=" * 50)
    print("【节点11】被遗忘的约定")
    print("【记忆分支】")
    print("=" * 50)
    print()
    print("*——记忆闪回中——*")
    print()
    print("夕阳、天台、纸条上的字……")
    print("约定的声音还在耳边回响：'永远在一起'")
    print("但画面正在崩解，你必须做出选择。")
    print()
    print("你要怎么做？")
    print()
    print("  1. 继续回忆那个约定")
    print("  2. 回忆那之后的场景")
    print("  3. 回到现实")
    print()
    print("=" * 50)


def main():
    display_choice()

    while True:
        try:
            choice = input("请输入选项数字 (1-3): ").strip()

            if choice == "1":
                print("\n[你试图抓住约定的更多细节...]")
                print("[系统将切换到节点: node_11_deep]")
                return "node_11_deep"
            elif choice == "2":
                print("\n[你试图回忆之后发生的事情...]")
                print("[系统将切换到节点: node_12]")
                return "node_12"
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
