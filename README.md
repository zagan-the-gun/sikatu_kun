# sikatu_kun
手っ取り早く作った死活監視スクリプト、もう早く酒飲んで寝たいんだよ！  
それでも書かなきゃREADME！酒で脳が腐ってるからな！

# インストール
いつものやつ  
もうちょっと細かく書くと git clone して出来た sikatu_kun/ ディレクトリで以下を入力すれば良いのよ
```
$ python3.10 -m venv venv3.10
$ source venv3.10/bin/activate
(venv3.10)$ pip install -r requirements.txt
```

# 使い方
引数にトークン書きたくない場合はカレントディレクトリの DISCORD_TOKEN ってファイルにトークン書いておけば良い  
引数無い時は勝手に読んでくれる
```
$ source venv3.10/bin/activate
(venv3.10)$ ./main.py [ディスコのAPIトークン]
```

## 何度も発報しないために
一度発報すると WANG_DA_REN ってファイルをカレントディレクトリに作るよ  
こいつがある限り死活くんは何もしないで終了する、だってワンターレンが死亡確認してくれてるんだぜ？死んでるに決まってるさ！  
  
あとはcronにでもブチ込んでおけば良いじゃろ  
こんな感じ？
```
*/10 * * * * cd /home/[home directory]/sikatu_kun/; /home/[home directory]/sikatu_kun/venv3.10/bin/python3.10 /home/[home directory]/sikatu_kun/main.py >> /tmp/cron.log 2>&1
```
