"""Unit test cases for hangman game."""
import unittest
import app as hangman


class HangmanTestCase(unittest.TestCase):

    # def setUp(self):
    #

    # checkCorrectAnswer(correctLetters, secretWord)
    def test_checkCorrectAnswer(self):
        answer = hangman.checkCorrectAnswer("baon", "baboon")
        self.assertTrue(answer)  # assertTrue는 TestCase에서 계승된 함수이다. answer가 true가 아니면 에러 반환

    def test_checkWrongAnswer(self):
        answer = hangman.checkWrongAnswer("zebrio", "zebra")
        self.assertTrue(answer)

    def test_1(self):
        answer = hangman.checkCorrectAnswer("bazn", "baboon")
        self.assertFalse(answer) # assertTrue의 반대. answer가 false가 아니면 에러 반환

    def test_2(self):
        answer = hangman.checkCorrectAnswer("", " ")
        self.assertFalse(answer)

    def test_3(self):
        answer = hangman.checkCorrectAnswer("ZEBRA", "zebra")
        self.assertFalse(answer)
'''
파이썬 파일은 실행될 때마다 **__name__**이라는 특별한 변수를 자동으로 생성해요.
이 파일이 직접 실행되면 → __name__은 "__main__"이 돼요.
하지만 다른 파일에서 import되면 → __name__은 파일 이름("test_hangman" 등)이 돼요.
'''
if __name__ == "__main__":   # 이 파일이 직접 실행된 경우에만 아래 코드를 실행해라
    unittest.main()          # unittest.main()은 unittest 모듈의 내장 함수예요. 위에서 정의한 HangmanTestCase 클래스의 모든 test_로 시작하는 함수들을 자동 실행해요. 결과를 콘솔에 예쁘게 출력해줍니다 (통과/실패 여부 등).
