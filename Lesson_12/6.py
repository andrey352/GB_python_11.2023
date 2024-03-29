# Изменяем класс прямоугольника.
# Заменяем пару декораторов проверяющих длину и ширину
# на дескриптор с валидацией размера.

class Side:

    def __init__(self, min_len, max_len):
        self.min_len = min_len
        self.max_len = max_len

    def __set_name__(self, owner, name):
        self.param_name = "_" + name

    def __get__(self, instance, owner):
        return getattr(instance, self.param_name)

    def __set__(self, instance, value):
        self.validate(value)
        setattr(instance, self.param_name, value)

    def validate(self, value):
        if value < self.min_len or value > self.max_len:
            raise ValueError


class Rectangle:
    _height = Side(10, 100)
    _width = Side(10, 100)

    def __init__(self, height, width=None) -> None:
        self._height = height
        if width:
            self._width = width
        else:
            self._width = height

    def __repr__(self):
        return f"Rectangle({self._height = }, {self._width = })"
        
    def per(self):
        return 2*(self._height + self._width)
    
    def area(self):
        return self._height * self._width
        
    def __add__(self, obj: "Rectangle"):
        new_per = self.per() + obj.per()
        new_height = self._height + obj._height
        new_width = (new_per / 2) - new_height
        if new_width <= 0 or new_height <= 0:
            raise ValueError
        return Rectangle(new_height, new_width)

    def __sub__(self, obj: "Rectangle"):
        new_per = self.per() - obj.per()
        new_height = self._height - obj._height
        new_width = (new_per / 2) - new_height
        if new_width <= 0 or new_height <= 0:
            raise ValueError
        return Rectangle(new_height, new_width)
    
    def __eq__(self, obj: "Rectangle") -> bool:
        return self.area() == obj.area()

    def __gt__(self, obj: "Rectangle") -> bool:
        return self.area() > obj.area()
    
    def __lt__(self, obj: "Rectangle") -> bool:
        return self.area() < obj.area()


if __name__ == "__main__":
    r1 = Rectangle(10, 11)
    # r1.width = 10
    print(r1._width)


