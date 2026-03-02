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

## 2) 먼저 이해하기: 이건 어디서 돌리나요?

- **GitHub에서 자동으로 돌아가는 서비스가 아닙니다.**
- 이 저장소를 **내 PC(로컬)**로 받아서 실행하는 코드입니다.
- 핵심 엔진은 Python이고, Node 사용자를 위해 `npm run demo`도 지원합니다.

## 3) 실행 방법 (Node 사용자 기준 추천)

### 방법 A: Node 명령으로 실행 (가장 익숙한 방식)

> Node로 실행하지만 내부적으로 Python 스크립트를 호출합니다.

```bash
cd /workspace/game
npm run demo
```

다른 목표로 실행하려면:

```bash
npm run demo -- --goal "신규 뷰티 브랜드 런칭"
```

## 4) 실행 방법 (Python 직접 실행)

### 방법 B: 설치 없이 바로 실행

```bash
cd /workspace/game
make run-demo
```

### 방법 C: Python 스크립트 직접 실행

```bash
cd /workspace/game
PYTHONPATH=src python3 scripts/run_demo.py --goal "신규 반려동물 간식 브랜드 런칭"
```

### 방법 D: 설치형 CLI 실행

```bash
cd /workspace/game
python3 -m venv .venv
source .venv/bin/activate
pip install -e .
ai-team-demo --goal "신규 반려동물 간식 브랜드 런칭"
```

실행 후 결과는 콘솔에 출력되고 기본적으로 `docs/sample_report.json` 파일에도 저장됩니다.

## 5) 결과 파일 위치 바꾸기

```bash
npm run demo -- --goal "신규 반려동물 간식 브랜드 런칭" --save docs/my_report.json
```

또는

```bash
ai-team-demo --goal "신규 반려동물 간식 브랜드 런칭" --save docs/my_report.json
```

## 6) 자주 묻는 질문

### Q1. 내가 파이썬으로 설치해야 하나요?
- 엄밀히는 Python 코드가 핵심이라 Python이 필요합니다.
- 다만 Node 사용자는 `npm run demo`로 실행하면 됩니다(내부에서 Python 호출).

### Q2. 그럼 이건 GitHub에서 하는 건가요?
- 아닙니다. GitHub는 코드 저장소입니다.
- 실제 실행은 로컬 PC(또는 서버)에서 합니다.

### Q3. Node만으로 완전한 버전은 없나요?
- 현재 구현은 Python 기반입니다.
- 원하시면 다음 단계에서 FastAPI 대신 Express/Nest 기반으로 오케스트레이터를 Node로 포팅할 수 있습니다.

## 7) 실제 확장 포인트

1. LLM API 연동(OpenAI, Azure OpenAI, Anthropic 등)
2. 외부 데이터 연동
   - 트렌드/검색량 API
   - SNS API
   - 스토어(스마트스토어/쿠팡/Shopify) API
   - 광고 플랫폼 API(Meta, Google, TikTok)
3. 작업 큐(Celery/RQ) + DB(PostgreSQL)
4. 관리자 대시보드(FastAPI + Next.js or Node + Next.js)

## 8) 추천 운영 규칙

- 모든 산출물에 `근거(source)` 필드 포함
- 실행성 높은 항목에 `priority`, `owner`, `due_date` 지정
- 반복 업무는 스케줄러(cron)로 자동 생성
