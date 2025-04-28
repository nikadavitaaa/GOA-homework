even_count = 0
odd_count = 0
num = 0

while num >= 0:
    num = int(input("შეიყვანეთ რიცხვი (უარყოფითზე შეწყდება): "))
    if num >= 0:  # მხოლოდ მაშინ ვმუშაობთ, როცა რიცხვი არ არის უარყოფითი
        if num % 2 == 0:
            even_count += 1
        else:
            odd_count += 1

print("ლუწი რიცხვების რაოდენობა:", even_count)
print("კენტი რიცხვების რაოდენობა:", odd_count)
