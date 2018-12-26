'''
定义一个学生类，用来形容学生
'''
# 定义一个空的类
class Student():
    # 一个空类，pass代表直接跳过
    # 此处pass必须有
    pass

# 定义一个对象
mingyue = Student()
class PythonStudent():
    # None给不确定的值赋值
    name = None
    age = 18
    course = "Python"
    # 需要注意
    # 1. def doHomeWork的缩进层级
    # 2. 系统默认一个self参数
    def doHomeWork(self):
        print("我在写作业")
        return None
# 实例化一个叫yueyue的学生，是一位具体的人
# 成员函数调用没有缩进参数
yueyue = PythonStudent()
yueyue.name
yueyue.age
yueyue.doHomeWork()