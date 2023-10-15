#!/usr/bin/python3
import math
from quiz_question import question_bank
from quiz_question import options

def correct_choice(option, answer):
    if option == answer:
        return True
    else:
        return False

def take_again(yes):
    if yes == 1:
        return True
    else:
        return False


while True:
    score = 0
    for question in range(len(question_bank)):
        print(" ")
        print("###############################################################")
        print(" ")
        print(f"{question + 1}. {question_bank[question]['text']}")
        for i in range(len(options[question])):
            print(options[question][i])
        choice = input("Enter the correct option(A/B/C/D).").upper()
        right_choice = correct_choice(choice, question_bank[question]['Answer'])

        if right_choice:
            score += 1
            print(f"Correct Answer")
        else:
            print(f"Incorrect Answer")
            print(f"The correct answer is {question_bank[question]['Answer']}")
        print(f"You got {score}/{question + 1} correctly.")
    print("")
    if score/len(question_bank)  >= 2.4/4:
        print(f"You passed the test.")
    else:
        print(f"You failed the test.")
    print(f"You answered {score} questions correctly.")
    print(f"Your overall score is {math.floor(score/len(question_bank) * 100)}%.")
    print("Want to take test again?")
    value = input("Press 1 for yes, press any other key to optout. ")
    if value != "1":
        break
