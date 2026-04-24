class Author:

    def __init__(self, name, bith_year, nationally):
        self.name = name
        self.birth_year = bith_year
        self.nationally = nationally
        self.age = 2026 - bith_year
        
author1 = Author("Navoiy", 1441, "O'zbek")

class Book:

    def __init__(self, title: str, author: Author, page_size: int):
        self.title = title
        self.author = author
        self.page_size = page_size



book1 = Book("Xamsa", Author, 872)

print(book1.title)