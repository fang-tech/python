# python学习 day2

## 1. 字符串

### 1. 转义字符

- 使用'\\'用作表示后续的字符的含义需要发生变化

- 常见的转义情况
    1. 制表符等缩进符号 : `\t`, `n`
    2. 跟八进制或者十六进制来表示字符, \146与\x61都表示小写字母a
    3. \后面跟Unicode字符编码表示字符, `\u9a86\u660a`表示的是中文"骆昊"
    4. 如果不希望字符串中的\表示转义, 可以使用`r"\n"`, 在字符串的最前面加上字母r来加以说明

### 2. 字符串相关运算符

- ```python
    # * 运算符
    s1 = 'hello'* 3
    print(s1) 
    
    # result : hello hello hello
    
    # "in" and "not in" operator
    s2 = 'hello'
    print(s2 in s1) # True
    print('s1' not in s1) # True
    
    # "slice operatr"
    str2 = 'abc12345'
    print(str2[2]) # c
    print(str2[2:5]) # c123
    print(str2[2::2]) # c24, start at c, step is 2        
    
    ```

### 3. 字符串相关函数

```python
len()
capitalize()
upper()
find()
startwith()
endwith()
isdigit()
isalnum()
isalpha()
strip() # 跳过头和尾的空白
```

## 2. 列表

### 1. 遍历链表

```python
# 通过循环用下标遍历列表元素
for index in range(len(list1)):
    print(list1[index])
# 通过for循环遍历列表元素
for elem in list1:
    print(elem)
# 通过enumerate函数处理列表之后再遍历可以同时获得元素索引和值
for index, elem in enumerate(list1):
    print(index, elem)
```

### 2. 添加和删除元素

```python
# 合并两个列表
# list1.extend([1000, 2000])
list1 += [1000, 2000]
# 添加元素
list1.append(200)
list1.insert(1, 400)
# 先通过成员运算判断元素是否在列表中，如果存在就删除该元素
if 3 in list1:
	list1.remove(3)
# 从指定的位置删除元素
list1.pop(0)
list1.pop(len(list1) - 1)
# 清空列表元素
list1.clear()
```

### 3. 切片

```pyhton
# 可以通过反向切片操作来获得倒转后的列表的拷贝
fruits5 = fruits[::-1]
```

###  4. 排序

```python
# sorted函数返回列表排序后的拷贝不会修改传入的列表
list3 = sorted(list1, reverse=True)
# 通过key关键字参数指定根据字符串长度进行排序而不是默认的字母表顺序
list4 = sorted(list1, key=len)  # 这里排序的是单词list
# 给列表对象发出排序消息直接在列表对象上进行排序
list1.sort(reverse=True)
```

## 3. 生成式和生成器

### 1. 生成式

- Code

```python
# 字典生成式
dict_ = {k:v for k in range(1, 100) for v in range(1, 200, 2)}
print(dict_)
   
# comprehension
f = [x for x in range(1, 10)]
print(f)
f = [x + y for x in 'ABCDE' for y in '1234567'] 
print(f)
```

- Description
  - 生成式就是一个自动创建列表, 字典, 集合的工具, 能根据需求创建一个对应的容器

### 2. 生成器

- Code

```python
# 生成式生成器
f = [x ** 2 for x in range(1, 1000)]
print(sys.getsizeof(f))

# 函数式的生成器
def count_up_to(max):
    count = 1
    while count <= max:
        # count += 1
        yield count
        count += 1

counter = count_up_to(5)
# 每次调用生成器的'__next__()'方法 (通常为'next()函数'), 
# 生成器函数运行到下一个'yield'表达式
# 就像一个单程车一样, 在需要的站点下来几个变量
print(next(counter))
```

- Description
  - 生成器是一种特殊的迭代器, 使用'yield'关键字来一次生成一个值, 而不是像普通函数一样一次性生成所有值
  - 惰性计算 : 只有在需要的时候才会计算下一个值
  - 状态保持 : 生成器会记住上一次暂停的状态, 并从该点继续运行
  - 单次迭代 : 生成器只能迭代一次, 这也导致了这是个"单程车"

### 3. 对比

|   /    | 生成式 | 生成器 |
| :----: | :----: | :----: |
|  内存  |   大   |   小   |
| 自由度 |   大   |   小   |
|  单向  |   是   |   否   |

## 4. 元组

- 不可变的列表
- 线程安全

## 5. 集合

- Code

```python
# 集合的交集、并集、差集、对称差运算
print(set1 & set2)
# print(set1.intersection(set2))
print(set1 | set2)
# print(set1.union(set2))
print(set1 - set2)
# print(set1.difference(set2))
print(set1 ^ set2)
# print(set1.symmetric_difference(set2))
# 判断子集和超集
print(set2 <= set1)
# print(set2.issubset(set1))
print(set3 <= set1)
# print(set3.issubset(set1))
print(set1 >= set2)
# print(set1.issuperset(set2))
print(set1 >= set3)
# print(set1.issuperset(set3))
```

## 6. 字典

- Code

```python
dict1 = {num: num ** 2 for num in range(10)}
print(dict1)

# 对所有键值对进行遍历
for Key in dict1:
    print(f"{Key}: {dict1[Key]}")

for i, v in enumerate(dict1):
    print(f"{i}: {v}")
```



 

