from turtle import * 

#ეზო
speed(10)
penup()
goto(-1000,-350)
pendown()
color("green")
begin_fill()
forward(1950)
right(90)
forward(300)
right(90)
forward(1950)
  
#1 სახლი
end_fill()
color("red", "orange")
penup()
goto(-600,-350)
pendown()
begin_fill()
right(90)
forward(500)
right(90) 
forward(400)
right(90)
forward(500)
end_fill()
penup()
goto(-350,50)
pendown()

#ფანჯრები
width(6)
color("white")
fillcolor("black")
begin_fill()
left(90)
forward(90)
left(90)
forward(45)
left(90)
forward(90)
left(90)
forward(45)
 


penup()
goto(-450,50)
pendown()
right(90)
forward(90)
right(90)
forward(45)
right(90)
forward(90)
right(90)
forward(45)
end_fill()
penup()
goto(-200,150)

pendown()
 

color("red")
fillcolor("red")
begin_fill()
left(210)
forward(400)
left(120)
forward(400)
end_fill()
width(1)
color("red")
fillcolor("orange")
penup()
goto(-600,-350)
pendown()

penup()
goto(0,-350)
pendown()
begin_fill()
right(150)
forward(500)
right(90)
forward(400)
right(90)
forward(500)
end_fill()
width(6)
color("white")
fillcolor("black")
penup()
goto(150,50)
pendown()
begin_fill()
right(90)
forward(90)
right(90)
forward(45)
right(90)
forward(90)
right(90)
forward(45)
penup()
goto(250,50)
pendown()
left(90)
forward(90)
left(90)
forward(45)
left(90)
forward(90)
left(90)
forward(45)
end_fill()
width(1)
penup()
goto(400,150)
pendown()
color("red")
begin_fill()
right(150)
forward(400)
left(120)
forward(400)
end_fill()
penup()
goto(500,-350)
pendown()
color("red")
fillcolor("orange")
begin_fill()
right(150)
forward(500)
right(90)
forward(350)
right(90)
forward(500)
end_fill()
width(6)
penup()
goto( 550,50)
pendown()
color("white")
fillcolor("black")
begin_fill()
left(90)
forward(45)
left(90)
forward(45)
left(90)
forward(45)
left(90)
forward(45)
penup()
goto(750,50)
pendown()
right(90)
forward(45)
right(90)
forward(45)
right(90)
forward(45)
right(90)
forward(45)
end_fill()
width(1)
penup()
goto(850,150)
pendown()
color("red")
begin_fill()
right(150)
forward(350)
left(120)
forward(350)
end_fill()
color("red")
penup()
goto(-950,250)
pendown()
begin_fill()
left(180)

#მზე
for i in range(50):
    forward(300)
    left(172.5)
end_fill()
penup()
goto(-750,250)
pendown()
color("black")
fillcolor("blue")
begin_fill()
for i in range(5):
    forward(200)
    right(144)
 
penup()
goto(-200,250)
pendown()
 
for i in range(5):
    forward(200)
    right(144)
end_fill()





exitonclick()
done()