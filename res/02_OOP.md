# 面对对象

## 1. python中类的特征

- 没有像C++一样的成员属性上的强行规定, 没有真正的访问限制
- 单下划线前缀 : _attribute_name : 成员是受保护的
- 双下划线前缀 : __attribute_name : 成员是私有的
  - 名称重整: 对于使用双下划线前缀的私有属性和方法, Python会将其名称改为`_ClassName_attribute_name`, 我们可以通过重整后的命名访问这个属性

## 2. getter and setter

- Code

```python
class Person(object):

    def __init__(self, name, age):
        self._name = name
        self._age = age

    # 访问器 - getter方法
    @property
    def name(self):
        return self._name

    # 访问器 - getter方法
    @property
    def age(self):
        return self._age

    # 修改器 - setter方法
    @age.setter
    def age(self, age):
        self._age = age
```

## 3. \_\_slots\_\_

- Code

```python
class Person(object):

    # 限定Person对象只能绑定_name, _age和_gender属性
    __slots__ = ('_name', '_age', '_gender')

    def __init__(self, name, age):
        self._name = name
        self._age = age
        
def main():
    person = Person('王大锤', 22)
    person.play()
    person._gender = '男'
    # AttributeError: 'Person' object has no attribute '_is_gay'
    # person._is_gay = True
```

## 4. staticmethod and classmethod

- Code

```python
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
```





