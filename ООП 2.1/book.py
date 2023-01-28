from typing import Union


BOOKS_DATABASE = [
    {
        "id": 1,
        "name": "test_name_1",
        "pages": 200,
    },
    {
        "id": 2,
        "name": "test_name_2",
        "pages": 400,
    }
]

# TODO написать класс Book

class Book:
    def __init__(self, id_: int, name: str, pages: int):
        self.id_ = id_
        self.name = name  # объем жидкости в стакане
        self.pages = pages
    def __str__(self):
        return f'Книга "{self.name}"'

    def __repr__(self):
        return f"Book(id_={self.id_}, name={self.name!r}, pages={self.pages})"

if __name__ == '__main__':

    # инициализируем список книг
    book1 = Book("", "test_name_1", "")
    book2 = Book("", "test_name_2", "")
    print(book1)
    print(book2)

    list_books = [
       Book(id_= book_dict["id"], name=book_dict["name"],pages= book_dict["pages"])for book_dict in BOOKS_DATABASE
    ]

    print(list_books)  # проверяем метод __repr__

