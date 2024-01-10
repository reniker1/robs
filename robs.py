#!/usr/bin/python3

import random

def display_random_color():
    colors = ['白', '黒', '赤', '黄', 'ベージュ', '緑', '茶', '紺', '青', 'オレンジ', '紫']
    occasions = ['帽子', '上半身', '下半身' '靴'] 
    for i in range(4):
        random_color = random.choice(colors)
        print(f'{occasions[i]}: {random_color}')

if __name__ == "__main__":
    display_random_color()
