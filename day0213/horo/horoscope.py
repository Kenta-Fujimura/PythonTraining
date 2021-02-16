import tkinter as tk
index = 0
zodiac = [
    ["山羊座", 12, 22,0],
    ["水瓶座", 1, 20,1],
    ["魚座", 2, 19,2],
    ["牡羊座", 3, 21,3],
    ["牡牛座", 4, 20,4],
    ["双子座", 5, 21,5],
    ["蟹座", 6, 22,6],
    ["獅子座", 7, 23,7],
    ["乙女座", 8, 23,8],
    ["天秤座", 9, 23,9],
    ["蠍座", 10, 24,10],
    ["射手座", 11, 23,11]
    ]

def bt_click():
    moon = s1.get()
    day = s2.get()
    global index

    for i in range(len(zodiac)):
        if zodiac[i][1] == int(moon):
            if zodiac[i][2] <= int(day):
                result = f"{zodiac[i][0]}です"
                x = int(zodiac[i][3])
                break
            else:
                result = f"{zodiac[i-1][0]}です"
                x= int(zodiac[i-1][3])
                break

    result = (f'あなたの誕生日{moon}月{day}日\n') + result
    label3['text']=result
    canvas.delete('p1')
    canvas.create_image(100,100,image=photos[x],tag='p1')

root=tk.Tk()
root.title('Horoscope') # windowタイトルを設定
root.geometry('400x650') #windowの大きさを設定
root.configure(bg='pink')

label1=tk.Label(root,text='誕生月',font=('Arial',20),bg='pink')
label1.pack(padx=50, pady=5,anchor=tk.W,fill='x')
s1 = tk.Spinbox(root, from_ = 1, to = 12, increment = 1, width = 10,font=('Arial',20))
s1.pack(padx=50,pady=5,anchor=tk.W,fill='x')

label2=tk.Label(root,text='誕生日',font=('Arial',20),bg='pink')
label2.pack(padx=50, pady=5,anchor=tk.W,fill='x')
s2 = tk.Spinbox(root, from_ = 1, to = 31, increment = 1, width = 10,font=('Arial',20))
s2.pack(padx=50,pady=5,anchor=tk.W,fill='x')

btn=tk.Button(root,text='占う',font=('Arial',20),command=bt_click)
btn.pack(padx=50,pady=40,anchor=tk.W,fill='x')

label3=tk.Label(root,text='',font=('Arial',20),bg='pink')
label3.pack(padx=5, pady=5,anchor=tk.W,fill='x')

canvas=tk.Canvas(root,width=200,height=200,bd=0, highlightthickness=0, relief='ridge')
canvas.pack(pady=20)

photos=[
	tk.PhotoImage(file='s01.png'),
	tk.PhotoImage(file='s02.png'),
	tk.PhotoImage(file='s03.png'),
	tk.PhotoImage(file='s04.png'),
	tk.PhotoImage(file='s05.png'),
	tk.PhotoImage(file='s06.png'),
	tk.PhotoImage(file='s07.png'),
	tk.PhotoImage(file='s08.png'),
	tk.PhotoImage(file='s09.png'),
	tk.PhotoImage(file='s10.png'),
	tk.PhotoImage(file='s11.png'),
	tk.PhotoImage(file='s12.png'),
]

canvas.create_image(100,100,image=photos[index],tag='p1')
root.mainloop()

