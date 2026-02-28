# AI 비즈니스 운영팀 시스템 (Claw Empire 스타일)

이 저장소는 여러 역할의 AI 봇이 협업하여 다음 업무를 자동화/반자동화하도록 설계된 **멀티 에이전트 운영 시스템**입니다.

- 시장조사
- SNS 게시글 기획/관리
- 쇼핑스토어 운영
- 신제품 개발 검토
- 브랜딩 전략
- 광고 집행 기획
- 디자이너 브리프 생성

## 1) 시스템 구조

```text
요청 입력
  └─ 오케스트레이터(Workflow Router)
       ├─ 시장조사 에이전트
       ├─ SNS 운영 에이전트
       ├─ 스토어 운영 에이전트
       ├─ 신제품 검토 에이전트
       ├─ 브랜딩 에이전트
       ├─ 광고 에이전트
       └─ 디자인 에이전트
            └─ 통합 보고서 + 실행 체크리스트
```

## 2) 핵심 개념

- **역할 기반 에이전트(Role-based agents)**: 각 에이전트가 KPI, 입력, 출력 형식을 가짐
- **워크플로우 기반 협업(Workflow DAG)**: 선행 결과를 후속 에이전트가 활용
- **표준 산출물(JSON)**: 자동 저장/대시보드 연결 가능
- **사람 검토 지점(Human-in-the-loop)**: 광고 집행, 실제 게시 예약 전 승인

## 3) 빠른 시작

```bash
python3 scripts/run_demo.py --goal "신규 반려동물 간식 브랜드 런칭"
```

실행 시 `docs/sample_report.json` 형식의 결과를 터미널에 출력합니다.

## 4) 실제 확장 포인트

1. LLM API 연동(OpenAI, Azure OpenAI, Anthropic 등)
2. 외부 데이터 연동
   - 트렌드/검색량 API
   - SNS API
   - 스토어(스마트스토어/쿠팡/Shopify) API
   - 광고 플랫폼 API(Meta, Google, TikTok)
3. 작업 큐(Celery/RQ) + DB(PostgreSQL)
4. 관리자 대시보드(FastAPI + Next.js)

## 5) 추천 운영 규칙

- 모든 산출물에 `근거(source)` 필드 포함
- 실행성 높은 항목에 `priority`, `owner`, `due_date` 지정
- 반복 업무는 스케줄러(cron)로 자동 생성

