from turtle import *
import random

def generate_color():
    return f"#{random.randint(0, 0xFFFFFF):06x}"

def playing_area():
    pen = Turtle()
    pen.ht()
    pen.speed(0)
    pen.color('light blue')
    pen.begin_fill()
    pen.goto(-240,240)
    pen.goto(240,240)
    pen.goto(240,-240)
    pen.goto(-240,-240)
    pen.goto(-240,240)
    pen.end_fill()
    
class Head(Turtle):
  def __init__(self, screen):
    super().__init__()
    self.ht()
    self.speed(0)
    self.color(generate_color())
    self.penup()
    self.setheading(90)
    self.shape("square")
    self.direction = "up"
    self.alive = True
    self.speed(2)
    self.st()
    screen.onkeypress(self.left, "Left")
    screen.onkeypress(self.right, "Right")
    screen.onkeypress(self.up, "Up")
    screen.onkeypress(self.down, "Down")

  def up(self):
    if self.direction != "down":
      self.speed(0)
      self.setheading(90)
      self.direction = "up"
      self.speed(2)

  def down(self):
    if self.direction != "up":
      self.speed(0)
      self.setheading(270)  
      self.direction = "down"
      self.speed(2)

  def left(self):
    if self.direction != "right":
      self.speed(0)
      self.setheading(180)
      self.direction = "left"
      self.speed(2)

  def right(self):
    if self.direction != "left":
      self.speed(0)
      self.setheading(0)
      self.direction = "right"
      self.speed(2)
  
  def move(self):
    self.forward(20)
    if self.xcor() == 240:
      self.die()
    elif self.xcor() == -240:
      self.die()
    elif self.ycor() == -240:
      self.die()
    elif self.ycor() == 240:
      self.die()
    
  def die(self):
    self.speed(0)
    self.alive = False
    self.ht()


class Segment(Turtle):
  def __init__(self, other):
    super().__init__()
    self.ht()
    self.speed(0)
    self.penup()
    self.shape("circle")
    self.color("blue")
    self.goto(other.position())
    self.speed(2)
    self.st()

  def move(self, other):
    self.speed(0)
    self.goto(other.position())
    self.speed(2)
  
  def die(self):
    self.speed(0)
    self.alive = False
    self.ht()


class Apple(Turtle):
  def __init__(self):
    super().__init__()
    self.ht()
    self.speed(0)
    self.color("red")
    self.penup()
    self.goto(random.randint(-230,230),random.randint(-230,230))
    self.shape("circle")
    self.st()

  def relocate(self):
    self.ht()
    self.goto(random.randint(-230,230),random.randint(-230,230))
    self.st()
  
def update():
  if head.alive:
    head.move()
    if head.distance(apple) < 20:
      body.append(Segment(body[-1]))
      apple.relocate()
    for i in range(len(body)-1,0,-1):
      body[i].move(body[i-1])
    for i in range(3,len(body)):
      if head.distance(body[i]) < 20:
        head.die()
        for i in range(1,len(body)):
          body[i].die()
        
  screen.ontimer(update, 120)

screen = Screen()
screen.bgcolor("black")
screen.setup()
# Key Binding. Connects key presses and mouse clicks with function calls
screen.listen()
screen.onkey(update,"space")

playing_area()
head = Head(screen)
apple = Apple()
body = [head]


screen.exitonclick()






screen.exitonclick()