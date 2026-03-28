#!/usr/bin/env python3
"""
迁移脚本：将旧格式（dev_script/nodes/node_XX/）转换为新格式（story/{branch}/node_XX.yaml）
"""

import os
import re
import yaml
import shutil
from pathlib import Path


BASE_DIR = Path(__file__).parent.parent
DEV_SCRIPT_DIR = BASE_DIR / "dev_script" / "nodes"
STORY_DIR = BASE_DIR / "story"

BRANCH_NODE_MAP = {
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
        "node_24_be",
        "node_25",
    ],
    "branch_sweet": [
        "node_17_sweet",
        "node_19",
        "node_20",
        "node_23",
        "node_24_sweet",
        "node_25",
    ],
}

TARGET_BRANCH_OVERRIDE = {
    "node_10": "branch_memory",
    "node_11": "branch_memory",
    "node_12": "branch_memory",
    "node_13": "branch_memory",
}


def get_base_node_id(node_id):
    for suffix in ["_be", "_sweet"]:
        if node_id.endswith(suffix):
            return node_id[: -len(suffix)]
    return node_id


def get_branches_for_node(node_id):
    """Get all branches a node belongs to"""
    branches = []
    for branch, nodes in BRANCH_NODE_MAP.items():
        if node_id in nodes:
            branches.append(branch)
    if not branches:
        branches = ["main"]
    return branches


def parse_choice_py(content):
    choices = []

    match = re.search(
        r"def get_choices\(\):\s*return\s*\{([^}]+(?:\{[^}]+\}[^}]*)*)\}",
        content,
        re.DOTALL,
    )
    if not match:
        return choices

    choice_block = match.group(0)

    pattern = r'(\d+):\s*\{[^}]*"text":\s*"([^"]+)"[^}]*"target":\s*"([^"]+)"[^}]*\}'
    for match in re.finditer(pattern, choice_block):
        num = int(match.group(1))
        text = match.group(2)
        target = match.group(3)
        choices.append({"num": num, "text": text, "target": target})

    if not choices:
        simple_pattern = (
            r'(\d+):\s*\{[^}]*"text":\s*"([^"]+)"[^}]*"target":\s*"([^"]+)"'
        )
        for match in re.finditer(simple_pattern, simple_pattern):
            num = int(match.group(1))
            text = match.group(2)
            target = match.group(3)
            choices.append({"num": num, "text": text, "target": target})

    return sorted(choices, key=lambda x: x.get("text", ""))


def read_file(path):
    try:
        with open(path, "r", encoding="utf-8") as f:
            return f.read()
    except FileNotFoundError:
        return ""
    except Exception as e:
        print(f"Error reading {path}: {e}")
        return ""


def process_node(node_dir, node_id):
    scene = read_file(node_dir / "Scene.md")
    story = read_file(node_dir / "Story.md")
    note = read_file(node_dir / "Note.md")
    choice_content = read_file(node_dir / "Choice.py")

    choices = parse_choice_py(choice_content)

    return {
        "scene": scene,
        "story": story,
        "note": note,
        "choices": choices,
        "_original_node_id": node_id,
    }


def convert_target_for_branch(target, target_branch):
    if target == "END":
        return "END"

    if not target.startswith("node_"):
        return target

    base_target = get_base_node_id(target)

    if base_target == "node_24":
        if target_branch in ["branch_be", "branch_sweet"]:
            suffix = target_branch.split("_")[1]
            return f"node_24_{suffix}"

    return target


def generate_yaml(output_node_id, data, target_branch, choices_override=None):
    choices = choices_override if choices_override is not None else data["choices"]

    converted_choices = []
    for choice in choices:
        raw_target = choice["target"]
        final_target = convert_target_for_branch(raw_target, target_branch)
        converted_choices.append({"text": choice["text"], "target": final_target})

    yaml_data = {
        "node_id": output_node_id,
        "scene": data["scene"],
        "story": data["story"],
        "choices": converted_choices,
    }

    if data["note"].strip():
        yaml_data["note"] = data["note"]

    return yaml_data


def write_yaml(branch, node_id, yaml_data):
    output_file = STORY_DIR / branch / f"{node_id}.yaml"
    with open(output_file, "w", encoding="utf-8") as f:
        yaml.dump(
            yaml_data, f, allow_unicode=True, default_flow_style=False, sort_keys=False
        )
    print(f"Migrated: {branch}/{node_id}.yaml")


SPLIT_NODES = {
    "node_17": {
        "branch_be": [
            {"num": 1, "text": "告诉我真相", "target": "node_18"},
            {"num": 2, "text": "我已经累了，算了吧", "target": "node_18"},
        ],
        "branch_sweet": [
            {"num": 1, "text": "我们重新开始吧", "target": "node_19"},
            {"num": 2, "text": "带我去看樱花", "target": "node_19"},
        ],
    },
    "node_24": {
        "branch_be": None,
        "branch_sweet": None,
    },
}


DUPLICATE_NODES = ["node_25"]


def migrate():
    for branch in ["main", "branch_memory", "branch_be", "branch_sweet"]:
        branch_dir = STORY_DIR / branch
        if branch_dir.exists():
            shutil.rmtree(branch_dir)
        branch_dir.mkdir(parents=True, exist_ok=True)

    for node_dir in sorted(DEV_SCRIPT_DIR.iterdir()):
        if not node_dir.is_dir() or not node_dir.name.startswith("node_"):
            continue

        node_id = node_dir.name
        base_id = get_base_node_id(node_id)

        if base_id in SPLIT_NODES:
            base_data = process_node(node_dir, node_id)

            for branch_name, choices_override in SPLIT_NODES[base_id].items():
                if choices_override is not None:
                    suffix = branch_name.split("_")[1]
                    output_id = f"{base_id}_{suffix}"
                else:
                    suffix = branch_name.split("_")[1]
                    output_id = f"{base_id}_{suffix}"

                yaml_data = generate_yaml(
                    output_id, base_data, branch_name, choices_override
                )
                write_yaml(branch_name, output_id, yaml_data)

        elif base_id in DUPLICATE_NODES:
            branches = get_branches_for_node(node_id)
            base_data = process_node(node_dir, node_id)

            for branch in branches:
                yaml_data = generate_yaml(node_id, base_data, branch)
                write_yaml(branch, node_id, yaml_data)

        else:
            branches = get_branches_for_node(node_id)
            data = process_node(node_dir, node_id)

            for branch in branches:
                yaml_data = generate_yaml(node_id, data, branch)
                write_yaml(branch, node_id, yaml_data)

    print("\nMigration completed!")
    print(f"Output directory: {STORY_DIR}")


if __name__ == "__main__":
    migrate()
