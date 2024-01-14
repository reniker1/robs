# SPDX-FileCopyrightText: 2024 Ren Imai
# SPDX-License-Identifier: BSD-3-Clause
#!/usr/bin/python3

import random

def display_random_outfit(season):
    colors = ['白', '黒', '赤']
    head_colors = ['無', '白', '黒']

    print(f'{season}のコーディネート:')

    for part in ['頭', '上半身', '下半身', '靴']:
        if part == '頭':
            random_color = random.choice(head_colors)
        else:
            random_color = random.choice(colors)
        print(f'{part}のランダムな色: {random_color}')

    random_style = random.choice(['カジュアル', 'スポーツ', 'ストリート'])
    print(f'ランダムな系統: {random_style}')

if __name__ == "__main__":
    season = input("季節を入力してください（春、夏、秋、冬）: ")
    display_random_outfit(season)
