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

## 2) 핵심: 이건 어디서 실행하나요?

- **GitHub 웹사이트에서 실행하는 게 아닙니다.**
- GitHub는 코드 저장소이고, 실제 실행은 **내 PC PowerShell/터미널**에서 합니다.
- 현재 엔진은 Python이며, Node 사용자는 `npm run demo`로 감싸서 실행할 수 있습니다.

---

## 3) PowerShell에서 가장 쉽게 실행하는 방법 (Windows)

아래는 **그대로 복붙 가능한 순서**입니다.

### 3-1. 프로젝트 폴더로 이동

```powershell
cd C:\경로\claw-empire-유사-프로젝트
```

예시:

```powershell
cd C:\work\game
```

### 3-2. Python 설치 확인

```powershell
python --version
```

버전이 나오면 정상입니다. (`Python 3.10+` 권장)

### 3-3. 1회 실행 (설치 없이)

```powershell
$env:PYTHONPATH = "src"
python scripts/run_demo.py --goal "신규 반려동물 간식 브랜드 런칭"
```

실행 후 결과 JSON은 기본적으로 `docs/sample_report.json`에 저장됩니다.

### 3-4. PowerShell 전용 실행 스크립트 사용 (더 편함)

```powershell
.\scripts\run_demo.ps1 -Goal "신규 반려동물 간식 브랜드 런칭"
```

저장 경로를 바꾸려면:

```powershell
.\scripts\run_demo.ps1 -Goal "신규 뷰티 브랜드 런칭" -Save "docs\my_report.json"
```

---

## 4) 경로 지정 규칙 (헷갈리는 부분 정리)

### A. `cd` 경로

- `cd`는 **프로젝트 루트 폴더**로 이동해야 합니다.
- 루트 폴더 기준으로 아래 파일이 보여야 정상입니다:
  - `README.md`
  - `scripts\run_demo.py`
  - `src\ai_team_system\...`

확인 명령:

```powershell
Get-ChildItem
```

### B. `--save` 경로

- 상대경로: 현재 폴더 기준
  - `--save "docs\my_report.json"`
- 절대경로: 원하는 위치 직접 지정
  - `--save "C:\work\output\report.json"`

예시:

```powershell
python scripts/run_demo.py --goal "테스트" --save "C:\work\output\report.json"
```

---

## 5) Node 사용자용 실행 (PowerShell에서도 가능)

Node 방식은 내부에서 Python을 호출합니다.

```powershell
npm run demo
```

목표/저장 경로 넘기기:

```powershell
npm run demo -- --goal "신규 뷰티 브랜드 런칭" --save "docs/my_report.json"
```

---

## 6) 설치형(반복 사용 시 추천)

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -e .
ai-team-demo --goal "신규 반려동물 간식 브랜드 런칭"
```

---

## 7) 자주 묻는 질문

### Q1. 파워셸에서 입력하면 되는 거야?
네. **PowerShell에서 명령어 입력하면 됩니다.**

### Q2. 경로는 어떻게 지정해?
1) 먼저 `cd`로 프로젝트 루트로 이동하고, 2) `--save`는 상대/절대 경로 중 편한 방식으로 지정하면 됩니다.

### Q3. 이걸 GitHub에서 실행하는 거야?
아니요. GitHub는 코드 저장소고, 실행은 로컬(내 PC)에서 합니다.

### Q4. Node만 쓰던 사람인데 가능해?
가능합니다. `npm run demo`로 시작하면 됩니다(내부에서 Python 호출).

---

## 8) 실제 확장 포인트

1. LLM API 연동(OpenAI, Azure OpenAI, Anthropic 등)
2. 외부 데이터 연동
   - 트렌드/검색량 API
   - SNS API
   - 스토어(스마트스토어/쿠팡/Shopify) API
   - 광고 플랫폼 API(Meta, Google, TikTok)
3. 작업 큐(Celery/RQ) + DB(PostgreSQL)
4. 관리자 대시보드(FastAPI + Next.js or Node + Next.js)

## 9) 추천 운영 규칙

- 모든 산출물에 `근거(source)` 필드 포함
- 실행성 높은 항목에 `priority`, `owner`, `due_date` 지정
- 반복 업무는 스케줄러(cron)로 자동 생성
