
import json
from pathlib import Path

from quiz import Quiz
from quiz_data import create_default_quizzes


# 프로젝트 루트에 state.json 저장
STATE_FILE = Path(__file__).resolve().parent / "state.json"


class QuizGame:
    def __init__(self):
        self.quizzes = []
        self.best_score = None
        self.best_correct = 0
        self.best_total = 0

        self.load_data()

    # 데이터 저장
    def save_data(self):
        data = {
            "quizzes": [
                {
                    "question": quiz.question,
                    "choices": quiz.choices,
                    "answer": quiz.answer
                }
                for quiz in self.quizzes
            ],
            "best_score": self.best_score,
            "best_correct": self.best_correct,
            "best_total": self.best_total
        }

        temp_file = STATE_FILE.with_suffix(".json.tmp")

        try:
            with open(temp_file, "w", encoding="utf-8") as file:
                json.dump(
                    data,
                    file,
                    ensure_ascii=False,
                    indent=4
                )

            temp_file.replace(STATE_FILE)
            print("💾 데이터가 저장되었습니다.")
            return True

        except OSError as error:
            print(f"⚠️ 데이터 저장 실패: {error}")
            return False

    # 데이터 불러오기
    def load_data(self):
        if not STATE_FILE.exists():
            print("📂 기본 퀴즈 데이터를 불러옵니다.")
            self.quizzes = create_default_quizzes()
            self.save_data()
            return

        try:
            with open(STATE_FILE, "r", encoding="utf-8") as file:
                data = json.load(file)

            if not isinstance(data, dict):
                raise ValueError("데이터 형식이 올바르지 않습니다.")

            quiz_data = data["quizzes"]

            if not isinstance(quiz_data, list):
                raise ValueError("퀴즈 목록 형식이 잘못되었습니다.")

            loaded_quizzes = []

            for item in quiz_data:
                if not isinstance(item, dict):
                    raise ValueError("퀴즈 데이터가 잘못되었습니다.")

                question = item["question"]
                choices = item["choices"]
                answer = item["answer"]

                if not isinstance(question, str) or not question.strip():
                    raise ValueError("문제 내용이 잘못되었습니다.")

                if (
                    not isinstance(choices, list)
                    or len(choices) != 4
                    or not all(
                        isinstance(c, str) and c.strip()
                        for c in choices
                    )
                ):
                    raise ValueError("선택지는 문자열 4개여야 합니다.")

                if type(answer) is not int or not 1 <= answer <= 4:
                    raise ValueError("정답은 1~4 사이여야 합니다.")

                loaded_quizzes.append(
                    Quiz(question, choices, answer)
                )

            best_score = data["best_score"]
            best_correct = data["best_correct"]
            best_total = data["best_total"]

            if best_score is not None:
                if (
                    type(best_score) is not int
                    or not 0 <= best_score <= 100
                ):
                    raise ValueError("최고 점수가 잘못되었습니다.")

            if (
                type(best_correct) is not int
                or type(best_total) is not int
                or best_correct < 0
                or best_total < 0
                or best_correct > best_total
            ):
                raise ValueError("점수 기록이 잘못되었습니다.")

            if best_score is None:
                if best_correct != 0 or best_total != 0:
                    raise ValueError("점수 기록이 일치하지 않습니다.")
            elif best_total == 0:
                raise ValueError("최고 점수의 문제 수가 잘못되었습니다.")
            elif round(best_correct / best_total * 100) != best_score:
                raise ValueError("최고 점수 계산이 일치하지 않습니다.")

            self.quizzes = loaded_quizzes
            self.best_score = best_score
            self.best_correct = best_correct
            self.best_total = best_total

            print(
                f"📂 저장된 데이터 불러오기 완료! "
                f"(퀴즈 {len(self.quizzes)}개)"
            )

        except (
            OSError,
            UnicodeError,
            json.JSONDecodeError,
            ValueError,
            KeyError,
            TypeError
        ) as error:
            print(f"⚠️ 데이터 파일 오류: {error}")
            print("📂 기본 퀴즈 데이터로 복구합니다.")

            self.quizzes = create_default_quizzes()
            self.best_score = None
            self.best_correct = 0
            self.best_total = 0

            # 손상된 파일을 보존하고 기본 데이터로 복구
            backup_file = STATE_FILE.with_name("state.json.broken")

            try:
                if STATE_FILE.exists():
                    STATE_FILE.replace(backup_file)
                    print(f"📁 손상 파일 백업: {backup_file.name}")
            except OSError as backup_error:
                print(f"⚠️ 백업 실패: {backup_error}")
                print("기존 파일을 덮어쓰지 않습니다.")
                return

            self.save_data()

    # 퀴즈 풀기
    def play_quiz(self):
        if not self.quizzes:
            print("⚠️ 등록된 퀴즈가 없습니다.")
            return

        score = 0
        total = len(self.quizzes)

        print(f"\n📝 퀴즈 시작! 총 {total}문제")

        for index, quiz in enumerate(self.quizzes, start=1):
            print(f"\n[문제 {index}/{total}]")
            quiz.display()

            while True:
                user_input = input("정답 입력 (1-4): ").strip()

                if not user_input:
                    print("⚠️ 정답 번호를 입력해주세요.")
                    continue

                try:
                    answer = int(user_input)
                except ValueError:
                    print("⚠️ 숫자를 입력해주세요.")
                    continue

                if 1 <= answer <= 4:
                    break

                print("⚠️ 1~4 사이의 번호를 입력해주세요.")

            if quiz.check_answer(answer):
                print("✅ 정답입니다!")
                score += 1
            else:
                print(f"❌ 오답입니다! 정답은 {quiz.answer}번입니다.")

        percentage = round(score / total * 100)

        print("\n" + "=" * 40)
        print(f"🏆 결과: {total}문제 중 {score}문제 정답!")
        print(f"📊 점수: {percentage}점")
        print("=" * 40)

        if self.best_score is None or percentage > self.best_score:
            self.best_score = percentage
            self.best_correct = score
            self.best_total = total

            print("🎉 새로운 최고 점수입니다!")
            self.save_data()

    # 퀴즈 추가
    def add_quiz(self):
        print("\n📌 새로운 퀴즈를 추가합니다.")

        while True:
            question = input("문제를 입력하세요: ").strip()

            if question:
                break

            print("⚠️ 문제를 비워둘 수 없습니다.")

        choices = []

        for i in range(1, 5):
            while True:
                choice = input(f"선택지 {i}: ").strip()

                if choice:
                    choices.append(choice)
                    break

                print("⚠️ 선택지를 비워둘 수 없습니다.")

        while True:
            user_input = input("정답 번호 (1-4): ").strip()

            if not user_input:
                print("⚠️ 정답 번호를 입력해주세요.")
                continue

            try:
                answer = int(user_input)
            except ValueError:
                print("⚠️ 숫자를 입력해주세요.")
                continue

            if 1 <= answer <= 4:
                break

            print("⚠️ 1~4 사이의 번호를 입력해주세요.")

        new_quiz = Quiz(question, choices, answer)
        self.quizzes.append(new_quiz)

        print("✅ 새로운 퀴즈가 추가되었습니다!")
        print(f"📚 총 퀴즈: {len(self.quizzes)}개")

        self.save_data()

    # 퀴즈 목록
    def show_quiz_list(self):
        print("\n📋 등록된 퀴즈 목록")

        if not self.quizzes:
            print("⚠️ 등록된 퀴즈가 없습니다.")
            return

        print(f"총 {len(self.quizzes)}개")
        print("-" * 40)

        for index, quiz in enumerate(self.quizzes, start=1):
            print(f"[{index}] {quiz.question}")

        print("-" * 40)

    # 최고 점수 확인
    def show_best_score(self):
        print("\n🏆 최고 점수 확인")
        print("-" * 40)

        if self.best_score is None:
            print("아직 퀴즈를 플레이한 기록이 없습니다.")
        else:
            print(f"최고 점수: {self.best_score}점")
            print(
                f"정답 기록: {self.best_total}문제 중 "
                f"{self.best_correct}문제 정답"
            )

        print("-" * 40)
