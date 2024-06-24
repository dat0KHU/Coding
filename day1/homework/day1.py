from turtle import *

#we're making a house
speed(30)
width(5)
color("blue")
forward(200)
left(90)

forward(200)
left(90)

forward(200)
left(90)

forward(200)
left(90)

#end of square😁

#making a door

forward(70)

color("red")
begin_fill()
left(90) 
forward(120) #HEIGHT
right(90)
forward(60)
right(90)
forward(120)
end_fill()

#end of door😁

#making a roof

penup()
goto(200, 200)
pendown()

color("yellow")
begin_fill()
right(150)
forward(200)
left(120)
forward(200)
end_fill()

#end of a roof

#making left window

color("blue")
begin_fill()
penup()
goto(15, 100)
pendown()
left(120)
forward(40)
left(90)
forward(40)
left(90)
forward(40)
left(90)
forward(40)
end_fill()

#making right window

begin_fill()
penup()
goto(145, 100)
pendown()
left(90)
forward(40)
left(90)
forward(40)
left(90)
forward(40)
left(90)
forward(40)
end_fill()

exitonclick()