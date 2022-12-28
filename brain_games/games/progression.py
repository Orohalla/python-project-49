#!/usr/bin/env python3
import random

TASK = 'What number is missing in the progression?'


def get_round():
    step = random.randint(2, 5)
    delete_number = random.randint(0, 9)
    start = random.randint(1, 10)
    fisrt = [i for i in range(1, 100, step)]
    second = fisrt[start:]
    last = [str(i) for i in second[:10]]
    correct_answer = last[delete_number]
    last[delete_number] = '..'
    text_question = ' '.join(last)
    return text_question, correct_answer
