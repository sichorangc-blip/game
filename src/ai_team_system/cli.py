import argparse
import json
from pathlib import Path

from .orchestrator import TeamOrchestrator


def main() -> None:
    parser = argparse.ArgumentParser(description="AI 비즈니스 운영팀 데모 실행")
    parser.add_argument("--goal", required=True, help="예: 신규 가습마스크 브랜드 런칭")
    parser.add_argument(
        "--save",
        default="docs/sample_report.json",
        help="결과 JSON 저장 경로",
    )
    parser.add_argument(
        "--chat",
        action="store_true",
        help="실행 과정을 채팅형 로그로 출력",
    )
    args = parser.parse_args()

    orchestrator = TeamOrchestrator()

    def on_progress(message: str) -> None:
        print(f"[CHAT] {message}")

    report = orchestrator.run(
        args.goal,
        progress_callback=on_progress if args.chat else None,
    )

    output_path = Path(args.save)
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(
        json.dumps(report.as_dict(), ensure_ascii=False, indent=2),
        encoding="utf-8",
    )

    print(json.dumps(report.as_dict(), ensure_ascii=False, indent=2))
    print(f"\n저장 완료: {output_path}")


if __name__ == "__main__":
    main()
