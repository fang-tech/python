def test_string():
    print("\thello world")
    print(r"\thello world")


def test_function_string():
    str1 = 'hello world'
    print(len(str1))
    print(str1.capitalize())  # make the fisrt letter uppercase
    print(str1.upper())  # make the whole world uppercase
    print(str1.find('or'))  # find the position of a substring in a string
    print(str1.find('index'))  # if not find, return -1
    print(str1.startswith('hel'))  # check if the string start with a specified substring, return a bool variable
    print(str1.endswith('!'))
    print(str1.isdigit())  # check if the string consists of digits only
    print(str1.isalnum())  # check if the string consists of digits and alphas
    print(str1.isalpha())
    print(str1.strip())  # remove leading and trailing whitespace from the string


def test_list():
    list1 = [1, 2, 3, 4, 5]
    for index in range(len(list1)):
        print(list1[index])
    for elem in list1:
        print(elem)
    for index, elem in enumerate(list1):
        print(f"index {index}, elem {elem }")

    # add elem and delete elem
    list1.append(12)  # tail insert
    list1.insert(1, 20)
    list1 += [1000, 2000]
    print(list1)

    # check if the element is in the list, then remove it if found
    if 3 in list1:
        list1.remove(1)

    print(list1)
    list1.pop(2)
    print(list1)

    list1.clear()
    print(list1)

    # sorted
    list2 = [25, 23, 1, 16, 78]
    print(list2)
    list3 = sorted(list2)
    print(list3)
    print(sorted(list2, reverse=True))
    print(sorted(list2))


def test_generator():
    # comprehension
    f = [x for x in range(1, 10)]
    print(f)
    f = [x + y for x in 'ABCDE' for y in '1234567'] 
    print(f)

    import sys
    # generator
    f = (x ** 2 for x in range(1, 1000))
    print(sys.getsizeof(f))

    # conprehension
    f = [x ** 2 for x in range(1, 1000)]
    print(sys.getsizeof(f))

    # 上面的书写形式是生成器的书写形式, 它会创建一个生成器对象
    # 通过生成器对象可以获取到数据, 但它不会占据额外的内存
    # 每次需要数据的时候就通过内部的运算得到数据

    # 与之相对的就是下面使用生成式创建列表容器, 因为所有元素都是创建好的, 所以会占据额外的内存
    # 但是不会花费额外的时间

def generator_and_conprehension():
    def count_up_to(max):
        count = 1
        while count <= max:
            # count += 1
            yield count
            count += 1

    counter = count_up_to(5)
    print(next(counter))
    print(next(counter))
    print(next(counter))

    dict_ = {k:v for k in range(1, 100) for v in range(1, 200, 2)}
    print(dict_)

def test_set():
    set1 = set(range(1, 10))
    set2 = {5, 3, 4, 24, 13}
    print(set1, set2)
    set3 = set((1, 1, 2, 2, 3))
    print(set3)
    set4 = {num for num in range(1, 100) if num % 7 == 0 or num % 5 == 0}
    print(set4)

    set4.add(123)
    print(set4)
    set4.pop()

    # 交集, 并集, 差集, 对称差
    print(set1 & set2)
    print(set1 | set2)
    print(set1 - set4)
    print(set1 ^ set2)

    # 判断子集和超集
    print(set1 <= set2)
    print(set1 >= set2)


def test_dict():
    dict1 = {num: num ** 2 for num in range(10)}
    print(dict1)

    # 对所有键值对进行遍历
    for Key in dict1:
        print(f"{Key}: {dict1[Key]}")

    for i, v in enumerate(dict1):
        print(f"{i}: {v}")


def main():
    # test_string()
    # test_function_string()
    # test_list()
    # test_generator()
    # generator_and_conprehension()
    # test_set()
    test_dict()
    pass


if __name__ == '__main__':
    main()
