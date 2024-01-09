#!/usr/bin/python3

import random
import string

def generate_random_string(length):
    # ランダムな文字列を生成する関数
    letters = string.ascii_letters + string.digits  # 英字と数字を使用します
    return ''.join(random.choice(letters) for i in range(length))

def generate_random_email(domain='example.com'):
    # ランダムなメールアドレスを生成する関数
    username_length = random.randint(5, 12)  # ユーザー名の長さをランダムに選択
    username = generate_random_string(username_length)
    email = f'{username}@{domain}'
    return email

if __name__ == "__main__":
    random_email = generate_random_email()
    print(f"Random Email Address: {random_email}")
