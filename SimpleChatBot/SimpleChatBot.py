def greet(bot_name, birth_year):
    print(f"Hello! My name is {bot_name}.")
    print(f"I was created in {birth_year}.")

def remind_name():
    print("Please, remind me your name")
    name = input()
    print(f"What a great name you have, {name}!")

def guess_age():
    print("Let me guess your age.")
    print("Enter remainders of dividing your age by 3, 5 and 7.")

    rem3 = int(input())
    rem5 = int(input())
    rem7 = int(input())
    age = ((rem3 * 70) + (rem5 * 21) + (rem7 * 15)) % 105

    print(f"Your age is {age}; that's a good time to start programming!")

def count():
    print("Now I will prove that I can count to any number you want.")

    cnt = int(input())
    for i in range(cnt + 1):
        print(i)

def test():
    print("Let's test your programming knowledge.")
    print("Why do we use methods?")
    print("""
    1. To repeat a statement multiple times.
    2. To decompose a program into several small subroutines.
    3. To determine the execution time of a program.
    4. To interrupt the execution of a program.""")

    answer = int(input())
    while answer != 2:
        if answer == 2:
            print("Completed, have a nice day!")
            break
        else:
            print("Please, try again.")
            answer = int(input())

greet("Aid", "2020")
remind_name()
guess_age()
count()
test()
print("Congratulations, have a nice day!")
print("whole lotta gang shit")