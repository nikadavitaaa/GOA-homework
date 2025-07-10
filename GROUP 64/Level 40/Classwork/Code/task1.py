"3) განხილულ მეთოდებზე: split, join, replace, strip მოიყვანეთ 2-2 მაგალითი. თითოეულს მიუწერეთ კომენტარებით ახსნა თუ როგორ მუშაობს"

# split() – სტრიქონის დაყოფა სიად

text = "hello world"
words = text.split()  
print(words)

data = "apple,banana,orange"
fruits = data.split(",")  
print(fruits)

# join() – ელემენტების გაერთიანება სტრიქონად

words = ['hello', 'world']
sentence = " ".join(words)
print(sentence)

letters = ['a', 'b', 'c']
result = "-".join(letters)
print(result)

# replace() – სტრიქონების ნაწილებიოს შეცვლა

text = "I like apples"
new_text = text.replace("apples", "bananas")
print(new_text)

text = "2025/06/29"
formatted = text.replace("/", "-")
print(formatted)

# strip() – სიმბოლოების მოცილება სტრიქონის დასაწყისიდან და ბოლოდან

text = "   hello   "
clean = text.strip()
print(clean)

text = "!!!wow!!!"
clean = text.strip("!")
print(clean)
