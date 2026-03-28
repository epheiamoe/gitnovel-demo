#!/usr/bin/env python3
"""
Choice.py - 节点16: 毕业典礼
当前节点ID: node_16
分支: main

【重要抉择点】
此节点的选择将决定进入哪个结局分支：
- 选择1或3: 进入 Sweet GE (甜蜜结局) 分支
- 选择2: 可能进入 BE (致郁结局) 分支
"""

import sys


def display_choice():
    print("\n" + "=" * 50)
    print("【节点16】毕业典礼")
    print("=" * 50)
    print()
    print("礼堂里人声鼎沸。")
    print("小夏的背影正在远去，走向舞台边缘。")
    print("她没有回头，但她在等。")
    print()
    print("毕业证书还空着。你的名字还差一个签名。")
    print()
    print("你要怎么做？")
    print()
    print("  1. 和小夏一起上台")
    print("  2. 留在座位上")
    print("  3. 冲上台拉住小夏的手")
    print()
    print("=" * 50)
    print("【抉择提示】")
    print("  - 选择 1 或 3 将进入 Sweet GE (甜蜜结局)")
    print("  - 选择 2 将进入 BE (致郁结局)")
    print("=" * 50)


def main():
    display_choice()

    while True:
        try:
            choice = input("请输入选项数字 (1-3): ").strip()

            if choice == "1":
                print("\n[你站起身，向舞台走去...]")
                print("[系统将切换到分支: branch_sweet]")
                return "branch_sweet"
            elif choice == "2":
                print("\n[你选择留在座位上...]")
                print("[系统将切换到分支: branch_be]")
                return "branch_be"
            elif choice == "3":
                print("\n[你从座位上冲了出去...]")
                print("[系统将切换到分支: branch_sweet]")
                return "branch_sweet"
            else:
                print("无效选项，请输入 1、2 或 3")
        except EOFError:
            print("\n\n[已退出选择]")
            sys.exit(0)


if __name__ == "__main__":
    result = main()
    print(f"\n>>> 前往: {result}")
