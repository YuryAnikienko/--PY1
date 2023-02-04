import doctest


# TODO Написать 3 класса с документацией и аннотацией типов

class Ballon:
    def __init__(self, colour: str, volume: float):
      """
      Создание и подготовка к работе объекта "Воздушный шар"
      :param colour: Цвет шарика
      :param volume: Объём шарика

      Примеры:
      >>> ballon1 = Ballon("Зелёный", 11)  # инициализация экземпляра класса
      """
      self.colour = colour
      self.volume = volume

    def change_colour(self, colour):
       self.colour = colour
       return f'{self.colour}'


    def change_volume (self, delta_volume):
       self.delta_volume = delta_volume
       return f'{self.delta_volume + self.volume}'



class Student:
    def __init__(self, average_score: float, final_exam: int):
        """
        Создание и подготовка к работе объекта "Студент"
        :param average_score: средний балл
        :param final_exam: результат итогового экзамена

        Примеры:
        >>> student1 = Student(4, 5)  # инициализация экземпляра класса
        """

        self.average_score = average_score
        self.final_exam = final_exam


    def internship(self, average_score: float)-> str:
        """
        Распределение по стажировкам
        :param average_score: средний балл
        Примеры:
        >>> student1 = Student(4, 5)
        >>> student1.internship()
        """

        if average_score < 4:
          return "Cтудент попадёт туда, где останутся места"
        if average_score >= 4:
          return "Cтудент сам выбирает работодателя для стажировки"


    def scolarship(self, final_exam: int)-> str:
        """
        Выплата стипендии
        :param final_exam: оценка за итоговый экзамен
        Примеры:
        >>> student1 = Student(4, 5)
        >>> student1.scolarship()
        """

        if final_exam == 3:
            return "Стипендии не будет"
        if final_exam == 4 or 5 :
            return "Стипендия будет"


class Chemical_element:
    def __init__(self, mass_number: int, charge_number: int):
       """
       Создание и подготовка к работе объекта "Химический элемент"
       :param mass_number: массовое число
       :param final_exam: зарядовое число

       Примеры:
       >>> chemical_element1 = Chemical_element(4, 5)  # инициализация экземпляра класса
       """
       self.mass_number = mass_number
       self.charge_number = charge_number

    def alpha_decay(self, mass_number):
       """
        Альфа-распад химического элемента
       :param mass_number: массовое число

       Примеры:
       >>> chemical_element1.alpha_decay()
       """

       self.mass_number = mass_number
       return f'{self.mass_number - 4}'


    def beta_decay(self, charge_number):
        """
        Бета-распад химического элемента
        :param charge_number: зарядовое число

       Примеры:
       >>> chemical_element1.beta_decay()
        """
        self.charge_number = charge_number
        return f'{self.charge_number - 2}'


    def gamma_decay(self):
       """
       Гамма-распад химического элемента

       Примеры:
       >>> chemical_element1.beta_decay()
       """
       return "Гамма-излучение"


if __name__ == '__main__':
    chemical_element1 = Chemical_element(4, 5)
    student1 = Student(4, 5)  # и
    ballon1 = Ballon ("Зелёный", 5)
    print(chemical_element1.alpha_decay(4))
    print(chemical_element1.beta_decay(5))
    print(chemical_element1.gamma_decay())
    print(student1.internship(3.4))  # п
    print(student1.scolarship(5))  # п
    print(ballon1.change_volume(10))


if __name__ == "__main__":
    # TODO работоспособность экземпляров класса проверить с помощью doctest
    doctest.testmod()
