#!/usr/bin/env python3
"""
Choice.py - 节点15: 真相浮现
当前节点ID: node_15
分支: main
"""

import sys


def display_choice():
    print("\n" + "=" * 50)
    print("【节点15】真相浮现")
    print("=" * 50)
    print()
    print("你握着那份文件夹，指节发白。")
    print("'是我自己选的。'")
    print("这句话像是一道深渊，横亘在你和小夏之间。")
    print()
    print("你要怎么做？")
    print()
    print("  1. 这到底是什么？！")
    print("  2. 我签过这个东西？")
    print("  3. 我不想知道真相了")
    print()
    print("=" * 50)


def main():
    display_choice()

    while True:
        try:
            choice = input("请输入选项数字 (1-3): ").strip()

            if choice == "1":
                print("\n[你追问更多细节...]")
                print("[系统将切换到节点: node_15_detail]")
                return "node_15_detail"
            elif choice == "2":
                print("\n[你接受了这个事实，试图了解更多...]")
                print("[系统将切换到节点: node_15_accept]")
                return "node_15_accept"
            elif choice == "3":
                print("\n[你把文件夹扔到一边...]")
                print("[系统将切换到节点: node_15_refuse]")
                return "node_15_refuse"
            else:
                print("无效选项，请输入 1、2 或 3")
        except EOFError:
            print("\n\n[已退出选择]")
            sys.exit(0)


if __name__ == "__main__":
    result = main()
    print(f"\n>>> 前往: {result}")
