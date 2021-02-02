import turtle
t=turtle.Turtle()
t.shape('turtle')

for _ in range(5)
t.forward(100) # 向いている方向に100移動
t.right(135) # 90度右回転
t.forward(100)

t.right(135) # 90度右回転
t.forward(100)
t.right(135) # 90度右回転
t.forward(100)
t.home() # 原点に移動し、デフォルトの方向を向く（右)
turtle.mainloop()
