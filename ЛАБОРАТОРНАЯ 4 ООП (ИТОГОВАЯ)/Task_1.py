if __name__ == "__main__":
    # Write your solution here
    pass

class Building:
    """ Базовый класс: здание.
      :param year_of_construction: Год постройки
      :param height: Высота здания"""
    def __init__(self, year_of_construction: int, height: int):
        self._year_of_construction = year_of_construction
        self._height = height

    @property
    def year_of_construction(self):
       return self._year_of_construction

    """ Год постройки не может быть изменён. """
    @property
    def height(self):
        return self._height

    """ Высота здания не может быть изменена. """

    def __str__(self):
        return f"Год постройки {self._year_of_construction}. Высота {self._height} метров"

    def __repr__(self):
      return f"{self.__class__.__name__}(year_of_construction={self._year_of_construction!r}, author={self._height!r})"

    def reconstruct_the_building(self):
        """Реконструировать здание"""
        ...
        """Метод можно унаследовать"""
    def demolish_the_building(self):
        """Снести здание"""
        ...
        """Метод можно унаследовать"""
class Residential_building(Building):
    """ Дочерний класс: жилое здание. 
    """   """ Базовый класс: здание.
      :param number_of_a_partments: Количество квартир"""
    def __init__(self, year_of_construction: int, height: int, number_of_a_partments: int):
        super().__init__(year_of_construction, height)
        self.number_of_a_partments = number_of_a_partments

    @property
    def number_of_a_partments(self):
        return self._number_of_a_partments

    """ Количество этажей не может быть изменено. """

    @number_of_a_partments.setter
    def number_of_a_partments(self, new_number_of_a_partments: int):
       if not isinstance(new_number_of_a_partments, int):
           raise TypeError("Количество квартир должно быть int")
       if new_number_of_a_partments <= 0:
           raise ValueError("Количество квартир должно быть положительным числом")
       self._number_of_a_partments = new_number_of_a_partments

    def __str__(self):
        return f"Год постройки {self._year_of_construction}. Высота {self._height} метров. Количество квартир {self.number_of_a_partments}"

    def __repr__(self):
        return f"{self.__class__.__name__}(Год постройки={self._year_of_construction!r}, Высота={self._height!r})"

print(Building(2020, 75))
print(Residential_building(1989, 50, 84))