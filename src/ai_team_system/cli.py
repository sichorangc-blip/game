import argparse
import json
from pathlib import Path

from .orchestrator import TeamOrchestrator


def main() -> None:
    parser = argparse.ArgumentParser(description="AI 비즈니스 운영팀 데모 실행")
    parser.add_argument("--goal", required=True, help="예: 신규 고양이 사료 브랜드 런칭")
    parser.add_argument(
        "--save",
        default="docs/sample_report.json",
        help="결과 JSON 저장 경로",
    )
    args = parser.parse_args()

    orchestrator = TeamOrchestrator()
    report = orchestrator.run(args.goal)

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
