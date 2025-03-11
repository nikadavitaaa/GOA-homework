from turtle import *
shape("turtle")

#აქ გავაფორმე ფანქარი რითაც ვხატავ
width(10)
color("black")
speed(15)

#დავიწყე სახლის მონახაზის გაკეტება
forward(350)
left(90)
forward(350)
left(90)
forward(350)
left(90)
forward(350)
left(90)

#ფანქარი გადავიტანე ამ კორდინატებზე კუთხის გასაკეტებლად
penup()
goto(350,350)
pendown()

#დავიწყე კუთხის ხაზვა
color("black")
begin_fill()
left(90)
forward(50)
left(90)
forward(50)
left(90)
forward(50)
end_fill()

#წავიღე ფანქარი ამ კორდინატზე
penup()
goto(0,350)
pendown()

#დავიწყე მეორე კუთხის ხაზვა
left(180)
begin_fill()
forward(50)
right(90)
forward(50)
right(90)
forward(50)
end_fill()


#გადამაქვს ფანქარი აქ
penup()
goto(115,350)
pendown()


#ვიწყებ მთავარი კოშკის ხაზვას
begin_fill()
left(180)
forward(50)
right(90)
forward(115)
right(90)
forward(50)
end_fill()


#ჩავიტანე ფანქარი კარის და ფანჯრების დასახაზად
penup()
goto(115,0)
pendown()

#დავიწყე კარის ხაზვა
color("brown")
begin_fill()
left(180)
forward(165)
right(90)
forward(115)
right(90)
forward(165)
end_fill()

#გადავედი ფანჯრებზე და წავედი ამ კორდინატებზე
penup()
goto(50,275)
pendown()

#ვიწყებ ფანჯრების ხაზვას
begin_fill()
forward(60)
left(90)
forward(60)
left(90)
forward(60)
left(90)
forward(60)
left(90)
end_fill()

penup()
goto(295,275)
pendown()

begin_fill()
forward(60)
right(90)
forward(60)
right(90)
forward(60)
right(90)
forward(60)
end_fill()

#მიმაქვს ფანქარი დროშის დასახატად
penup()
goto(170,400)
pendown()


#ვიწყებ დროშის ხატვას
color("black")
begin_fill()
left(90)
forward(75)
right(130)
color("green")
forward(50)
right(140)
forward(30)
end_fill()

#საბოლოო ჯამში არცტუისე კარგი გამოვიდა მაგრამ დავტოვებ ასე,არამგონია გოას ლოგოს დახაზვა მოვახერხო <3














exitonclick()