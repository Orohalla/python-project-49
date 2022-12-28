#!/usr/bin/env python3
import random

TASK = 'What is the result of the expression?'


def get_round():
    number1 = random.randint(1, 25)
    number2 = random.randint(1, 25)
    symbol = random.choice('+-*')
    text_question = f'{number1} {symbol} {number2}'
    if symbol == '+':
        correct_answer = f'{number1 + number2}'
    elif symbol == '-':
        correct_answer = f'{number1 - number2}'
    else:
        correct_answer = f'{number1 * number2}'
    return text_question, correct_answer
