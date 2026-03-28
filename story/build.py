#!/usr/bin/env python3
"""
构建脚本：根据 story/ 下的 yaml 文件构建游戏目录
直接提交到 git，不生成 game/nodes/ 目录
"""

import os
import re
import json
import yaml
import shutil
import subprocess
from pathlib import Path


BASE_DIR = Path(__file__).parent.parent
STORY_DIR = BASE_DIR / "story"
GAME_DIR = BASE_DIR / "game"


NODE_ORDER = {
    "main": [
        "node_01",
        "node_02",
        "node_03",
        "node_04",
        "node_05",
        "node_06",
        "node_07",
        "node_08",
        "node_09",
        "node_14",
        "node_15",
        "node_16",
    ],
    "branch_memory": ["node_10", "node_11", "node_12", "node_13"],
    "branch_be": [
        "node_17_be",
        "node_18",
        "node_21",
        "node_22",
        "node_24",
        "node_25",
    ],
    "branch_sweet": [
        "node_17_sweet",
        "node_19",
        "node_23",
        "node_20",
        "node_24",
        "node_25",
    ],
}


def run_git(cmd, cwd=None, check=True):
    """Run a git command"""
    result = subprocess.run(
        cmd, shell=True, cwd=cwd or GAME_DIR, capture_output=True, text=True
    )
    if result.returncode != 0 and check:
        print(f"Git command failed: {cmd}")
        print(f"stderr: {result.stderr}")
    return result


def init_git_repo():
    """Initialize git repository"""
    if not (GAME_DIR / ".git").exists():
        GAME_DIR.mkdir(parents=True, exist_ok=True)
        run_git("git init", cwd=GAME_DIR)
        run_git("git config user.email 'game@blank-graduation.local'", cwd=GAME_DIR)
        run_git("git config user.name 'Blank Graduation'", cwd=GAME_DIR)
        run_git("git branch -M main", cwd=GAME_DIR)
        print("Initialized git repository")


def load_yaml_files(branch):
    """Load all yaml files for a branch, ordered by NODE_ORDER"""
    branch_dir = STORY_DIR / branch
    if not branch_dir.exists():
        return {}

    result = {}
    for node_id in NODE_ORDER.get(branch, []):
        yaml_file = branch_dir / f"{node_id}.yaml"
        if yaml_file.exists():
            with open(yaml_file, "r", encoding="utf-8") as f:
                result[node_id] = yaml.safe_load(f)

    return result


def create_branch(branch_name):
    """Create a new git branch"""
    run_git(f"git checkout -b {branch_name}", cwd=GAME_DIR, check=False)


def create_commit(node_id, message=""):
    """Create a git commit for a node"""
    run_git("git add -A", cwd=GAME_DIR)
    commit_msg = message or f"Node: {node_id}"
    result = run_git(f'git commit -m "{commit_msg}"', cwd=GAME_DIR, check=False)

    tag_name = node_id
    run_git(f'git tag -a {tag_name} -m "Node {tag_name}"', cwd=GAME_DIR, check=False)


def checkout_branch(branch_name):
    """Checkout a git branch"""
    result = run_git(f"git checkout {branch_name}", cwd=GAME_DIR, check=False)
    return result.returncode == 0


def write_node_files_to_git(node_id, data):
    """Write node files directly to git working tree"""
    scene = data.get("scene", "")
    story = data.get("story", "")
    note = data.get("note", "")
    choices = data.get("choices", [])

    with open(GAME_DIR / "Scene.md", "w", encoding="utf-8") as f:
        f.write(scene)

    with open(GAME_DIR / "Story.md", "w", encoding="utf-8") as f:
        f.write(story)

    with open(GAME_DIR / "Note.md", "w", encoding="utf-8") as f:
        f.write(note)

    with open(GAME_DIR / "choices.json", "w", encoding="utf-8") as f:
        json.dump(choices, f, ensure_ascii=False, indent=2)


def parse_target(target):
    """Parse target into branch and node_id"""
    if target == "END":
        return (None, "END")

    if ":" in target:
        parts = target.split(":", 1)
        return (parts[0], parts[1])

    return (None, target)


