sum = 0
continue_input = True

while continue_input:
    num = int(input("შეიყვანეთ რიცხვი (უარყოფითზე შეწყდება): "))
    if num < 0:
        continue_input = False
    else:
        sum += num

print("მიღებული დადებითი რიცხვების ჯამი:", sum)
