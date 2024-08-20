# Python基础zhi'shi

## 简单的IO 
```python
    type(intput("提示信息"))
```

## 循环结构

1. range

```
range(101): 可以用来生成0 - 100范围的整数
range(1, 101): 可以生成1 - 100范围的整数, 相当于前面是闭区间后面是开区间
range(1, 101, 2): 可以用来生成1 - 100 的奇数, 其中2是步长, 即每次数值递增的值
range(100, 0, -2): 可以用来产生1到100的偶数, 其中-2是步长, 即每次数值递减的值
```
## 函数

1. 函数的参数
     - python不直接支持函数的重载
        - 我们更倾向于使用可变参数
        - 样例
            ```python
            def add(*args):
                total = 0
                for val in args:
                    total += val
                return total
            ```
2. 使用模块管理函数
     - 可以使用模块名.函数名, 来引用其他模块中的函数
     - 也可以直接from 模块名 import 函数名
     - 样例
        ```python
        from module1 import func1
        import module2
        func1()
        module2.func2()
        ```
3. pass的作用
     - python 的if语句内, 函数块内, 都不能为空, 但是有时候我们只是需要一个占位的内容, 我们就可以使用pass
     - pass表示空操作, 可以用做占位符

4. 变量的作用域
     - python中函数传递的是实参
     - python查找变量的顺序是
        1. 局部定义域 : 局部变量
        2. 嵌套作用域 : 外层函数变量
        3. 全局作用域 : 全局变量
        4. 最后, 如果三个都没有找到, 就会去内置作用域中查找, step by step, 找到了其中一个就不会继续往下找了

5. 内置作用域
    1. python最外层的作用域, 包含了Python语言预定义的名称. 在任何python程序中使用, 无需额外导入
    2. 内置作用域的内容 : 
        - 内置函数: 如print(), len(), range(), type()
        - 内置常量: 如True, False
        - 内置异常类: Exception, TypeError
        - 内置类型: int, float
    3. 访问内置作用域:
        - 可以直接使用内置名称, 无需导入
        - 可以通过__builtins__模块访问所有内置名称.
    4. 查看所有内置名称:
        - 可以使用dir(__builtins__)查看所有内置名称列表
6. 生命周期
    - 局部变量 : 函数执行结束后销毁
    - 全局变量 : 程序结束时销毁
    - 类的属性 : 当对象被销毁时随之销毁

7. 内存管理
python的内存管理是自动的主要涉及以下几个方面
    1.  引用计数:
        - 每个对象都有一个引用计数, 记录有多少个引用指向它
        - 当引用的计数的数字为0的时候, 对象被销毁
    2. 内存池 :
        - python维护一个内存池, 用于小对象 (如小整数, 短字符串) 的重用
    3. 内存分配策略 :
        - 大对象直接通过操作系统分配内存
        - 小对象通过内存池分配

8. 垃圾回收机制 :
    1. 引用计数(主要机制):
        - 优点 : 简单, 即时
        - 缺点 : 无法处理循环引用
    2. 分代回收 :
        - 基于"新生代对象更容易成为垃圾"的假设
        - 将对象分为三代, 新生代对象更频繁地进行回收
    3. 循环垃圾收集器 :
        - 用于检测和回收循环引用的对象
        - 通过图算法检测无法到达的对象组
    4. 详细说明 :
        1. 引用计数 :   
            ```python
            import sys
              
            a = [1, 2, 3]
            print(sys.getrefcount(a) - 1)  # 输出：1
              
            b = a  # 增加引用
            print(sys.getrefcount(a) - 1)  # 输出：2
              
            del b  # 减少引用
            print(sys.getrefcount(a) - 1)  # 输出：1
           ```
        2. 循环引用 :
           ```python
            class Node:
                def __init__(self):
                    self.ref = None
           
            a = Node()
            b = Node()
            a.ref = b
            b.ref = a
           
            # a 和 b 相互引用，但外部没有引用它们
            # 需要循环垃圾收集器来回收
           ```
        3. 手动触发垃圾回收 :
            ```python
            import gc
            
            gc.collect()  # 手动触发垃圾回收
            ```
            4. 内存使用情况 :
            ```python
            import psutil
            import os
            
            process = psutil.Process(os.getpid())
            print(process.memory_info().rss)  # 输出当前进程的内存使用
            ```
        5. 弱应用
            ```python
            import weakref
            
            class Object:
                pass
            
            obj = Object()
            r = weakref.ref(obj)
            
            print(r() is obj)  # 输出：True
            
            del obj
            print(r() is None)  # 输出：True
            ```
