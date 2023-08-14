import time

students_pass = ['p1', 'p2', 'p3', 'p4', 'p5']


class Candidate:
    def __init__(self, name, details):
        self.name = name
        self.details = details
        self.votes = 0

    def vote_calc(self):
        self.votes += 1

    def __str__(self):
        return f'Aspirant: {self.name} \nVotes: {self.votes}'


candidates_details = ['Olalegacy - President\nY or N: ', 'M.T.O - Gen.Sec\nY or N: ', 'Premier - Senator\nY or N: ',
                      'Elitech - President\nY or N: ']

candidates = [
    Candidate(candidates_details[0].split()[0], candidates_details[0]),
    Candidate(candidates_details[1].split()[0], candidates_details[1]),
    Candidate(candidates_details[2].split()[0], candidates_details[2]),
    Candidate(candidates_details[3].split()[0], candidates_details[3]),
]

while True:

    if len(students_pass) == 0:
        print('Poll is now closed.Loading results...')
        time.sleep(5)
        for candidate in candidates:
            print(candidate)
            print('\n')
        break

    passkey = ''

    while passkey not in students_pass:
        passkey = input('Please input your pass: ').lower()
        print('Loading...')
        time.sleep(2)
        if passkey not in students_pass:
            print('You have either voted already or incorrect passkey!')
            print('\n')

    print('You are eligible to vote. Please choose "Y" or "N" to vote for a Candidate of your choice for the '
          'respective office.\n')

    students_pass.remove(passkey)

    for candidate in candidates:
        choice = ''
        while choice != 'Y' and choice != 'N':
            choice = input(candidate.details).upper()
            if choice != 'Y' and choice != 'N':
                print('Please make sure your vote is valid!\n')
        if choice == 'Y':
            candidate.vote_calc()
            print('\n')
        elif choice == 'N':
            pass
            print('\n')
    print('You have successfully casted your vote. Have a nice day.\n')
    print('\n'*10)
    time.sleep(5)
