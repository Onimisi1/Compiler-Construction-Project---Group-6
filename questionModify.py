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
    Question(questions_prompts[0], 'A'),
    Question(questions_prompts[1], 'C'),
    Question(questions_prompts[2], 'C'),
    Question(questions_prompts[3], 'C'),
    Question(questions_prompts[4], 'B')
]


def run_test(tests):
    score = 0
    for test in tests:
        answer = ''
        while answer not in ['A', 'B', 'C', 'D']:
            answer = input(test.prompt).upper()
            if answer not in ['A', 'B', 'C', 'D']:
                print('Please choose a valid option\n')
        if answer == test.answer:
            score += 1
        time.sleep(1)
        print('\n'*5)
    print('You got ' + str(score) + '/' + str(len(tests)), 'correct.')


run_test(questions)
print('LOADING ANSWERS TO THE QUESTIONS...')
time.sleep(3)
for question in questions:
    print(question.answer + '.')
