# AI 비즈니스 운영팀 시스템 (Claw Empire 스타일)


## 0) 30초 긴급 복구 (파일 없다고 뜰 때)

에러가 `can't open file ...run_demo.py`이면, **명령 문제가 아니라 현재 폴더에 파일이 없는 상태**입니다.

아래 4줄을 먼저 그대로 실행하세요 (PowerShell):

```powershell
pwd
git remote -v
git branch
python -c "from pathlib import Path; print('run_demo.py=',Path('run_demo.py').exists()); print('scripts/run_demo.py=',Path('scripts/run_demo.py').exists()); print('scripts/auto_bootstrap.py=',Path('scripts/auto_bootstrap.py').exists())"
```

- 셋 다 `False`면: 지금 로컬 폴더가 우리가 안내한 코드 상태가 아닙니다.
- 이 경우 **fresh 폴더 재클론이 최단 경로**입니다:

```powershell
cd C:\work
git clone https://github.com/GreenSheep01201/claw-empire.git claw-empire-fresh
cd claw-empire-fresh
python .\scripts\auto_bootstrap.py --goal "신규 가습마스크 브랜드 런칭"
```

> 핵심: 같은 명령을 반복해도 파일이 없으면 절대 실행되지 않습니다. 먼저 파일 존재 여부를 확인해야 합니다.

---


### 0-2) 방금 보내주신 상태 해석 (main 브랜치)

아래 상태면 원인 99%는 **브랜치/커밋 불일치**입니다.

- `git remote -v`는 정상
- `git branch`가 `main`
- 그런데 `run_demo.py`, `scripts/run_demo.py`, `scripts/auto_bootstrap.py`가 없음

즉, 현재 로컬 `main`에는 데모 실행 파일 변경이 아직 없습니다.

즉시 복구 명령:

```powershell
cd C:\work\claw-empire
git pull origin main
python -c "from pathlib import Path; print(Path('run_demo.py').exists(), Path('scripts/run_demo.py').exists(), Path('scripts/auto_bootstrap.py').exists())"
```

- 결과가 여전히 `False False False`면: 이 기능은 아직 `main`에 머지되지 않은 상태입니다.
- 이 경우에는 해당 기능이 포함된 브랜치를 체크아웃해서 실행해야 합니다.

```powershell
# 예시: 기능 브랜치가 있다면
git fetch --all
git branch -a
# origin/<feature-branch> 확인 후
git checkout -b ai-demo origin/<feature-branch>
python .\scripts\auto_bootstrap.py --goal "신규 가습마스크 브랜드 런칭"
```

> 참고: PowerShell에서 긴 명령이 중간에 끊기면 출력이 안 보일 수 있습니다. 위 한 줄을 그대로 복붙하세요.

---


### 0-3) 지금 당신 출력값 기준 "정답 명령" (origin/dev 존재)

당신이 보낸 결과:
- `main` 최신
- `run_demo.py`, `scripts/run_demo.py`, `scripts/auto_bootstrap.py` 모두 `False`
- `remotes/origin/dev` 존재

=> 즉, 실행 파일은 `main`이 아니라 `dev` 쪽에 있습니다. 아래 **그대로** 실행하세요.

```powershell
cd C:\work\claw-empire
git checkout dev
git pull origin dev
python -c "from pathlib import Path; print(Path('run_demo.py').exists(), Path('scripts/run_demo.py').exists(), Path('scripts/auto_bootstrap.py').exists())"
python .\scripts\auto_bootstrap.py --goal "신규 가습마스크 브랜드 런칭"
```

위 4번째 줄이 `True`를 포함하면 정상입니다.

> 만약 `git checkout dev`에서 로컬 변경 충돌이 나면:
> `git stash -u` → `git checkout dev` → `git pull origin dev` 순서로 진행하세요.

---

### 0-4) `git ls-tree`가 둘 다 빈 출력이면 (지금 상황)

