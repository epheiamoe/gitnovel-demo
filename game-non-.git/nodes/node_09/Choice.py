#!/usr/bin/env python3
"""
Choice.py - 节点9: 樱花树下
当前节点ID: node_09
分支: main
"""

import sys


def display_choice():
    print("\n" + "=" * 50)
    print("【节点9】樱花树下")
    print("=" * 50)
    print()
    print("你站在樱花树下，眼前是刻着字的石碑。")
    print("花瓣不断飘落，落在你的肩头、发间。")
    print("你想起了什么，却又什么都抓不住。")
    print()
    print("你要怎么做？")
    print()
    print("  1. 去树后面的亭子看看")
    print("  2. 继续在湖边走走")
    print("  3. 回到礼堂找小夏")
    print()
    print("=" * 50)


def main():
    display_choice()

    while True:
        try:
            choice = input("请输入选项数字 (1-3): ").strip()

            if choice == "1":
                print("\n[你走向树后面的亭子...]")
                print("[系统将切换到节点: node_09_亭子 或后续节点]")
                return "node_09_亭子"
            elif choice == "2":
                print("\n[你沿着湖边继续漫步...]")
                print("[系统将切换到节点: node_09_湖边 或后续节点]")
                return "node_09_湖边"
            elif choice == "3":
                print("\n[你决定回到礼堂...]")
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
