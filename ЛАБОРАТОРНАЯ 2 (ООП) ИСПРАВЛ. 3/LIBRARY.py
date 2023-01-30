

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
        self.id = id_
        self.name = name
        self.pages = pages

    def __str__(self) -> str:
        return f'{self.id + 1}'

    def __repr__(self)-> str:
        return f"Book(id_={self.id}, name={self.name!r}, pages={self.pages})"

# TODO написать класс Library

list1= []
class Library:
    def __init__(self, books = None):
       if books == None:
        self.books = None
       if books != None:
        self.books = books

    def get_next_book_id(self)-> int:
        if self.books == None:
          return 1
        if self.books != None:
          return list_id[-1]+1

    def get_index_by_book_id(self, id_)-> str:
        self.id = id_
        if id_ in list_id:
          return f'{self.id - 1}'
        else:
          return "Error"

if __name__ == '__main__':

    library1 = Library()  # инициализируем пустую библиотеку

    print(library1.get_next_book_id())  # проверяем следующий id для пустой библиотеки
    list_books = [
        Book(id_=book_dict["id"], name=book_dict["name"], pages=book_dict["pages"]) for book_dict in BOOKS_DATABASE
    ]
    list_id = [book_dict["id"] for book_dict in BOOKS_DATABASE]

    library2 = Library(books=list_books)  # инициализируем библиотеку с книгами
    print(library2.get_next_book_id())  # проверяем следующий id для непустой библиотеки###отвечает за вывод второй двойки

    print(library2.get_index_by_book_id(1))  # проверяем индекс книги с id = 1

