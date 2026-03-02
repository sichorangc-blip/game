# AI 비즈니스 운영팀 시스템 (Claw Empire 스타일)


## 0) 제일 쉬운 자동 실행 (권장)

### 0-1) 파일 없어도 가능한 초진단

아래 명령은 **파일이 없어도** 실행됩니다.

```powershell
python -c "from pathlib import Path; import os; print('cwd=',Path.cwd()); print('run_demo.py=',(Path('run_demo.py').exists())); print('scripts/run_demo.py=',(Path('scripts/run_demo.py').exists())); print('scripts/auto_bootstrap.py=',(Path('scripts/auto_bootstrap.py').exists()))"
```

그리고 저장소 상태를 바로 확인하세요:

```powershell
git remote -v
git branch
git pull
Get-ChildItem
```

또는 이 프로젝트에 포함된 진단 스크립트:

```powershell
python .\scripts\doctor.py
```

아래 한 줄만 실행하면, 가능한 방식(Python/Node)을 자동으로 찾아 실행합니다.

```powershell
python .\scripts\auto_bootstrap.py --goal "신규 가습마스크 브랜드 런칭"
```

> 지금처럼 `run_demo.py`가 없다고 나오는 경우에도, 자동으로 `scripts/run_demo.py` 또는 `npm run demo`를 시도합니다.

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
