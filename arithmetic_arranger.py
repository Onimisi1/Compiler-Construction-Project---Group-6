

def arithmetic_arranger(problems, answer=False):

    if len(problems) > 5:
        return "Error: Too many problems"

    arranger = []
    for problem in problems:
        part = problem.split()
        operand1 = part[0]
        operator = part[1]
        operand2 = part[2]
        calc_answer = ''

        if operator != '+' and operator != '-':
            return "Error: Operator must be '+' or '-' "

        if not operand1.isdigit() or not operand2.isdigit():
            return "Error: Numbers must only contain digits"

        if len(operand1) > 4 or len(operand2) > 4:
            return "Error: Numbers cannot be more than four digits"

        if answer:
            if operator == '+':
                calc_answer = str(int(operand1) + int(operand2))
            elif operator == '-':
                calc_answer = str(int(operand1) - int(operand2))

        width = max(len(operand1), len(operand2)) + 2

        arranger.append([operand1.rjust(width), operator + operand2.rjust(width - 1), '-' * width])

        if answer:
            calc_answer = calc_answer.rjust(width)
            arranger[-1].append(calc_answer)

    f_output = ''
    for i in range(len(arranger[0])):
        f_output += "   ".join(arranger[j][i] for j in range(len(arranger))) + "\n"

    return  f_output.rstrip()


print(arithmetic_arranger(problems=['250 + 30', '600 - 32', '500 + 25', '450 - 30', '300 + 3003'],
                          answer=True))
