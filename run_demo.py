#!/usr/bin/env python3
"""Root-level runner to avoid path confusion.

Usage:
    python run_demo.py --goal "신규 가습마스크 브랜드 런칭"
"""

from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parent
SRC = ROOT / "src"
if str(SRC) not in sys.path:
    sys.path.insert(0, str(SRC))

from ai_team_system.cli import main


if __name__ == "__main__":
    main()
