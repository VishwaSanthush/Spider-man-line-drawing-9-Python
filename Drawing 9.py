import turtle

turtle.bgcolor('black')

p=turtle.Turtle()

wn = turtle.Screen()

p.pencolor('red')

p.hideturtle()
p.speed(900)

#curve01

def curve01(a,d):

    for i in range(d):

        p.right(a)

        p.forward(1)



#making eye

p.width(15)

p.penup()

p.right(90)

p.forward(85)

p.left(90)

p.forward(35)

p.pendown()

p.fillcolor('white')

p.begin_fill()

p.left(55)

curve01(0.09,100)

curve01(0.2,100)

p.forward(70)

p.right(90)

curve01(0.5,100)

curve01(00,30)

curve01(0.3,50)

curve01(0.6,50)

p.forward(50)

p.right(47)

curve01(0.1,95)

p.end_fill()



#changing

p.penup()

p.left(36)

p.forward(70)

p.pendown()



#curve02

def curve02(a,d):

    for i in range(d):

        p.left(a)

        p.forward(1)



#second eye

p.fillcolor('white')

p.begin_fill()

p.right(55)

curve02(0.09,100)

curve02(0.2,100)

p.forward(70)

p.left(90)

curve02(0.5,100)

curve02(00,30)

curve02(0.3,50)

curve02(0.6,50)

p.forward(50)

p.left(47)

curve02(0.1,95)

p.end_fill()



p.penup()

p.width(0)

p.right(49)

p.forward(30)

p.left(102)  #100.40

p.forward(145)

p.pencolor('red')





#making left face

p.fillcolor('red')

p.begin_fill()

p.speed(0)

p.pendown()

p.left(90)

curve01(5,20)

p.left(175)

p.forward(50)

p.left(25)

p.forward(28)

p.right(160)

p.forward(170)

curve02(0.2,65)

p.right(60)

curve01(0.1,140)

curve01(0.5,50)

p.left(180)

curve02(0.2,150)

curve02(0.1,95)

p.left(127)

p.forward(5)

curve01(2,20)

p.right(30)

p.forward(90)

p.right(7)

p.forward(75)

p.right(160)

p.forward(100)

curve02(0.1,105)

p.right(70)

curve01(0.2,200)

curve01(0.3,70)

p.left(175)

curve02(0.2,150)

curve02(0.3,150)

p.forward(20)

p.left(65)

curve01(0.1,120)

curve01(0.010,105)

p.right(10)

curve01(0.2,110)

p.right(60)

curve01(0.3,138)

p.right(30)

curve01(0.2,160)

p.left(150)

curve02(0.2,100)

curve02(0.1,150)

p.forward(70)

curve02(0.4,40)

p.left(160)

curve01(0.1,60)

p.left(7)

curve01(0.1,120)

curve01(0.2,30)

p.forward(20)

p.right(140)

curve02(0.2,40)

p.right(50)

curve02(0.2,70)

p.right(8)

curve02(0.1,70)

curve02(0.5,50)

p.left(153)

curve01(0.1,170)

p.right(81)

curve02(0.2,20)

p.right(3)

curve02(0.1,62)

p.right(153) #..

curve01(0.1,63) 

p.left(50)

curve02(0.1,175)

p.left(60)

p.forward(7)

p.end_fill()





#going to replicate

p.left(92.15)

p.penup()

p.forward(417)

p.pendown()



p.fillcolor('red')

p.begin_fill()

#right face 

p.right(90)

curve02(5,20)

p.right(175)

p.forward(50)

p.right(25)

p.forward(28)

p.left(160)

p.forward(170)

curve01(0.2,65)

p.left(60)

curve02(0.1,140)

curve02(0.5,50)

p.right(180)

curve01(0.2,150)

curve01(0.1,95)

p.right(127)

p.forward(5)

curve02(2,20)

p.left(30)

p.forward(90)

p.left(7)

p.forward(75)

p.left(160)

p.forward(100)

curve01(0.1,105)

p.left(70)

curve02(0.2,200)

curve02(0.3,70)

p.right(175)

curve01(0.2,150)

curve01(0.3,150)

p.forward(20)

p.right(65)

curve02(0.1,120)

curve02(0.010,105)

p.left(10)

curve02(0.2,110)

p.left(60)

curve02(0.3,138)

p.left(30)

curve02(0.2,160)

p.right(150)

curve01(0.2,100)

curve01(0.1,150)

p.forward(70)

curve01(0.4,40)

p.right(160)

curve02(0.1,60)

p.right(7)

curve02(0.1,120)

curve02(0.2,30)

p.forward(20)

p.left(140)

curve01(0.2,40)

p.left(50)

curve01(0.2,70)

p.left(8)

curve01(0.1,70)

curve01(0.5,50)

p.right(153)

curve02(0.1,170)

p.left(81)

curve01(0.2,20)

p.left(3)

curve01(0.1,62)

p.left(153) #..

curve02(0.1,63) 

p.right(50)

curve01(0.1,100)  #0.1

p.forward(75)

p.right(75)

p.forward(2)

p.end_fill()

turtle.done()