당신이 방금 보낸 것처럼 아래 두 명령이 아무것도 안 나오면,

```powershell
git ls-tree -r --name-only origin/main | findstr /i "run_demo.py auto_bootstrap.py"
git ls-tree -r --name-only origin/dev  | findstr /i "run_demo.py auto_bootstrap.py"
```

의미는 하나입니다: **원격 main/dev 어디에도 해당 파일이 존재하지 않습니다.**

즉, 지금 저장소는 `run_demo.py` 방식이 아니라 원래 저장소의 실행 방식(프론트/서버)으로 실행해야 합니다.

바로 다음 단계:

```powershell
cd C:\work\claw-empire
corepack enable
pnpm install
pnpm dev
```

`pnpm`이 없거나 막히면:

```powershell
npm install
npm run dev
```

그리고 서버가 따로 필요한 구조면(현재 폴더에 `server` 디렉터리 존재):

```powershell
cd .\server
npm install
npm run dev
```

> 요약: 지금은 파일이 없어서 막힌 게 맞고, 당신 잘못이 아닙니다. 이 저장소는 Node 실행 경로로 가야 합니다.

---

### 0-5) "CLI 설치" 버튼이 비활성화일 때 (지금 질문)

이 경우는 보통 아래 3가지입니다.

1. 브라우저 UI 권한만 있고, 실제 호스트 머신에 CLI 설치 권한이 없음
2. CLI 자동설치 기능이 꺼진 배포 모드
3. 설치 대상 바이너리(node/pnpm/codex 등) 미설치

먼저 진단:

```powershell
python .\scripts\doctor.py
```

다음으로 수동 설치(Windows PowerShell):

```powershell
# Node 계열
winget install OpenJS.NodeJS.LTS
npm install -g pnpm

# 예시: Codex CLI
npm install -g @openai/codex
```

설치 후:

```powershell
where node
where npm
where pnpm
where codex
```

그 다음 웹 UI에서:
1) Settings > CLI Tools > Refresh
2) Agent 클릭 > CLI Tool을 방금 설치한 항목으로 지정
3) 다시 Office 화면에서 Connected 숫자 증가 확인

> 핵심: 버튼이 비활성화면 UI에서 설치 못 합니다. 서버/PC 터미널에서 수동 설치 후 Refresh해야 합니다.

---

### 0-6) CLI가 Installed인데 Offline일 때 (화면처럼 `Not Authenticated`)

지금 화면 상태는 원인이 명확합니다.

- Codex CLI: `Installed`
- Codex CLI: `Not Authenticated`
- 우상단: `Offline`
- 좌하단: `Disconnected`

즉, 설치는 되었지만 **CLI 로그인(인증)이 안 끝나서** 에이전트가 연결되지 않은 상태입니다.

해결 순서(Windows PowerShell):

```powershell
# 1) Codex CLI 로그인
codex login

# 2) 로그인 상태 확인
codex whoami

# 3) 앱 재시작 또는 Settings > CLI Tools > Refresh
```

그 다음 UI에서 꼭 할 것:

1) Settings > API에서 OpenAI 키 저장 확인
2) Office 화면에서 에이전트 클릭
3) 각 에이전트의 CLI Tool을 `Codex CLI`로 지정
4) 모델(provider/model) 지정 후 저장
5) 좌하단 `Disconnected`가 `Connected`로 바뀌는지 확인

`codex login`이 막히면:

```powershell
codex logout
codex login
```

> 핵심: `Installed`만으로는 부족하고, `Authenticated` 상태가 되어야 Online/Connected로 올라옵니다.

---

### 0-7) API Test가 `origin_not_allowed`일 때 + Codex 토큰 이슈

지금 에러(`origin_not_allowed`)는 **키 자체가 틀린 에러가 아니라, 해당 API 키의 사용 출처(Origin/IP/Project 제한) 정책에 걸린 상태**입니다.

#### A. `origin_not_allowed` 해결 순서

