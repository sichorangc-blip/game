#!/usr/bin/env python3
"""Minimal OpenAI connectivity/origin diagnostic.

Usage (PowerShell):
  $env:OPENAI_API_KEY="sk-..."
  python .\scripts\api_probe.py
  python .\scripts\api_probe.py --origin http://localhost:8000
"""

from __future__ import annotations

import argparse
import json
import os
import sys
import urllib.request
import urllib.error


def main() -> int:
    parser = argparse.ArgumentParser(description="OpenAI API 연결/Origin 진단")
    parser.add_argument("--key", default=os.getenv("OPENAI_API_KEY", ""), help="OpenAI API key")
    parser.add_argument("--base-url", default="https://api.openai.com/v1", help="API base url")
    parser.add_argument("--origin", default="", help="Optional Origin header for debugging")
    args = parser.parse_args()

    if not args.key:
        print("[probe] OPENAI_API_KEY가 없습니다. --key 또는 환경변수로 전달하세요.")
        return 2

    url = args.base_url.rstrip("/") + "/models"
    req = urllib.request.Request(url)
    req.add_header("Authorization", f"Bearer {args.key}")
    if args.origin:
        req.add_header("Origin", args.origin)

    try:
        with urllib.request.urlopen(req, timeout=15) as resp:
            body = resp.read().decode("utf-8", errors="replace")
            print(f"[probe] status={resp.status}")
            print(f"[probe] ok=True")
            print(f"[probe] body_prefix={body[:200]}")
            return 0
    except urllib.error.HTTPError as e:
        body = e.read().decode("utf-8", errors="replace")
        print(f"[probe] status={e.code}")
        print("[probe] ok=False")
        print(f"[probe] body_prefix={body[:400]}")
        try:
            obj = json.loads(body)
            code = (obj.get("error") or {}).get("code")
            if code:
                print(f"[probe] error.code={code}")
        except Exception:
            pass
        return 1
    except Exception as e:
        print("[probe] request_failed:", e)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
