#!/usr/bin/env python3
import random

TASK = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def get_round():
    number = random.randint(1, 100)
    text_question = f'{number}'
    counter = 0
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            counter = counter + 1
    if number < 2:
        correct_answer = 'no'
    elif counter == 0:
        correct_answer = 'yes'
    else:
        correct_answer = 'no'
    return text_question, correct_answer
