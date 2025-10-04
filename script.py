# I was playing with the basics I know about classes. And here's what I did
# The "math" library was never used in this code... yet

import math
import random

class System:
    def out():
        message = input("What message?\n")
        print(". . .")
        print(message)
    
    def calc():
        calc_type = input("What operation? + - * /\n")
        values = int(input("Value 1: \n")), int(input("Value 2: \n"))
        if calc_type == "+":
            print(values[0] + values[1])
        elif calc_type == "-":
            print(values[0] - values[1])
        elif calc_type == "*":
            print(values[0] * values[1])
        elif calc_type == "/":
            print(values[0] / values[1])

    def getRandom():
        range = int(input("Minimun number: ")), int(input("Maximum number: "))
        print(random.randint(range[0], range[1]))

    def piramid():
        start = 1
        amount = int(input("Enter the amount of lines:\n"))
        print(" - - - \n")
        while start <= amount:
            print("1" * start)
            start = start + 1
            

    def reverse_piramid():
        amount = int(input("Enter amount of lines:\n"))
        print(" - - - \n")
        while amount >= 1:
            print("1" * amount)
            amount = amount - 1

    def full_piramid():
        start = 1
        amount = int(input("Enter amount of lines (Remember that this function is doubled):\n"))
        print(" - - - ")
        while start <= amount:
            print("1" * start)
            start = start + 1
        while amount >= 1:
            print("1" * amount)
            amount = amount - 1
