#!/usr/bin/env python3
"""校验 transmigrator-strategist 通用 agent 仓库结构。

检查项：
  1. 核心文件齐全（AGENTS.md / LICENSE / README.md）
  2. avatar 存在且尺寸合规（≤500KB，建议 512×512）
  3. plugin.json（WorkBuddy 兼容层）存在且为合法 JSON

用法：
  python3 scripts/validate_agent.py [仓库根目录]
默认仓库根目录为脚本上级目录。
"""
import json
import os
import sys
from pathlib import Path

MAX_AVATAR_BYTES = 500 * 1024
EXPECTED_AVATAR_SIZE = (512, 512)


def fail(msg: str) -> bool:
    print(f"  [FAIL] {msg}")
    return False


def ok(msg: str) -> bool:
    print(f"  [ OK ] {msg}")
    return True


def check_repo(root: Path) -> int:
    errors = 0
    print(f"校验仓库：{root}\n")

    # 1. 核心文件
    for f in ("AGENTS.md", "LICENSE", "README.md"):
        p = root / f
        if p.is_file():
            ok(f"存在：{f}")
        else:
            errors += 1
            fail(f"缺失核心文件：{f}")

    # 2. avatar
    avatar = root / "avatars" / "expert.png"
    if not avatar.is_file():
        errors += 1
        fail("缺失头像：avatars/expert.png")
    else:
        size = avatar.stat().st_size
        if size <= MAX_AVATAR_BYTES:
            ok(f"头像体积合规：{size/1024:.0f}KB (≤500KB)")
        else:
            errors += 1
            fail(f"头像过大：{size/1024:.0f}KB，需 ≤500KB")
        try:
            from PIL import Image
            with Image.open(avatar) as im:
                if im.size == EXPECTED_AVATAR_SIZE:
                    ok(f"头像尺寸合规：{im.size}")
                else:
                    print(f"  [WARN] 头像尺寸 {im.size}，建议 {EXPECTED_AVATAR_SIZE}")
        except Exception:
            print("  [WARN] 未安装 Pillow，跳过尺寸检查（pip install Pillow）")

    # 3. plugin.json（WorkBuddy 兼容层）
    pj = root / ".codebuddy-plugin" / "plugin.json"
    if not pj.is_file():
        print("  [WARN] 无 WorkBuddy 兼容层 .codebuddy-plugin/plugin.json（仅影响 WorkBuddy 加载）")
    else:
        try:
            data = json.loads(pj.read_text(encoding="utf-8"))
            assert "name" in data and "displayName" in data
            dn = data["displayName"]
            dn_label = dn if isinstance(dn, str) else (dn.get("en") or dn.get("zh") or data["name"])
            ok(f"plugin.json 合法：{dn_label}")
        except Exception as e:
            errors += 1
            fail(f"plugin.json 非法：{e}")

    print()
    if errors == 0:
        print("校验通过：仓库结构完整，可发布。")
        return 0
    print(f"校验未通过：发现 {errors} 处问题，请修正后再发布。")
    return 1


if __name__ == "__main__":
    root = Path(sys.argv[1]) if len(sys.argv) > 1 else Path(__file__).resolve().parent.parent
    sys.exit(check_repo(root))