1. OpenAI 콘솔에서 현재 키의 제한 정책 확인
   - Allowed origins / Referrer 제한
   - Project 제한(다른 프로젝트 키를 넣었는지)
   - Organization/Project 매핑
2. 가장 빠른 검증용으로 **제한 없는 새 테스트 키**를 발급
3. 앱 Settings > API에서 기존 provider를 Edit
   - Base URL: `https://api.openai.com/v1`
   - Key 교체 후 Save
4. 앱/서버 재시작 후 Test 재실행

PowerShell에서 키 자체 체크(앱 바깥 검증):

```powershell
$env:OPENAI_API_KEY="sk-..."
curl https://api.openai.com/v1/models -H "Authorization: Bearer $env:OPENAI_API_KEY"
```

- 여기서도 실패하면 키/프로젝트 제한 문제입니다.
- 여기서는 성공하는데 앱에서만 실패하면 앱 요청 Origin 제한 문제입니다.

#### B. Codex `whoami`에서 토큰이 쓰이는 이유

`codex whoami`도 내부적으로 Codex 세션/모델을 통해 실행되어 **입출력 토큰이 집계**됩니다.
- `cached` 토큰은 할인/캐시 경로로 처리될 수 있지만 사용량 표시는 됩니다.
- 완전 무과금 확인이 필요하면 API 호출 없는 로컬 명령(`where`, `echo`)로 점검하세요.

#### C. 아직 Disconnected일 때 마지막 확인

1. Settings > CLI Tools: Codex가 `Installed + Authenticated`인지
2. Settings > API: Test가 성공하는 provider 1개 이상인지
3. Agent별로 CLI Tool=Codex, Provider=OpenAI를 지정했는지
4. 서버 로그에 `/api/cli-status`, `/api/agents` 200 응답이 뜨는지

> 요약: 지금 막힘의 1순위는 `origin_not_allowed`(키 정책)이며, 이게 풀려야 Connected가 안정적으로 올라옵니다.

---

### 0-8) 새 키로도 `origin_not_allowed` + 저장이 안 될 때

이 케이스는 보통 **키 자체 문제 + 앱 저장 플로우 문제**가 섞여 있습니다.

#### A. 저장이 안 될 때 UI 순서

1. 기존 provider에서 `Edit` 대신 `+ Add`로 새 provider를 추가
2. 새 provider 이름을 다르게 지정 (예: `openai-new`)
3. Base URL: `https://api.openai.com/v1`
4. 키 붙여넣기 후 Save
5. 기존 provider는 `Disable`만 하고 즉시 삭제하지 않기
6. 브라우저 강력 새로고침(Ctrl+F5) 후 `Refresh`

#### B. 앱 밖에서 키 자체 진단 (중요)

```powershell
$env:OPENAI_API_KEY="sk-..."
python .\scripts\api_probe.py
python .\scripts\api_probe.py --origin http://localhost:8000
```

- 둘 다 성공: 키 정상, 앱 쪽 origin/저장 로직 이슈
- 첫 번째 실패: 키/프로젝트/조직 제한 이슈
- 두 번째만 `origin_not_allowed`: Origin 제한 정책 이슈

#### C. 앱 서버 쪽 점검

- 서버 allowed origins에 `http://localhost:8000` / `http://127.0.0.1:8000` 포함
- API 서버 재시작 후 Settings > API > Test 재실행
- 여전히 실패하면 새 provider로 교체한 뒤 Agent 매핑을 새 provider로 변경

> 핵심: `origin_not_allowed`는 대부분 키 오타가 아니라 정책 제한/Origin 검증 문제입니다.

---

## 0-1) 자동 실행 (파일이 있을 때)

```powershell
python .\scripts\auto_bootstrap.py --goal "신규 가습마스크 브랜드 런칭"
```

`run_demo.py` → `scripts/run_demo.py` → `npm run demo` 순서로 자동 시도합니다.

---

