"https://www.codewars.com/kata/5648b12ce68d9daa6b000099/train/python"

"Number of People in the Bus"

def number(bus_stops):
    total = 0
    for on, off in bus_stops:
        total += on - off
    return total
