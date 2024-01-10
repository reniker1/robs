#!/usr/bin/python3

import random

def display_random_color():
    colors = ['白', '黒', '赤']
    occasions = ['頭', '上半身', '下半身']
    for i in range(3):
        random_color = random.choice(colors)
        print(f'{occasions[i]}のランダムな色: {random_color}')

if __name__ == "__main__":
    display_random_color()