CHOICE_PY_TEMPLATE = '''#!/usr/bin/env python3
"""
空白毕业典礼 - Choice.py
游戏选择引擎
从 git commit 读取内容
"""

import json
import os
import sys
import subprocess
from pathlib import Path

GAME_DIR = Path(__file__).parent
STATE_FILE = GAME_DIR / ".state.json"


def load_state():
    if STATE_FILE.exists():
        with open(STATE_FILE, 'r', encoding='utf-8') as f:
            return json.load(f)
    return {
        "current_node": "node_01",
        "current_branch": "main",
        "history": [],
        "visited_nodes": []
    }


def save_state(state):
    with open(STATE_FILE, 'w', encoding='utf-8') as f:
        json.dump(state, f, ensure_ascii=False, indent=2)


def git_show(ref, file_path):
    """Read file content from a git tag/ref"""
    result = subprocess.run(
        ["git", "show", f"{ref}:{file_path}"],
        cwd=GAME_DIR,
        capture_output=True,
        text=True
    )
    if result.returncode == 0:
        return result.stdout
    return ""


def git_checkout(ref):
    """Checkout a specific commit or branch"""
    result = subprocess.run(
        ["git", "checkout", ref],
        cwd=GAME_DIR,
        capture_output=True,
        text=True
    )
    return result.returncode == 0


if sys.platform == 'win32':
    import io
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')
    sys.stdin = io.TextIOWrapper(sys.stdin.buffer, encoding='utf-8', errors='replace')


def load_current_node(state):
    """Load current node data from git commit"""
    node_id = state.get("current_node", "node_01")

    scene = git_show(f"node_{node_id}", "Scene.md")
    story = git_show(f"node_{node_id}", "Story.md")
    note = git_show(f"node_{node_id}", "Note.md")
    choices_str = git_show(f"node_{node_id}", "choices.json")

    try:
        choices = json.loads(choices_str) if choices_str else []
    except json.JSONDecodeError:
        choices = []

    return {
        'node_id': node_id,
        'scene': scene,
        'story': story,
        'note': note,
        'choices': choices
    }


def display_node(node_data):
    print()
    print("=" * 60)
    print(f"【{node_data.get('node_id', '?')}】")
    print("=" * 60)
    print()

    scene = node_data.get('scene', '')
    if scene:
        print(scene)

    print()

    story = node_data.get('story', '')
    if story:
        print(story)


def show_choices(choices):
    print()
    print("你会怎么做？")
    print()

    for i, choice in enumerate(choices, 1):
        print(f"  [{i}] {choice['text']}")

    print()


def parse_target(target):
    if target == "END":
        return (None, "END")

    if ':' in str(target):
        parts = str(target).split(':', 1)
        return (parts[0], parts[1])
    return (None, str(target))


def handle_choice(choice_num, choices, state):
    if choice_num < 1 or choice_num > len(choices):
        print("无效的选择。")
        return None

    choice = choices[choice_num - 1]
    target = choice['target']

    if target == "END":
        print()
        print("=" * 60)
        print("感谢游玩《空白毕业典礼》")
        print("=" * 60)
        print()
        print("一个关于记忆、失去和重新开始的故事。")
        print()
        print("也许，下次再见。")
        print()
        return None

    target_branch, target_node = parse_target(target)

    if target_branch:
        state["current_branch"] = target_branch
        git_checkout(target_branch)

    state["current_node"] = target_node
    state["history"].append(target_node)
    state["visited_nodes"].append(target_node)

    return target_node


def display_status():
    state = load_state()
    print(f"当前节点: {state['current_node']}")
    print(f"当前分支: {state['current_branch']}")
    if state['history']:
        print(f"历史: {' -> '.join(state['history'][-5:])}")


def main():
    state = load_state()

    if len(sys.argv) > 1:
        if sys.argv[1] == "--status":
            display_status()
            return
        elif sys.argv[1] == "--goto" and len(sys.argv) > 2:
            target = sys.argv[2]
            target_branch, target_node = parse_target(target)
            if target_branch:
                state["current_branch"] = target_branch
                git_checkout(target_branch)
            state["current_node"] = target_node
            state["history"].append(target_node)
            state["visited_nodes"].append(target_node)
            save_state(state)
            print(f"已跳转到: {target}")
            return
        elif sys.argv[1] == "--choice" and len(sys.argv) > 2:
            try:
                choice_num = int(sys.argv[2])
                node_data = load_current_node(state)
            except ValueError:
                print("无效的选择数字。")
                return
        else:
            print("用法: python Choice.py [--status] [--goto <node>] [--choice <num>]")
            return
    else:
        node_data = load_current_node(state)

        if not node_data:
            print("无法加载节点数据。")
            return

        display_node(node_data)
        show_choices(node_data.get('choices', []))

        try:
            choice_num = int(input("请输入你的选择: "))
        except ValueError:
            print("请输入有效的数字。")
            return

    result = handle_choice(choice_num, node_data.get('choices', []), state)

    if result:
        save_state(state)
        print(f"\\n→ 前往: {result}")
        print("=" * 60)


if __name__ == "__main__":
    main()
'''


