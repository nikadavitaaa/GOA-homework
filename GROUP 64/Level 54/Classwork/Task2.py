def greet_people(Special, *Guests, **Visitors):
    print(f"Welcome {Special}")
    for Guest in Guests:
        print(f"Hello {Guest}")
    for Visitor in Visitors.items():
        print(f"Hey there! {Visitor}")
