try:
    user_input = input("გთხოვთ, შეიყვანოთ რიცხვი: ")
    number = int(user_input)
    print("შეყვანილი რიცხვია:", number)
except ValueError:
    print("შეიყვანეთ მხოლოდ რიცხვი")