def init_state_json():
    """Initialize .state.json"""
    state = {
        "current_node": "node_01",
        "current_branch": "main",
        "history": ["node_01"],
        "visited_nodes": ["node_01"],
    }

    with open(GAME_DIR / ".state.json", "w", encoding="utf-8") as f:
        json.dump(state, f, ensure_ascii=False, indent=2)


def build():
    """Main build function"""

    print("Building game...")

    if GAME_DIR.exists():
        git_dir = GAME_DIR / ".git"
        if git_dir.exists():
            import stat

            def on_rm_error(func, path, exc_info):
                if not os.path.exists(path):
                    return
                os.chmod(path, stat.S_IWRITE)
                func(path)
                if os.path.exists(path):
                    on_rm_error(func, path, exc_info)

            shutil.rmtree(git_dir, onerror=on_rm_error)
        for item in GAME_DIR.iterdir():
            if item.name != ".git":
                if item.is_dir():
                    shutil.rmtree(item)
                else:
                    item.unlink()
    GAME_DIR.mkdir(parents=True, exist_ok=True)

    init_git_repo()

    checkout_branch("main")

    print("\n=== Building main branch ===")
    main_nodes = load_yaml_files("main")

    for node_id in NODE_ORDER["main"]:
        if node_id not in main_nodes:
            print(f"Warning: {node_id} not found in main branch")
            continue

        data = main_nodes[node_id]
        write_node_files_to_git(node_id, data)
        create_commit(node_id)
        print(f"Added: {node_id}")

    main_head = subprocess.run(
        ["git", "rev-parse", "HEAD"], cwd=GAME_DIR, capture_output=True, text=True
    ).stdout.strip()

    print("\n=== Building branch_memory ===")
    checkout_branch("main")

    memory_nodes = load_yaml_files("branch_memory")
    create_branch("branch_memory")

    for node_id in NODE_ORDER["branch_memory"]:
        if node_id not in memory_nodes:
            print(f"Warning: {node_id} not found in branch_memory")
            continue

        data = memory_nodes[node_id]
        write_node_files_to_git(node_id, data)
        create_commit(node_id)
        print(f"Added: {node_id}")

    print("\n=== Building branch_be ===")
    checkout_branch(main_head)
    create_branch("branch_be")

    be_nodes = load_yaml_files("branch_be")

    for node_id in NODE_ORDER["branch_be"]:
        if node_id not in be_nodes:
            print(f"Warning: {node_id} not found in branch_be")
            continue

        data = be_nodes[node_id]
        write_node_files_to_git(node_id, data)
        create_commit(node_id)
        print(f"Added: {node_id}")

    print("\n=== Building branch_sweet ===")
    checkout_branch(main_head)
    create_branch("branch_sweet")

    sweet_nodes = load_yaml_files("branch_sweet")

    for node_id in NODE_ORDER["branch_sweet"]:
        if node_id not in sweet_nodes:
            print(f"Warning: {node_id} not found in branch_sweet")
            continue

        data = sweet_nodes[node_id]
        write_node_files_to_git(node_id, data)
        create_commit(node_id)
        print(f"Added: {node_id}")

    checkout_branch("main")

    choice_py_path = GAME_DIR / "Choice.py"
    with open(choice_py_path, "w", encoding="utf-8") as f:
        f.write(CHOICE_PY_TEMPLATE)

    print(f"\nGenerated: Choice.py")

    init_state_json()
    print("Generated: .state.json")

    print("\n=== Build completed! ===")
    print(f"Game directory: {GAME_DIR}")
    print("\nTo play:")
    print(f"  cd {GAME_DIR}")
    print("  python Choice.py")


if __name__ == "__main__":
    build()
