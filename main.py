
from quiz_game import QuizGame


def show_menu():
    print("\n" + "=" * 40)
    print("       🎯 Python 퀴즈 게임 🎯")
    print("=" * 40)
    print("1. 퀴즈 풀기")
    print("2. 퀴즈 추가")
    print("3. 퀴즈 목록")
    print("4. 점수 확인")
    print("5. 종료")
    print("=" * 40)


def get_menu_choice():
    while True:
        choice = input("메뉴 선택 (1-5): ").strip()

        if not choice:
            print("⚠️ 번호를 입력해주세요.")
            continue

        try:
            number = int(choice)
        except ValueError:
            print("⚠️ 숫자를 입력해주세요.")
            continue

        if 1 <= number <= 5:
            return number

        print("⚠️ 1~5 사이의 번호를 입력해주세요.")


def main():
    game = QuizGame()

    print("🎮 퀴즈 게임에 오신 것을 환영합니다!")

    try:
        while True:
            show_menu()
            choice = get_menu_choice()

            if choice == 1:
                game.play_quiz()

            elif choice == 2:
                game.add_quiz()

            elif choice == 3:
                game.show_quiz_list()

            elif choice == 4:
                game.show_best_score()

            elif choice == 5:
                print("👋 게임을 종료합니다.")
                break

    except (KeyboardInterrupt, EOFError):
        print("\n⚠️ 입력이 중단되어 안전하게 종료합니다.")


if __name__ == "__main__":
    main()
