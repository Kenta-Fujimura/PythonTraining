import tkinter as tk
def btn_click():
	txt=entry.get()
	btn['text']=txt
root=tk.Tk()
root.title('My Window')
root.geometry('400x200')
label=tk.Label(root,text='金額',font=('Arial',10))
entry=tk.Entry(width=20)
label.place(x=0,y=0,side='top')
entry.place(x=10,y=10,side='top')
btn=tk.Button(text='文字列の取得',command=btn_click)
#btn.place(x=20,y=100,side='top')
root.mainloop()
