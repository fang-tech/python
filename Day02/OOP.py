# 装饰器

class Person(object):
    
    def __init__(self, name, age):
        self._name = name
        self._age = age

    # getter
    @property
    def name(self):
        print("name getter")
        return self._name
    
    # getter
    @property
    def age(self):
        print("age getter")
        return self._age

    # setter
    @name.setter
    def name(self, name):
        print("name setter")
        self._name = name
    
    def print(self):
        print(f"age: {self._age}, name: {self._name}")
        

def test_property():
    p = Person(name = 'fang', age = 20)
    p.name = "tian"
    print(f"{p.name}, {p.age}")


# __slots__
class Person(object):

    # 限定对象只能有, _name, _age, _gender属性
    __slots__ = ('_name', "_age", '_gender')

    def __init__(self, name, age , gender):
        self._name = name
        self._age = age
        self._gender = gender


def test_slots():
    p = Person('fang', 21, '难')
    # AttributeError: 'Person' object has no attribute '_is_gay'
    p._is_gay = False


# staticmethod
class Triangle(object):

    def __init__(self, a, b, c):
        self._a = a
        self._b = b
        self._c = c

    @staticmethod
    def is_valid(a, b, c):
        return a + b > c and a + c > b and b + c > a


def test_staticmethod():
    a, b, c = 1, 2, 3
    print(Triangle.is_valid(a,b,c))


class MyClass(object):

    class_variable = "MyClass"

    @classmethod
    def class_method(cls):
        print(cls.class_variable)

    @staticmethod
    def static_method():
        print("无法访问类变量")


def test_classMethod():
    MyClass.class_method()
    MyClass.static_method()


class Factory(object):

    def __init__(self, age, name):
        self._age = age
        self._name = name

    @classmethod
    def from_birth_year(cls, birthyear, name):
        return cls(2024-birthyear, name)


def test_factory():
    p1 = Factory(19, 'a')
    p2 = Factory.from_birth_year(2004, 'fang')
    print(p1._name, p1._age)
    print(p2._name, p2._age)


def main():
    # test_property() 
    # test_slots()
    # test_staticmethod()
    # test_classMethod()
    test_factory()
    pass


if __name__ == "__main__":
    main()
