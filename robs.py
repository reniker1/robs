#!/usr/bin/python3

import random

def display_random_color():
    colors = ['白', '黒', '赤']
    for i in range(1, 4):
        random_color = random.choice(colors)
        print(f'{i}回目のランダムな色: {random_color}')

if __name__ == "__main__":
    display_random_color()
