import tkinter as tk
def bt_click():
    t1 = int(txt1.get())
    t2 = int(txt2.get())
    dnum = t1 / t2
    pay = dnum // 100*100
    if dnum > pay:
        pay = int(pay + 100)
    
    payorg = t1 - pay * (t2 - 1)
    result = (f'1人あたり{int(pay)}円({t2-1}人)、幹事は{int(payorg)}円です')
    label2=tk.Label(root,text=result,font=('Arial',10),bg='skyblue')
    label2.pack(padx=5, pady=5,anchor=tk.W)



root=tk.Tk()
root.title('割り勘君My ') # windowタイトルを設定
root.geometry('400x600') #windowの大きさを設定
root.configure(bg='skyblue')
label=tk.Label(root,text='金額',font=('Arial',20),bg='skyblue')
label.pack(padx=5, pady=5,anchor=tk.W)
txt1 = tk.Entry(width=40,font=('Arial',20))
txt1.pack(padx=5, pady=5,anchor=tk.W)
label=tk.Label(root,text='人数',font=('Arial',20),bg='skyblue')
label.pack(padx=5, pady=5,anchor=tk.W)
txt2 = tk.Entry(width=40,font=('Arial',20))
txt2.pack(padx=5, pady=5,anchor=tk.W)
btn=tk.Button(root,text='計算する',font=('Arial',20),command=bt_click)
btn.pack(padx=5,pady=5,anchor=tk.W)

root.mainloop()

