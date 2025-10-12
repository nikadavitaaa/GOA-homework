class Book:
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages

    def info(self):
        print(f"სათაური: {self.title}, ავტორი: {self.author}, გვერდები: {self.pages}")
