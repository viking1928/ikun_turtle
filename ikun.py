from turtle import *
speed(11)
up()
goto(-200,-100)
down()
bgcolor('lavender')
pensize(5)
pencolor('black')
fillcolor('chocolate')
begin_fill()
circle(100,360+210)
end_fill()
lt(90)
circle(100,90)
rt(90)
circle(-100,90)
rt(90)
circle(100,90)
rt(90)
circle(-100,45)
rt(90)
fd(200)
up()
goto(-50,-20)
down()
seth(0)
fillcolor('yellow')
begin_fill()
circle(120)
end_fill()
up()
goto(-30,140)
down()
rt(90)
fillcolor('white')
begin_fill()
circle(35)
end_fill()
begin_fill()
circle(-35)
end_fill()
up()
goto(10,140)
down()
fillcolor('black')
begin_fill()
circle(10)
end_fill()
up()
goto(-60,140)
down()
begin_fill()
circle(10)
end_fill()
up()
goto(-60,93)
down()
fillcolor('orange')
begin_fill()
seth(50)
circle(-40,100)
end_fill()
seth(-130)
circle(-40,100)
seth(90)
begin_fill()
circle(-30,-180)
end_fill()
seth(-130)
circle(-40,100)
seth(0)
up()
goto(-50,-20)
down()
circle(120,100)
pencolor('red')
lt(90)
fillcolor('red')
begin_fill()
circle(40,143)
lt(90)
pensize(4)
pencolor('black')
circle(120,39)
end_fill()
up()
goto(-50,-20)
down()
seth(0)
pensize(5)
circle(120,280)
up()
goto(-160,80)
down()
begin_fill()
pencolor('red')
fillcolor('red')
circle(40)
end_fill()
seth(0)
up()
goto(-50,280)
down()
pencolor('black')
fillcolor('silver')
begin_fill()
circle(-180,90)
rt(90)
circle(-180,90)
end_fill()
rt(180)
begin_fill()
circle(-180,90)
rt(90)
circle(-180,90)
end_fill()
up()
goto(-150,-100)
down()
seth(90)
fillcolor('black')
begin_fill()
fd(130)
rt(90)
fd(200)
rt(90)
fd(130)
a=pos()
rt(90)
fd(200)
rt(90)
end_fill()
pencolor('snow')
pensize(15)
up()
fd(80)
down()
rt(90)
circle(-80,90)
up()
goto(a)
down()
up()
bk(80)
down()
rt(90)
circle(80,90)
up()
bk(40)
down()
rt(90)
fd(40)
up()
goto(-300,-180)
down()
seth(0)
ht()
pencolor('mediumslateblue')
write('我是练习时长两年半的个人练习生,喜欢唱跳rap篮球',font=('宋体',18,'normal'))
ht()
done()
