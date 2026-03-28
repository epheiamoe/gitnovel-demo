#!/usr/bin/env python3
"""
Choice.py - 节点10: 暴雨之日
当前节点ID: node_10
分支: branch_memory (记忆分支)
"""

import sys


def display_choice():
    print("\n" + "=" * 50)
    print("【节点10】暴雨之日")
    print("【记忆分支】")
    print("=" * 50)
    print()
    print("*——记忆闪回中——*")
    print()
    print("画面正在崩塌。")
    print("雨中的场景越来越模糊，你听到了碎裂的声音。")
    print("但你不想就这样放弃……")
    print()
    print("你要怎么做？")
    print()
    print("  1. 试着继续回忆")
    print("  2. 抓住那个画面不放")
    print("  3. 回到现实")
    print()
    print("=" * 50)


def main():
    display_choice()

    while True:
        try:
            choice = input("请输入选项数字 (1-3): ").strip()

            if choice == "1":
                print("\n[你拼命想要抓住那段记忆...]")
                print("[系统将切换到节点: node_11]")
                return "node_11"
            elif choice == "2":
                print("\n[你紧紧抓住那个画面...]")
                print("[系统将保持在节点: node_10 (深入记忆)]")
                return "node_10_deep"
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
