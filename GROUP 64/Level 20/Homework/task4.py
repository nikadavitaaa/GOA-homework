Pin = "1234"  # შეგიძლიათ შეცვალოთ თქვენი PIN კოდი
attempts = 3
access_granted = False

while attempts > 0 and not access_granted:
    pin = input("შეიყვანეთ PIN კოდი: ")
    if pin == Pin:
        access_granted = True
        print("Access Granted")
    else:
        attempts -= 1
        if attempts > 0:
            print("პასუხი არასწორია. დარჩენილია " + str(attempts) + " მცდელობა.")
        else:
            print("Access Denied")

