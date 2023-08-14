import datetime
import time
today = datetime.date.today()
print(today)
print(time.ctime(time.time()))


class Question:
    def __init__(self, prompt, answer):
        self.prompt = prompt
        self.answer = answer


questions_prompts = [
    "1. The recent rainstorm did ……. To our farms.\nA. much damage\nB. many damages\nC. plenty damage\nD. many more "
    "damages.\nAnswer: ",
    "2.	My neighbour’s children always make …… when he is not at home\nA.	noises\nB.	Plenty noise\nC.	A lot of "
    "noise\nD.	A lot of noises.\nAnswer: ",
    "3. There is not ……… sense in what that politician has just said \nA. many\nB.lot of\nC. much\nD. more.\nAnswer: ",
    "4. The main objective of the library is all of these except………\nA. store book\nB. prevent it from getting "
    "stolen\nC. play with book\nD. read books\nAnswer: ",
    "5. We have received …… from him\nA. few information\nB. sufficient information\nC. an information\nD. some "
    "information.\nAnswer: "
]
questions = [
    Question(questions_prompts[0], 'a'),
    Question(questions_prompts[1], 'c'),
    Question(questions_prompts[2], 'c'),
    Question(questions_prompts[3], 'c'),
    Question(questions_prompts[4], 'b')
]


def run_test(tests):
    score = 0
    for test in tests:
        answer = input(test.prompt)
        if answer == test.answer:
            score += 1
    print('You got ' + str(score) + '/' + str(len(tests)), 'correct.')


run_test(questions)
print('ANSWERS TO THE QUESTIONS...')
for question in questions:
    print(question.answer + '.')
