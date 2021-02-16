# tkinterのインポート
import tkinter as tk
import tkinter.ttk as ttk

# rootフレームの設定
root = tk.Tk()
root.title("文字列の取得・セット・クリア")
root.geometry("200x100")

# フレームの作成と設置
frame = ttk.Frame(root)
frame.grid(column=0, row=0, sticky=tk.NSEW, padx=5, pady=10)

# 各種ウィジェットの作成
label = ttk.Label(frame, text="誕生日：")
entry = ttk.Entry(frame)
button_execute = ttk.Button(frame, text="実行", command=birthday)

# 各種ウィジェットの設置
label.grid(row=0, column=0)
entry.grid(row=0, column=1)
button_execute.grid(row=1, column=1)

root.mainloop()
