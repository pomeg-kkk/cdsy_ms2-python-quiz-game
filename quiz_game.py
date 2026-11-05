
from quiz import Quiz
from quiz_data import create_default_quizzes


class QuizGame:
    def __init__(self):
        self.quizzes = create_default_quizzes()
        self.best_score = None
        self.best_correct = 0
        self.best_total = 0

    # 퀴즈 풀기
    def play_quiz(self):
        if not self.quizzes:
            print("⚠️ 등록된 퀴즈가 없습니다.")
            return

        score = 0
        total = len(self.quizzes)

        print(f"\n📝 퀴즈를 시작합니다! 총 {total}문제")

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

        # 최고 점수 갱신
        if self.best_score is None or percentage > self.best_score:
            self.best_score = percentage
            self.best_correct = score
            self.best_total = total
            print("🎉 새로운 최고 점수입니다!")

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

        print("\n✅ 새로운 퀴즈가 추가되었습니다!")
        print(f"📚 현재 등록된 퀴즈: {len(self.quizzes)}개")

    # 퀴즈 목록 확인
    def show_quiz_list(self):
        print("\n📋 등록된 퀴즈 목록")

        if not self.quizzes:
            print("⚠️ 등록된 퀴즈가 없습니다.")
            return

        print(f"총 {len(self.quizzes)}개의 퀴즈가 있습니다.")
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
                f"정답 기록: "
                f"{self.best_total}문제 중 "
                f"{self.best_correct}문제 정답"
            )

        print("-" * 40)