이 저장소는 여러 역할의 AI 봇이 협업하여 다음 업무를 자동화/반자동화하도록 설계된 **멀티 에이전트 운영 시스템**입니다.

- 시장조사
- SNS 게시글 기획/관리
- 쇼핑스토어 운영
- 신제품 개발 검토
- 브랜딩 전략
- 광고 집행 기획
- 디자이너 브리프 생성

## 1) 먼저 오해부터 정리

- `C:\work\game`, `/workspace/game` 같은 경로는 **예시 경로**입니다.
- 이미 해당 폴더를 만들어둬야 하는 게 아니라, **원하는 위치에 새로 클론**하면 됩니다.
- GitHub 웹에서 실행하는 게 아니라 **내 PC 터미널(PowerShell)**에서 실행합니다.

---

## 2) 진짜 처음부터 (Windows PowerShell 기준)

### 2-1. 작업할 폴더 하나 만들기

```powershell
mkdir C:\work
cd C:\work
```

### 2-2. GitHub에서 코드 내려받기

```powershell
git clone https://github.com/GreenSheep01201/claw-empire.git
cd claw-empire
```

> 폴더 이름은 `claw-empire`가 기본이고, 원하면 다른 이름으로 받아도 됩니다.

### 2-3. "여기가 맞는 폴더인가" 확인

```powershell
Get-ChildItem
```

아래 파일/폴더가 보이면 맞습니다.

- `README.md`
- `scripts`
- `src`
- `package.json`

### 2-4. Python 설치 확인

```powershell
python --version
```

`Python 3.10+`가 보이면 OK.

---

## 3) 실행 방법 A (가장 쉬움, PowerShell)

```powershell
$env:PYTHONPATH = "src"
python run_demo.py --goal "신규 가습마스크 브랜드 런칭"
# 또는
python .\scripts\run_demo.py --goal "신규 가습마스크 브랜드 런칭"
```

결과는 콘솔에 출력되고 기본적으로 `docs/sample_report.json`에 저장됩니다.

---

## 4) 실행 방법 B (PowerShell 전용 스크립트)

```powershell
.\scripts\run_demo.ps1 -Goal "신규 가습마스크 브랜드 런칭"
```

저장 위치 지정:

```powershell
.\scripts\run_demo.ps1 -Goal "신규 뷰티 브랜드 런칭" -Save "docs\my_report.json"
```

---

## 5) 실행 방법 C (Node 사용자용)

> Node로 실행해도 내부적으로 Python 스크립트를 호출합니다.

```powershell
npm run demo
```

목표/저장경로 같이 넘기기:

```powershell
npm run demo -- --goal "신규 뷰티 브랜드 런칭" --save "docs/my_report.json"
```

---

## 6) 경로 지정이 헷갈릴 때 핵심 규칙

### A. `cd` 경로

- `cd`는 "이 저장소를 클론한 폴더"로 들어가면 됩니다.
- 예: `C:\work\claw-empire`

### B. `--save` 경로

- 상대경로: 현재 위치 기준
  - `--save "docs\my_report.json"`
- 절대경로: PC의 정확한 위치
  - `--save "C:\work\output\report.json"`

예시:

```powershell
python scripts/run_demo.py --goal "테스트" --save "C:\work\output\report.json"
```

---

## 7) 자주 묻는 질문

### Q1. 저런 경로를 만든 적이 없는데?
정상입니다. 그건 예시 경로였고, 지금부터 원하는 위치(`C:\work` 등)에 폴더 만들고 `git clone` 하면 됩니다.

### Q2. 파워셸에서 입력하면 돼?
네. PowerShell에서 그대로 입력하면 됩니다.

### Q3. GitHub에서 실행하는 거야?
아니요. GitHub는 코드 저장소이고 실행은 로컬 PC에서 합니다.

### Q4. Node만 쓰던 사람도 가능?
가능합니다. `npm run demo`로 시작하면 됩니다.


