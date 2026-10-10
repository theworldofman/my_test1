# from os import name
# from random import choice

class Student:
    def __init__(self,name,chinese,math,english):
        self.name=name
        self.chinese=chinese
        self.math=math
        self.english=english

    def __str__(self):
        return f"姓名:{self.name}|语文:{self.chinese}|数学:{self.math}|英语:{self.english}|总分:{self.english+self.chinese+self.math}"
    # 方法修改成绩
    def change_score(self,chinese = None,math = None,english = None):
        if chinese is not None:
            if 0 <= chinese <= 100:
                self.chinese = chinese
            else:
                print('成绩不合理,请重新操作')
        if math is not None:
            if 0 <= math <= 100:
                self.math = math
            else:
                print('成绩不合理,请重新操作')
        if english is not None:
            if 0 <= english <= 100:
                self.english = english
            else:
                print('成绩不合理,请重新操作')

# 增加学生,修改,删除,查询
class AcademicAffairsSystem:
    student_list=[]
# 添加学生成绩
    def add_student(self,student):
        if student not in AcademicAffairsSystem.student_list:
            chinese = int(input('请输入语文成绩:'))
            math = int(input('请输入数学成绩:'))
            english = int(input('请输入英语成绩:'))
            stu = Student(student,chinese,math,english)
            AcademicAffairsSystem.student_list.append(stu)

        else:
            print('学生已经存在,重新操作')
# 修改学生程序
    def change_student(self,student):
        for a in AcademicAffairsSystem.student_list:
            if student == a.name:
                print(a)
                s = input('请输入要修改科目')
                match s:
                    case "语文":
                        b = int(input('请输入修改后的语文成绩'))
                        a.change_score(chinese=b)
                    case "英语":
                        b = int(input('请输入修改后的英语成绩'))
                        a.change_score(english=b)
                    case "数学":
                        b = int(input('请输入修改后的数学成绩'))
                        a.change_score(math=b)
                    case _:
                        print('没有该科目')
                return
        print('暂无该学生请添加后再修改')

# 删除学生信息
    def delete_student(self,student):
        for a in AcademicAffairsSystem.student_list:
            if student == a.name:
                AcademicAffairsSystem.student_list.remove(student)
                print("学生删除成功")
                return
        print('学生不存在')
        return
# 查询学生信息
    def query_student(self,student):
        for a in AcademicAffairsSystem.student_list:
            if student == a.name:
                print(a)
                return
        print('学生不存在')
        return

# 打印学生
    def print_student(self):
        for a in AcademicAffairsSystem.student_list:
            print(a)
        print('欢迎再次使用')
        return

# 运行系统
    def run(self):
        print('欢迎使用学生管理系统')

        while True:
            print()
            print('########################################################')
            print('1.添加学生 2.修改学生 3.删除学生 4.查询学生 5.打印成绩 6.退出菜单')
            print('########################################################')
            print()

            choice =int( input('请输入想要操作') )
            match choice:
                case 1:
                    name = input("输入添加学生的名字")
                    self.add_student(name)
                case 2:
                    name = input("输修改学生的名字")
                    self.change_student(name)
                case 3:
                    name = input("输入删除学生的名字")
                    self.delete_student(name)
                case 4:
                    name = input("输入查询学生的名字")
                    self.query_student(name)
                case 5:
                    self.print_student()
                case 6:
                    break





list1 = AcademicAffairsSystem()
list1.run()
# list1.add_student('lhx')
# print(list1.student_list[0])