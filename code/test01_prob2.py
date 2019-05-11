# 面试题2: 实现单例(Singleton)模式

# 方法一:
# Python 的模块就是天然的单例模式，因为模块在第一次导入时，会生成 .pyc 文件，
# 当第二次导入时，就会直接加载 .pyc 文件，而不会再次执行模块代码。
# 因此，我们只需把相关的函数和数据定义在一个模块中，就可以获得一个单例对象了。如果我们真的想要一个单例类，可以考虑这样做：
class Singleton(object):
    def foo(self):
        pass


singleton = Singleton()


# 把上面的代码保存在一个文件中
# from 文件名 import singleton


# 方法二:
# 使用类名()创建对象时, Python的解释器会自动调用两个方法:
# 使用__new__()完成: 1.为类对象分配空间  2.返回类对象引用
# 使用__init_()完成: 1.对象初始化  2.定义实例属性
# Python中似乎不像Java中将类对象和实例的初始化完全分成了两步
class Singleton(object):
    # 记录第一个被创建实例对象的引用
    instance = None

    # 记录是否执行过初始化
    init_flag = False

    def __new__(cls, *args, **kwargs):
        if cls.instance is None:
            # 调用父类方法
            cls.instance = super().__new__(cls)

        return cls.instance

    def __init__(self):
        if not Singleton.init_flag:
            print("初始化一个类对象")

            Singleton.init_flag = True


s = Singleton()
print(s)
s1 = Singleton()
print(s1)

# 下面是检验单例模式在多线程中是否稳定
import threading


class Singleton1(object):
    # 记录第一个被创建对象的引用
    instance = None

    # 记录是否执行过初始化
    init_flag = False

    def __new__(cls, *args, **kwargs):
        if cls.instance is None:
            cls.instance = super().__new__(cls)

        return cls.instance

    def __init__(self):
        if not Singleton.init_flag:
            print("初始化类")

            Singleton.init_flag = True


obj1 = Singleton1()
obj2 = Singleton1()
print(obj1, obj2)


def task(arg):
    obj = Singleton1()
    print(obj)


for i in range(10):
    t = threading.Thread(target=task, args=[i, ])
    t.start()
