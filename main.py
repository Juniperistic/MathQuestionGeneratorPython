#generate a number of math questions
#ask the user those questions
#don't allow them to move on until the question is answered correct
#time the total time it takes to complete all the questions

import random
import time

#constants so they do not change
OPERATORS = ["+", "-", "*"]
MIN_OPERAND = 3
MAX_OPERAND = 12
TOTAL_PROBLEMS = 10

def generate_problem():
    left = random.randint(MIN_OPERAND, MAX_OPERAND)
    right = random.randint(MIN_OPERAND, MAX_OPERAND)
    #random.choice - randomly picks an element from a list
    operator = random.choice(OPERATORS)

    expr = str(left) + " " + operator + " " + str(right)
    #eval() evaluates a string as if its a python expression
    answer = eval(expr)
    return expr, answer

wrong = 0
input("Press enter to start!")
print("---------------")

#gives time stamp in seconds
start_time = time.time()

for i in range(TOTAL_PROBLEMS):
    expr, answer = generate_problem()
    while True:
        guess = input("Problem #" + str(i + 1) + ": " + expr + " = ")
        if guess == str(answer):
            break
        wrong += 1

end_time = time.time()
#round - it rounds the number to the nearest 2 digits since 2 is entered in command
total_time = round(end_time - start_time, 2)

print("---------------")
print("Nice Work! You finished in", total_time, "seconds!")