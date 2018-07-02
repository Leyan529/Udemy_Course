import turtle
import time

t = turtle.Pen()
t.color("green")
t.speed(10)
#turtle.speed(speed)	画笔绘制的速度范围[0,10]整数

def 上() :
    t.heading()
    t.left(90)
    t.forward(50)

def 下() :
    t.heading()
    t.right(90)
    t.forward(50)

def 小畫家():
    while(True):
        key = input("")
        if ord(key) == 119:
            print("上")
            上()
        if ord(key) == 115:
            print("下")
            下()
        if ord(key) == 100:
            print("右")
        if ord(key) == 97:
            print("左")
        print(ord(key))

def 三角形():
    a = 60
    turtle.forward(a)
    turtle.left(120)
    turtle.forward(a)
    turtle.left(120)
    turtle.forward(a)
    turtle.left(120)
    time.sleep(2.5)

def partice():
    t.up()
    t.goto(-100,100)
    print("Start Point")
    t.down()
    t.forward(50)
    print("straight 50")

    t.up()
    t.goto(-100,100)
    t.forward(25)
    t.left(90)
    t.down()
    t.forward(25)
    t.right(180)
    t.forward(50)
    print(str(t.pos()))
    time.sleep(2.5)

def loopTurtle():
    for i in range(0,8):
        t.forward(50)
        t.left(45)
    t.reset()

    for i in range(1,38):
        t.forward(100)
        t.left(175)
    t.reset()

    for i in range(1,20):
        t.forward(100)
        t.left(95)

def loop():
    for i in range(1,20):
        t.forward(100)
        t.left(95)
    t.up()  #up() : 畫筆離開繪製區塊，不再繪製

def updown():
    for i in range(0,6):
        t.down()   #down() : 畫筆回到繪製區塊
        loop()
        t.right(90*i)
        t.forward(150)

def 車身():
    # t.color("blue")
    t.color(0.1, 0.5, 1)  # color(R,G,B) or color("color name")  R,G,B [0,1]
    t.begin_fill()  # begin_fill() : 準備填充繪製圖形顏色
    t.forward(150)
    t.left(90)
    t.forward(30)
    t.left(90)
    t.forward(40)
    t.right(90)
    t.forward(40)
    t.left(90)
    t.forward(70)
    t.left(90)
    t.forward(40)
    t.right(90)
    t.forward(40)
    t.left(90)
    t.forward(30)
    t.end_fill()  # end_fill()  : 填充繪製圖形顏色

def 車輪():
    t.color("black")
    t.begin_fill()
    t.circle(15)
    t.end_fill()

def colorTurtle():
    車身()
    t.up()
    t.right(270)
    t.forward(30)
    t.right(90)
    t.forward(2.5)
    t.down()
    車輪()
    t.up()
    t.right(270)
    t.forward(70)
    t.right(90)
    t.down()
    車輪()
    t.up()
    t.forward(100)

def square(side):
    for i in range(0,5):
        t.forward(int(side))
        t.left(90)
def circle(radius):
    t.circle(int(radius))














