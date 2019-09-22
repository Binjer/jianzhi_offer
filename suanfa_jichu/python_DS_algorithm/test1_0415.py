# 计算机科学: 研究能够解决的问题的方案(可计算的)和不能解决的问题(不可计算的)的科学

# 理解程序抽象
# import math
# print(math.sqrt(16))

# 抽象数据类型ADT(Abstract data type), 通常称为数据结构


# 测试运行时间
import timeit
import random

for i in range(1000, 10001, 20000):
    t = timeit.Timer("random.randrange(%d) in x" % i, "from __main__ import random, x")
    x = list(range(i))
    lst_time = t.timeit(number=1000)
    x = {j: None for j in range(i)}
    d_time = t.timeit(number=1000)
    print("%d, %10.3f, %10.3f" % (i, lst_time, d_time))
