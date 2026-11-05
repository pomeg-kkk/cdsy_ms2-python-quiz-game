
# 🎯 Python 콘솔 퀴즈 게임

## 1. 프로젝트 개요

Python 기본 문법과 객체 지향 프로그래밍을 학습하기 위해 제작한 콘솔 기반 퀴즈 게임입니다.

사용자는 퀴즈를 풀거나 새로운 문제를 등록할 수 있으며,
프로그램을 종료해도 JSON 파일을 통해 퀴즈와 최고 점수가 유지됩니다.

## 2. 퀴즈 주제 및 선정 이유

### 주제
Python 기초 문법

### 선정 이유
Python 프로그래밍의 핵심 개념인 변수, 자료형, 조건문, 반복문, 함수 등을 복습하고,
퀴즈를 통해 학습 내용을 확인하기 위해 선정했습니다.

## 3. 개발 환경

- Python 3.10 이상
- Ubuntu (WSL)
- Visual Studio Code
- Git
- GitHub

외부 라이브러리 없이 Python 표준 라이브러리만 사용했습니다.

## 4. 실행 방법

### 저장소 복제

```bash
git clone https://github.com/pomeg-kkk/cdsy_ms2-python-quiz-game.git
```

### 프로젝트 폴더 이동

```bash
cd cdsy_ms2-python-quiz-game
```

### 프로그램 실행

```bash
python3 main.py
```

## 5. 주요 기능

| 기능 | 설명 |
|------|------|
| 퀴즈 풀기 | 등록된 퀴즈를 풀고 점수를 계산합니다. |
| 퀴즈 추가 | 문제, 선택지 4개, 정답 번호를 입력해 새 퀴즈를 등록합니다. |
| 퀴즈 목록 | 등록된 모든 문제의 목록을 확인합니다. |
| 점수 확인 | 최고 점수와 정답 기록을 확인합니다. |
| JSON 저장 | 퀴즈와 최고 점수를 state.json에 저장합니다. |
| 예외 처리 | 잘못된 입력과 파일 오류를 처리합니다. |
| 종료 | 프로그램 데이터를 저장하고 종료합니다. |

## 6. 프로젝트 파일 구조

```text
python-quiz-game/
├── main.py
├── quiz.py
├── quiz_game.py
├── quiz_data.py
├── state.json
├── README.md
├── .gitignore
└── docs/
    └── screenshots/
```

### 파일 설명

- main.py: 메인 메뉴와 프로그램 실행
- quiz.py: 개별 퀴즈를 관리하는 Quiz 클래스
- quiz_game.py: 게임 진행과 저장 기능을 관리하는 QuizGame 클래스
- quiz_data.py: 기본 Python 퀴즈 5문제
- state.json: 퀴즈 데이터와 최고 점수 저장
- README.md: 프로젝트 설명 및 실행 방법
- .gitignore: Git 추적 제외 파일 설정

## 7. 데이터 저장 방식

프로젝트 루트의 state.json 파일에 UTF-8 인코딩으로 데이터를 저장합니다.

### 데이터 구조 예시

```json
{
  "quizzes": [
    {
      "question": "Python에서 화면에 내용을 출력하는 함수는?",
      "choices": ["input()", "print()", "len()", "type()"],
      "answer": 2
    }
  ],
  "best_score": 80,
  "best_correct": 4,
  "best_total": 5
}
```

### 필드 설명

- quizzes: 등록된 퀴즈 목록
- question: 문제 내용
- choices: 4개의 선택지
- answer: 정답 번호(1~4)
- best_score: 최고 점수(0~100점)
- best_correct: 최고 점수 기록의 정답 개수
- best_total: 최고 점수 기록의 전체 문제 수

파일이 없는 경우 기본 문제 5개를 생성합니다.

파일이 손상된 경우 오류를 처리하고 기본 데이터로 복구합니다.

## 8. 사용한 Python 개념

- 변수와 자료형
- 조건문(if, elif, else)
- 반복문(for, while)
- 함수와 반환값
- 클래스와 객체
- 파일 입출력
- JSON 데이터 처리
- try/except 예외 처리

## 9. Git 활용

프로젝트 개발 과정에서 Git을 사용하여 변경 이력을 관리했습니다.

- 기능 단위 커밋
- feature/quiz-play 브랜치 생성
- main 브랜치 병합
- GitHub 원격 저장소 Push
- git clone 및 git pull 실습

## 10. 향후 개선 사항

- 랜덤 문제 출제
- 문제 수 선택
- 힌트 기능
- 퀴즈 삭제
- 점수 기록 히스토리

## 11. 실행 화면

프로그램 실행 화면은 docs/screenshots 폴더에 추가할 예정입니다.
```
