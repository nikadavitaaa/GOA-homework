''' 2) შექმენით ფუნქცია, რომელიც მიიღებს კვადრატის სიგრძეს თუ სიგრძე არ გადმოგეცემათ ივარაუდოთ რომ ის 10-ია, გამოთვლის მის ფართობსა და პერიმეტრს და დააბრუნებს ერთად. ეს ფუნქცია გამოიძახეთ მინიმუმ 2-ჯერ ერთხელ გადაეცით თქვენთვის სასურველი სიგრძე, მეორედ კი არაფერი გადასცეთ, ორივე შემთხვევაში შეინახეთ ფუნქციის დაბრუნებული მნიშვნელობები ცვლადებში: square_area1, square_perimeter1, square_area2, square_perimeter2 '''

def square(length = 10):
    perimeter = length * 4
    area = length ** 2
    return perimeter, area

square_area1, square_perimeter1 = square(7)
square_area2, square_perimeter2 = square()