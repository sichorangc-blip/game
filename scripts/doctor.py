#!/usr/bin/env python3
"""Diagnose common setup issues for local runs and CLI-tool readiness."""

from __future__ import annotations

import platform
import shutil
from pathlib import Path


ROOT = Path.cwd()

CHECKS = [
    "README.md",
    "package.json",
    "pyproject.toml",
    "run_demo.py",
    "scripts/run_demo.py",
    "scripts/auto_bootstrap.py",
]

CLI_BINS = ["node", "npm", "pnpm", "codex", "claude", "gemini", "opencode"]


def main() -> int:
    print("[doctor] platform:", platform.platform())
    print("[doctor] cwd:", ROOT)
    print("[doctor] python:", platform.python_version())
    print("[doctor] files:")

    missing = []
    for rel in CHECKS:
        exists = (ROOT / rel).exists()
        print(f"  - {rel}: {'OK' if exists else 'MISSING'}")
        if not exists:
            missing.append(rel)

    print("\n[doctor] cli binaries:")
    for name in CLI_BINS:
        print(f"  - {name}: {'FOUND' if shutil.which(name) else 'MISSING'}")

    if missing:
        print("\n[doctor] 일부 파일이 없습니다.")
        print("[doctor] 현재 폴더가 올바른 저장소 루트인지 확인하세요.")
        print("[doctor] PowerShell 예시:")
        print("  git remote -v")
        print("  git branch")
        print("  git pull")
        print("  Get-ChildItem")
        return 1

    print("\n[doctor] 실행 파일이 모두 확인되었습니다.")
    print("[doctor] 이제 아래 명령으로 실행하세요:")
    print('  python run_demo.py --goal "신규 가습마스크 브랜드 런칭"')
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
