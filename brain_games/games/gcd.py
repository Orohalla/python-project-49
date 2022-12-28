#!/usr/bin/env python3
import random
import math

TASK = 'Find the greatest common divisor of given numbers.'


def get_round():
    number1 = random.randint(1, 100)
    number2 = random.randint(1, 100)
    text_question = f'{number1} {number2}'
    answer = math.gcd(number1, number2)
    correct_answer = f'{answer}'
    return text_question, correct_answer
