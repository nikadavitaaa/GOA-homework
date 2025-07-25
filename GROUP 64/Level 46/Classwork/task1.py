"1) შექმენით student dictionary, რომელშიც გექნებათ მინიმუმ 4 ელემენტი. შემდეგ გამოიყენეთ მეთოდები ამ dictionary-ზე"

student = {
    "Name": "Nika",
    "Age": 15,
    "Height": 280, # ;)
    "Hobby": "Bjj, Proggraming"
}

student["Name"] = "nika"

student.update({
    "FavColor": "Blue"
})

student.pop("FavColor")

print(student)