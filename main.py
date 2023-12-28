#!/usr/bin/python3.10
# -*- coding: utf8 -*-

import sys
sys.path.append('./venv3.10/lib/python3.10/site-packages/')
import requests
import json
import os


CHECK_URL = 'https://misskey.the-menz.com/'
if len(sys.argv) >= 2:
    DISCORD_TOKEN = sys.argv[1]

elif os.path.isfile('DISCORD_TOKEN'):
    with open('DISCORD_TOKEN', 'r') as f:
        DISCORD_TOKEN = f.read().splitlines()[0]

def main():
    r = requests.get(CHECK_URL)
    if r.status_code != 200:
        discord()

def discord():
    headers = {'content-type': 'application/json'}
    data = json.dumps({
        'username'   : '死活くん',
        'content'    : '**' + 'おほ！死んでるゼ、こいつ！' + '** : ' + CHECK_URL,
        })
    result = requests.post('https://discord.com/api/webhooks/' + DISCORD_TOKEN, data, headers=headers)
    print(result)

if __name__ == "__main__":
    main()

