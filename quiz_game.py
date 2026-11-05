
from quiz_data import create_default_quizzes


class QuizGame:
    def __init__(self):
        # 기본 퀴즈 5문제 불러오기
        self.quizzes = create_default_quizzes()

        # 아직 최고 점수가 없는 상태
        self.best_score = None

    def play_quiz(self):
        # 등록된 퀴즈가 없는 경우
        if not self.quizzes:
            print("⚠️ 등록된 퀴즈가 없습니다.")
            return

        score = 0
        total = len(self.quizzes)

        print(f"\n📝 퀴즈를 시작합니다! 총 {total}문제")

        # 저장된 퀴즈를 하나씩 출제
        for index, quiz in enumerate(self.quizzes, start=1):
            print(f"\n[문제 {index}/{total}]")
            quiz.display()

            # 정답 입력
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

                print("⚠️ 1~4 사이의 숫자를 입력해주세요.")

            # 정답 확인
            if quiz.check_answer(answer):
                print("✅ 정답입니다!")
                score += 1
            else:
                print(f"❌ 오답입니다! 정답은 {quiz.answer}번입니다.")

        # 최종 점수 계산
        percentage = round(score / total * 100)

        print("\n" + "=" * 40)
        print(f"🏆 결과: {total}문제 중 {score}문제 정답!")
        print(f"📊 점수: {percentage}점")
        print("=" * 40)

        # 최고 점수 갱신
        if self.best_score is None or percentage > self.best_score:
            self.best_score = percentage
            print("🎉 새로운 최고 점수입니다!")
