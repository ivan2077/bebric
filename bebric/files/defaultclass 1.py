#каждое слово в имени класса с большой буквы
class NameClass():
    """тут пиши коментарий к классу"""
    #self по традици передает имя объекта. после него идут атрибуты запрашиеваемые при инициализации (init) класса
    def __init__(self, atr1, atr2, atr3):
        self.atr1 = atr1
        self.atr2 = atr2
        self.atr3 = atr3

    # действия с атрибутами в функции (функция в классе называется методом)
    def namefunc(self):
        """тут пиши коментарий к методу"""
        print(f'атрибут1:{self.atr1} атрибут2:{self.atr2} атрибут3:{self.atr3}')

    # можно добавить аргумент
    def plus(self, chislo):
        """тут пиши коментарий к методу"""
        self.atr1 += chislo 
        self.atr2 += chislo
        self.atr3 += chislo

# создание экземпляра класса и передача атрибутов
x = NameClass(1,2,3)
y = NameClass(4,5,6)

# применяем метод к объекту класса
x.namefunc()
y.namefunc()

# выполняем метод с доп аргументом
x.plus(5)
y.plus(6)

x.namefunc()
y.namefunc()
