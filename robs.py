# SPDX-FileCopyrightText: 2024 Ren Imai
# SPDX-License-Identifier: BSD-3-Clause
#!/usr/bin/python3

import random

def display_random_color():
    category = ['カジュアル', 'スポーツ', 'ストリート']
    colors = ['白', '黒', '赤', 'グレー', 'ベージュ', '青', '緑', '紫', 'オレンジ']
    head_colors = ['無', 'ニット', 'キャップ', ]
    body_parts = ['帽子', 'ウェア', 'パンツ', 'シューズ']
    
    for i, part in enumerate(body_parts):
        if part == '帽子':
            random_color = random.choice(head_colors)
        else:
            random_color = random.choice(colors)
        print(f'{part}: {random_color}')

    random_category = random.choice(category)
    print(f'系統: {random_category}')

if __name__ == "__main__":
    display_random_color()
