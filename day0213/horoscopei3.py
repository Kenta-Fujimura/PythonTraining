#スクロールバーの使い方
import tkinter as tk

#ウインド画面の作成
root=tk.Tk()
root.title("スクロールバーの使い方")

#フレームの作成
#フレーム1(上側：リストボックスを格納する)
frame=tk.Frame()
frame.grid(row=0,sticky="we")
#フレーム２（下側：ボタンを格納する）
frame_button=tk.Frame()
frame_button.grid(row=1,sticky="we")


#データ（リストボックスに表示させる）
list_value=tk.StringVar()
list_value.set(["Aさん","Bさん","Cさん","Dさん","Eさん","Fさん","Gさん","Hさん","Iさん","Jさん","Kさん","Lさん"])

#リストボックスの作成
#selectmodeの種類(single:1つだけ選択できる、multiple:複数選択できる、extended：複数選択可能＋ドラッグでも選択可能)
listbox=tk.Listbox(frame,height=8,listvariable=list_value,selectmode="single")
listbox.pack()


#テキストの作成
text_str=tk.StringVar()
text_str.set("ボタンを押して下さい")
text=tk.Label(frame_button,textvariable=text_str)
text.grid(row=0,columnspan=3)

#ボタンを押したら選択している人を表示する
def check():
    text_check=listbox.curselection()
    text_str.set(listbox.get(text_check))

#全選択する
def all_select():
    listbox.select_set(0,tk.END)

#全クリアする
def all_clear():
    listbox.select_clear(0,tk.END)
    
#ボタンの作成
Button=tk.Button(frame_button,text="判定",command=check)
Button.grid(row=1,column=0)

Button_allselect=tk.Button(frame_button,text="全選択",command=all_select)
Button_allselect.grid(row=1,column=1)

Button_allclear=tk.Button(frame_button,text="全クリア",command= all_clear)
Button_allclear.grid(row=1,column=2)


#画面の表示
root.mainloop()
