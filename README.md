# sikatu_kun
手っ取り早く作った死活監視スクリプト、もう早く酒飲んで寝たいんだよ！
それでも書かなきゃREADME！酒で脳が腐ってるからな！

# インストール
いつものやつ
```
$ python3.10 -m venv venv3.10
$ source venv3.10/bin/activate
$ pip install -r requirements.txt
```

# 使い方
引数にトークン書きたくない場合はDISCORD_TOKENってファイルにトークン書いておけば良い、引数無い時は勝手に読んでくれる
```
$ ./main.py [ディスコのAPIトークン]
```

あとはcronにでもブチ込んでおけば良いじゃろ
