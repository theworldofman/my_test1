# 定义学生对象
class Student:
    def __init__(self,name,age):
        self.name=name
        self.age=age
        self.my_course=[]
    def addcourse(self,course):
        self.my_course.append(course)

    def delcourse(self,course):
        for course in self.my_course:
            if course.name==self.name:
                self.my_course.remove(course)


    def __str__(self):
        return ""

# 定义课程对象
class Course:
    def __init__(self,name,id,Capacity,num):
        self.name=name
        self.id=id
        self.Capacity=Capacity
        self.num=num

    def addcourse(self,stu):
        if self.num+1 < self.Capacity:
            self.num+=1
            stu.my_course.append(self)
            print("添加成功")
        else:
            print("选择失败,人数已满")

    def delcourse(self,stu):
        if self in stu.my_course:
            stu.my_course.remove(self)
            print("删除成功")
        else:
            print("没有该课程删除失败")

# 定义选课管理系统
class CourseSelectionManagement:
    def __init__(self):
        self.my_students=[]
        self.my_course=[]

    def addstudent(self,name,age):
        i=0
        for stu in self.my_students:
            if stu.name==name:
                print("学生存在无法添加")
                i=1
                break
        if i==0:
            stu=Student(name,age)
            self.my_students.append(stu)
            print("学生添加成功")

    def addcourse(self,name,id,Capacity,num):
        i=0
        for course in self.my_course:
            if course.name==name:
                print("课程存在无法添加")
                i=1
                break
        if i == 0:
            course = Course(name, id, Capacity, num)
            self.my_course.append(course)

    #控制学生添加课程
    def stuaddcourse(self,stuname,coursename):
        i=0
        j=0
        for stu in self.my_students:
            if stu.name==stuname:
                i = 1
                for course in self.my_course:
                    if course.name==coursename:
                        j=1
                        course.addcourse(stu)
        if i==0:
            print("学生未找到添加失败")

        if j==0:
            print("课程未找到添加失败")

#控制学生删减
    def studelcourse(self,stuname,coursename):
        i = 0
        j = 0
        for stu in self.my_students:
            if stu.name == stuname:
                i = 1
                for course in stu.my_course:
                    if course.name == coursename:
                        j = 1
                        course.num-=1
                        stu.delcourse(course)
                        print("删除成功")
        if i == 0:
            print("学生未找到删减失败")

        if j == 0:
            print("课程未找到删减失败")

# 控制面板
    def ControlPanel(self):
        i=1
        while True:
            if i != 5:
                print("#############################################################")
                print("1.添加学生  2.添加课程   3.控制学生添加课程  4控制学生删减课程    5退出")
                print("#############################################################")
                i = int(input("请选择功能"))
                match i:
                    case 1:
                        stu = input("请输入学生姓名")
                        age = input("请输入学生年龄")
                        self.addstudent(stu, age)
                    case 2:
                        name=input("请输入课程名字")
                        id=input("请输入课程编号")
                        Capacity=int(input("请输入课程容量"))
                        num=int(input("请输入已选课的人数"))
                        self.addcourse(name,id,Capacity,num)
                    case 3:
                        stuname=input("请输入学生名字")
                        coursename=input("请输入添加课程名称")
                        self.stuaddcourse(stuname,coursename)
                    case 4:
                        stuname = input("请输入学生名字")
                        coursename = input("请输入添加课程名称")
                        self.studelcourse(stuname,coursename)


test=CourseSelectionManagement()
test.ControlPanel()

