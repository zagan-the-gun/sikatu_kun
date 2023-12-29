#!/usr/bin/python3.10
# -*- coding: utf8 -*-

import sys
sys.path.append('./venv3.10/lib/python3.10/site-packages/')
import requests
import json
import os


# ワンターレンに死亡確認されてたら、無駄なので全ての処理をしない
if os.path.isfile('WANG_DA_REN'):
    print('sibou kakunin!')
    sys.exit()

CHECK_URL = 'https://misskey.the-menz.com/'

if len(sys.argv) >= 2:
    DISCORD_TOKEN = sys.argv[1]
elif os.path.isfile('DISCORD_TOKEN'):
    with open('DISCORD_TOKEN', 'r') as f:
        DISCORD_TOKEN = f.read().splitlines()[0]
else:
    print('DISCORD_TOKEN not found')
    sys.exit(1)

def main():
    # 死活チェック
    r = requests.get(CHECK_URL)

    # ダメそうならディスコに発報
    if r.status_code != 500:
        discord()

def discord():
    headers = {'content-type': 'application/json'}
    data = json.dumps({
        'username'   : '死活くん',
        'content'    : '@everyone ' + '**' + 'おほ！死んでるゼ、こいつ！' + '** : ' + CHECK_URL,
        })
    result = requests.post('https://discord.com/api/webhooks/' + DISCORD_TOKEN, data, headers=headers)
    # 何度も発報しないように信頼と実績のワンターレンに死亡を確認して貰う
    if result.status_code == 204:
        with open('WANG_DA_REN', 'w') as f:
            # 空ファイルがあれば死亡確認なので書く必要はねーが、ちょっとしたチェック用にね？
            f.write(CHECK_URL)

    print(result)
    return result

if __name__ == "__main__":
    main()

