#!/usr/bin/env python3
"""
Choice.py - 节点14: 碎片拼凑
当前节点ID: node_14
分支: main
"""

import sys


def display_choice():
    print("\n" + "=" * 50)
    print("【节点14】碎片拼凑")
    print("=" * 50)
    print()
    print("你握着小夏递过来的文件夹。")
    print("'梦境协议'——这四个字让你的心跳加速。")
    print("小夏站在你面前，等待着你的反应。")
    print()
    print("你要怎么做？")
    print()
    print("  1. 告诉小夏你记起来的事")
    print("  2. 问小夏到底发生了什么")
    print("  3. 继续听她说什么")
    print()
    print("=" * 50)


def main():
    display_choice()

    while True:
        try:
            choice = input("请输入选项数字 (1-3): ").strip()

            if choice == "1":
                print("\n[你开始讲述自己恢复的记忆...]")
                print("[系统将切换到节点: node_14_share]")
                return "node_14_share"
            elif choice == "2":
                print("\n[你直接询问她发生了什么...]")
                print("[系统将切换到节点: node_15]")
                return "node_15"
            elif choice == "3":
                print("\n[你沉默地等待她继续说下去...]")
                print("[系统将切换到节点: node_15]")
                return "node_15"
            else:
                print("无效选项，请输入 1、2 或 3")
        except EOFError:
            print("\n\n[已退出选择]")
            sys.exit(0)


if __name__ == "__main__":
    result = main()
    print(f"\n>>> 前往: {result}")
