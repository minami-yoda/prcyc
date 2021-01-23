# coding: UTF-8
import random
import tkinter as tk

# ラベルの文字をおみくじでランダムに出たものに変更する関数
def displabel():
    kuji = ["大吉","中吉","小吉"]
    lbl.configure(text=random.choice(kuzi))

#画面作る
root = tk.Tk()
#!/usr/bin/env python3
# coding=utf-8

# サイズ決定
root.geometry("200×100")

# ラベル作成
lbl = tk.Label(text="今日の運勢は？")
# ボタン作成 commandで押した時に関数実行
btn = tk.Button(text="PUSH", command = displabel)

# 画面にラベルとボタン配置
lbl.pack()
btn.pack()

# 作ったウィンドウ表示する
tk.mainloop
