from turtle import *
shape("turtle")


#i started painting the house
width(5)
color("orange")
forward(250)
left(90)
forward(250)
left(90)
forward(265)
left(90)
forward(250)
left(90)
forward(95)
# i painted the shape 0f the house and now im working on the door, roof and the window





#1. door
color("black")
begin_fill()
left(90)
forward(100)
right(90)
forward(70)
right(90)
forward(100)
end_fill()
#i finished drawing the door



#2. the roof

penup()
goto(250, 250)
pendown()

color("green")
begin_fill()
right(134)
forward(195)
left(91)
forward(187)
end_fill()
#ive drawn the roof

#now only the windows remain


#3. the windows


penup()
goto(0,200)


right(225)
pendown()


color("brown")
begin_fill()
forward(70)
right(90)
forward(70)
right(90)
forward(70)
right(90)
forward(70)
end_fill()

#i finished the first window and moved onto the second

penup()
goto(200,200)
pendown()


begin_fill()
left(90)
forward(35)
left(90)
forward(70)
left(90)
forward(70)
left(90)
forward(70)
left(90)
forward(35)
end_fill()




name = "nika" # ეს არის str (string) ტიპის ცვლადი, 
#name არის ცვლადი
# = არის ცვლადისთვის მნიშნელობის მიმნიჭებელი სიმბოლო
# "nika" არის ცვლადისთვის მნიშვნელობა
surname = "davitashvili"
age = 15 # ეს არის int(integer) მთელი რიცხვი


height = 175.1 # ეს არის float ტიპის ცვლადი( ათწილადი )
#boolean ( bool ) ტიპის ცვლადი


knows_proggraming = True  #True ან False

is_ugly = False  #snakecase ( უბრალოდ წერის სტილი სტანდარტულად )

isUgly = False  #javascript ( camelcase )

print(name + " " + surname)








exitonclick()