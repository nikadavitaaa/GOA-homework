pin_code = "9010"
attempted_pin = ""

count = 0
while entered_pin != pin_code:
    entered_pin = input("Enter pin code: ")
    count += 1

print(f"Logging in, You took {count} tries")
