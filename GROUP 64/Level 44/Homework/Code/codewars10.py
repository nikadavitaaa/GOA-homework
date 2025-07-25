"https://www.codewars.com/kata/558fc85d8fd1938afb000014/train/python"

"Sum of two lowest positive integers"

def sum_two_smallest_numbers(numbers):
    numbers.sort()  # ჩამოვთხრი სიას ზრდადობით
    return numbers[0] + numbers[1]  # პირველი ორი ყველაზე პატარა რიცხვი დავუბრუნოთ
