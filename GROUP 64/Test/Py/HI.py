# ბანკის პროგრამის პროტოტიპი

accounts = {}

def create_account():
    name = input("შეიყვანე სახელი: ")
    if name in accounts:
        print("ეს მომხმარებელი უკვე არსებობს.")
        return
    pin = input("შეიყვანე 4-ნიშნა PIN კოდი: ")
    accounts[name] = {"balance": 0, "pin": pin}
    print(f"ანგარიში შეიქმნა მომხმარებლისთვის {name}.")

def login():
    name = input("შეიყვანე სახელი: ")
    pin = input("შეიყვანე PIN კოდი: ")
    
    if name in accounts and accounts[name]["pin"] == pin:
        print(f"\nმოგესალმებით, {name}!")
        account_menu(name)
    else:
        print("არასწორი სახელი ან PIN კოდი.")

def account_menu(name):
    while True:
        print("\n--- ანგარიშის მენიუ ---")
        print("1. ბალანსის შემოწმება")
        print("2. თანხის შეტანა")
        print("3. თანხის განაღდება")
        print("4. გამოსვლა")

        choice = input("აირჩიეთ: ")

        if choice == "1":
            print(f"მიმდინარე ბალანსი: {accounts[name]['balance']} ₾")

        elif choice == "2":
            amount = float(input("შეიყვანე თანხა შესატანად: "))
            accounts[name]["balance"] += amount
            print(f"{amount} ₾ დამატებულია ანგარიშზე.")

        elif choice == "3":
            amount = float(input("შეიყვანე თანხა განაღდებისთვის: "))
            if amount <= accounts[name]["balance"]:
                accounts[name]["balance"] -= amount
                print(f"{amount} ₾ განაღდებულია ანგარიშიდან.")
            else:
                print("არასაკმარისი თანხა.")

        elif choice == "4":
            print("გამოსვლა ანგარიშიდან.")
            break
        else:
            print("არასწორი არჩევანი.")

def main_menu():
    while True:
        print("\n--- მთავარი მენიუ ---")
        print("1. ანგარიშის შექმნა")
        print("2. სისტემაში შესვლა")
        print("3. გამოსვლა პროგრამიდან")

        choice = input("აირჩიეთ: ")

        if choice == "1":
            create_account()
        elif choice == "2":
            login()
        elif choice == "3":
            print("პროგრამიდან გამოსვლა...")
            break
        else:
            print("არასწორი არჩევანი.")

# პროგრამის გაშვება
main_menu()
