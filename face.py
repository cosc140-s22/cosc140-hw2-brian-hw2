#######################################################
#
# COSC 140 Homework 2, "face" problem
#
#######################################################
import turtle
# create a grid of 500x500, origin at lower left
turtle.setworldcoordinates(0,0,500,500)
turtle.bgcolor("black")
franklin = turtle.Turtle()
franklin.speed("fastest")
# draw a blue square
franklin.penup() # pull pen up, next moves won't draw anything
def popcorn1():
  countx = 50
  county = 300
  while (True):
    franklin.goto(countx,county)
    franklin.pendown()
    franklin.color('yellow')
    franklin.begin_fill()
    franklin.setheading(0)
    franklin.circle(30)
    franklin.end_fill()
    franklin.penup()
    countx+=35
    county+=10
    if (countx>200):
      break
def popcorn2():
  count2x = 200
  count2y = 350
  while (True):
    franklin.goto(count2x,count2y)
    franklin.pendown()
    franklin.color('yellow')
    franklin.begin_fill()
    franklin.setheading(0)
    franklin.circle(30)
    franklin.end_fill()
    franklin.penup()
    count2x+=35
    count2y-=10
    if (count2x>400):
      break
popcorn1()
popcorn2()
franklin.pendown()
franklin.color('orange')
franklin.begin_fill()
franklin.right(120)
franklin.forward(300)
franklin.right(115)
franklin.forward(350)
franklin.end_fill()
franklin.penup()
franklin.goto(200,200)
franklin.pendown()

def popcorn3():
  count3x = 50
  count3y = 275
  while (True):
    franklin.goto(count3x,count3y)
    franklin.pendown()
    franklin.color('yellow')
    franklin.begin_fill()
    franklin.setheading(0)
    franklin.circle(30)
    franklin.end_fill()
    franklin.penup()
    count3x+=35
    count3y+=10
    if (count3x>200):
      break
def popcorn4():
  count4x = 200
  count4y = 300
  while (True):
    franklin.goto(count4x,count4y)
    franklin.pendown()
    franklin.color('yellow')
    franklin.begin_fill()
    franklin.setheading(0)
    franklin.circle(30)
    franklin.end_fill()
    franklin.penup()
    count4x+=35
    count4y-=10
    if (count4x>400):
      break
popcorn3()
popcorn4()
franklin.goto(200,130)
franklin.pendown()
franklin.pensize(10)
franklin.color('black')

franklin.circle(80,50)
franklin.pensize(5)
franklin.penup()
franklin.goto(165,220)
franklin.pendown()
franklin.color('white')
franklin.begin_fill()
franklin.circle(30)
franklin.end_fill()
franklin.color('black')
franklin.begin_fill()
franklin.circle(20)
franklin.end_fill()
franklin.penup()


franklin.goto(300,220)
franklin.pendown()
franklin.color('white')
franklin.begin_fill()
franklin.circle(30)
franklin.end_fill()
franklin.color('black')
franklin.begin_fill()
franklin.circle(20)
franklin.end_fill()


turtle.done()