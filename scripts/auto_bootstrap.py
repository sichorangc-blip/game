#!/usr/bin/env python3
"""Automatic runner for first-time users.

Priority:
1) run_demo.py at repository root
2) scripts/run_demo.py
3) npm run demo (if package.json exists)
"""

from __future__ import annotations

import argparse
import subprocess
import sys
from pathlib import Path


def run(cmd: list[str], cwd: Path) -> int:
    print("[auto] 실행:", " ".join(cmd))
    proc = subprocess.run(cmd, cwd=cwd)
    return proc.returncode


def main() -> int:
    parser = argparse.ArgumentParser(description="자동 실행 도우미")
    parser.add_argument("--goal", default="신규 반려동물 간식 브랜드 런칭")
    parser.add_argument("--save", default="docs/sample_report.json")
    args = parser.parse_args()

    root = Path(__file__).resolve().parents[1]

    root_runner = root / "run_demo.py"
    script_runner = root / "scripts" / "run_demo.py"
    package_json = root / "package.json"

    if root_runner.exists():
        return run(
            [sys.executable, str(root_runner), "--goal", args.goal, "--save", args.save],
            root,
        )

    if script_runner.exists():
        return run(
            [sys.executable, str(script_runner), "--goal", args.goal, "--save", args.save],
            root,
        )

    if package_json.exists():
        return run(["npm", "run", "demo", "--", "--goal", args.goal, "--save", args.save], root)

    print("[auto] 실행 가능한 엔트리포인트를 찾지 못했습니다.")
    print("[auto] 현재 폴더가 프로젝트 루트인지 확인하세요.")
    print("[auto] 확인 항목: run_demo.py / scripts/run_demo.py / package.json")
    return 1


if __name__ == "__main__":
    raise SystemExit(main())
