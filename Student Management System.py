global class_list
class_list = {"mimi": '20/52HA118', "kizito": '19/52HA057', "favour": '19/52HA056', "teemy": '19/52HA100'}


def CSC_students():
    print('\n')
    1
    print("Enter 1 : To Add a Student")
    print("Enter 2 : To view Students List")
    print("Enter 3 : To search a Student")
    print("Enter 4 : To delete a Student\n")

    userInput = ''

    while userInput not in [1, 2, 3, 4]:
        try:
            userInput = int(input("Kindly enter your command: "))
            if userInput < 1 or userInput > 4:
                print('Please enter a valid option')
                print('\n')
        except:
            print("Please enter a valid command")
            print('\n')

    else:
        print("\n")

    if userInput == 1:
        stname = input("What is your name ? ")
        stnam = stname.lower()
        if stnam in class_list.keys():
            print("This Student already exist!")
        else:
            print('\n')
            matric_n = input("Enter your matric no: ")
            class_list[stnam] = matric_n
            print('\n')
            print("The below student has been added successfully\n")
            print(stname, class_list[stnam])


    elif userInput == 2:
            for name in class_list:
                print(name.upper())

    elif userInput == 3:
        stname = input("Enter name of student to search: ")
        stnam = stname.lower()
        if stnam in class_list:
            print(stnam.upper(),class_list[stnam])
        else:
            print(f"No Record of {stnam.upper()} found")

    elif userInput == 4:
        stname = input("Enter student name to delete: ")
        stnam = stname.lower()
        if stnam in class_list.keys():
            class_list.pop(stnam)
            print(stnam.upper() + ' successfully deleted.')
        else:
            print(f'{stnam.upper()} record not found.')


def runagain():
    runagain = input("Would you like to do something else ? Y/N ")
    return runagain.lower().startswith('y')


def rerun():
    runagain()


while True:
    CSC_students()
    if not runagain():
        break
