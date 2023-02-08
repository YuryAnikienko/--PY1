
class Book:
    """ Базовый класс книги. """
    def __init__(self, name: str, author: str):
        self._name = name
        self._author = author

    @property
    def name(self):
       return self._name

    @property
    def author(self):
        return self._author

    def __str__(self):
        return f"Книга {self._name}. Автор {self._author}"

    def __repr__(self):
      return f"{self.__class__.__name__}(name={self._name!r}, author={self._author!r})"


class PaperBook(Book):
    """ Бумажная книга. """
    def __init__(self, name: str, author: str, pages: int):
        super().__init__(name, author)
        self.pages = pages

    @property
    def pages(self):
        return self._pages

    @pages.setter
    def pages(self, new_pages: int):
       if not isinstance(new_pages, int):
           raise TypeError("Количество страниц должно быть int")
       if new_pages <= 0:
           raise ValueError("Количество страниц должно быть положительным числом")
       self._pages = new_pages

    def __str__(self):
        return f"Книга {self._name}. Автор {self._author}. Количество страниц {self.pages}"

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self._name!r}, author={self._author!r})"

class AudioBook(Book):
    """ Аудиокнига """
    def __init__(self, name: str, author: str, duration: float):
        super().__init__(name, author)
        self.duration = duration

    @property
    def duration(self):
        return self._duration

    @duration.setter
    def duration(self, new_duration: float):
        if not isinstance(new_duration, float):
            raise TypeError("Продолжительность аудиокниги float")
        if new_duration <= 0:
            raise ValueError("Продолжительность аудиокниги должна быть положительным числом")
        self._duration = new_duration

    def __str__(self):
        return f"Книга {self._name}. Автор {self._author} Продолжительность аудиокниги {self.duration}"

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self._name!r}, author={self._author!r})"

print(PaperBook("Книга 1", "N1", 200))
print(AudioBook("Аудиокнига 1", "N2", 60.0))