### Q5. Python 3.12인데 괜찮아?
네. 이 프로젝트는 `requires-python = ">=3.10"`이라 Python 3.12도 지원 범위입니다.

### Q6. `can't open file ... scripts\run_demo.py` 에러가 나와요
이 에러는 Python 버전 문제가 아니라 **현재 위치에 `scripts/run_demo.py`가 없다는 뜻**입니다.

아래 순서로 확인해 주세요.

```powershell
# 1) 현재 위치 확인
pwd

# 2) 현재 폴더에 scripts가 있는지 확인
Get-ChildItem

# 3) scripts 폴더 안에 run_demo.py가 있는지 확인
Get-ChildItem .\scripts
```

`run_demo.py`가 안 보이면 보통 아래 둘 중 하나입니다.

1) 잘못된 폴더에 들어와 있음
```powershell
cd C:\work\claw-empire
```

2) 저장소를 아직 안 받았거나, 다른 이름으로 클론함
```powershell
cd C:\work
git clone https://github.com/GreenSheep01201/claw-empire.git
cd claw-empire
```

그 다음 다시 실행:

```powershell
$env:PYTHONPATH = "src"
python run_demo.py --goal "신규 가습마스크 브랜드 런칭"
# 또는
python .\scripts\run_demo.py --goal "신규 가습마스크 브랜드 런칭"
```



### Q7. 그럼 처음부터 다시하면 돼?
네, 가장 빠른 해결은 **작업 폴더 하나 새로 만들어서 다시 클론 후 실행**하는 겁니다.

```powershell
cd C:\work
# (선택) 기존 폴더가 꼬였으면 이름 변경/삭제
# Rename-Item .\claw-empire claw-empire-old

git clone https://github.com/GreenSheep01201/claw-empire.git
cd claw-empire

python --version
$env:PYTHONPATH = "src"
python run_demo.py --goal "신규 가습마스크 브랜드 런칭"
# 또는
python .\scripts\run_demo.py --goal "신규 가습마스크 브랜드 런칭"
```

위 순서로 하면 경로 꼬임 문제를 거의 100% 피할 수 있습니다.



### Q8. 계속 같은 에러가 나면 (60초 점검)
아래 4개를 PowerShell에 그대로 입력해 주세요.

```powershell
pwd
Get-ChildItem
Test-Path .\scripts\run_demo.py
git remote -v
```

- `Test-Path`가 `False`면: 현재 폴더가 잘못됐거나, 다른 저장소입니다.
- 이 경우 아래처럼 **새 폴더로 재클론**하는 게 가장 빠릅니다.

```powershell
cd C:\work
git clone https://github.com/GreenSheep01201/claw-empire.git claw-empire-fresh
cd claw-empire-fresh
python run_demo.py --goal "신규 가습마스크 브랜드 런칭"
```

`python run_demo.py`는 루트 실행 파일이라 `PYTHONPATH`를 직접 안 넣어도 동작하도록 구성되어 있습니다.



### Q9. `run_demo.py`가 아예 없는데요?
정상일 수 있습니다. 저장소마다 엔트리포인트 이름이 다릅니다.

그래서 아래 명령으로 자동 탐지 실행하세요.

```powershell
python .\scripts\auto_bootstrap.py --goal "신규 가습마스크 브랜드 런칭"
```

이 스크립트는 순서대로 `run_demo.py` → `scripts/run_demo.py` → `npm run demo`를 자동 시도합니다.

### Q10. auto_bootstrap.py도 없다고 나오면?
그 경우는 현재 폴더가 우리가 수정한 코드가 있는 루트가 아닐 가능성이 큽니다.
먼저 아래로 확인하세요.

```powershell
python .\scripts\doctor.py
```

`doctor.py`까지 없으면, 현재 로컬 폴더가 다른 브랜치/다른 저장소 상태입니다.
그때는 `git remote -v`, `git branch`, `git pull` 결과를 확인한 뒤 다시 실행하세요.

---

## 8) 시스템 구조

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
