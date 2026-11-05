
from quiz import Quiz


def create_default_quizzes():
    quizzes = [
        Quiz(
            "Python에서 화면에 내용을 출력하는 함수는?",
            ["input()", "print()", "len()", "type()"],
            2
        ),
        Quiz(
            "Python에서 사용자 입력을 받는 함수는?",
            ["print()", "int()", "input()", "str()"],
            3
        ),
        Quiz(
            "다음 중 Python의 리스트를 나타내는 것은?",
            ["(1, 2, 3)", "{1, 2, 3}", "[1, 2, 3]", '"1, 2, 3"'],
            3
        ),
        Quiz(
            "Python에서 조건문을 작성할 때 사용하는 키워드는?",
            ["for", "while", "def", "if"],
            4
        ),
        Quiz(
            "Python에서 반복문에 사용하는 키워드는?",
            ["return", "class", "for", "import"],
            3
        )
    ]

    return quizzes
