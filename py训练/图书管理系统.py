# 图书管理系统主要有三个类
class user:
    def __init__(self,account,password,havebook=0,is_vip = 3 ):
        self.account=account
        self.password=password
        self.havebook=havebook
        self.is_vip=is_vip
        self.vip_level=0 if self.is_vip==3 else 1
        self.book=[]

    # 用户方法增加借的书
    def add_book(self,book_name):
        if self.havebook<self.is_vip:
            self.book.append(book_name)
            self.havebook+=1
            print('添加成功')
            return True
        else:
            print(f'你最多可以借{self.is_vip}本书')
            return None
    # 用户方法删除这本书
    def del_book(self,book_name):
        if book_name in self.book:
            self.book.remove(book_name)
            self.havebook-=1
            print('删除成功')
            return True
        else:
            print('没有这本书')
    # 升级成为vip
    def Upgrade_vip(self):
        if self.is_vip==6:
            print("你已经是VIP")
        elif self.is_vip==3:
            self.is_vip = 6
            self.vip_level = 1
            print("升级成功")

class book:
    def __init__(self,book_name,author,publish_time,publish_house,capacity):
        self.book_name=book_name
        self.author=author
        self.publish_time=publish_time
        self.publish_house=publish_house
        self.capacity=capacity
        self.borrowed=0

#     获得书籍信息
    def get_book_info(self):
        print(f'书名：{self.book_name},作者：{self.author},出版时间：{self.publish_time},出版社：{self.publish_house},容量：{self.capacity},已借出：{self.borrowed}')
#     借书
    def borrow_book(self):
        if self.borrowed<self.capacity:
            self.borrowed+=1
            print('借书成功')
        else:
            print('书已借完')
# 还书
    def return_book(self):
        if self.borrowed>0:
            self.borrowed-=1
            print('还书成功')
        else:
            print('没有这本书')
#定义魔法方法
    def __eq__(self, other):
        return self.book_name==other.book_name and self.author==other.author and self.publish_time==other.publish_time and self.publish_house==other.publish_house

class Library_system:
    def __init__(self):
        self.user=[]
        self.book=[]

#     登录
    def login(self,account,password):
        for i in self.user:
            if i.account==account and i.password==password:
                print('登录成功')
                return i
        print('登录失败')
        return None
#     注册
    def register(self,account,password):
        for i in self.user:
            if i.account==account:
                print('账号已存在')
                return None
        self.user.append(user(account,password))
        print('注册成功')
        return self.user[-1]
# 进书
    def add_book(self,book_name,author,publish_time,publish_house,capacity):
        self.book.append(book(book_name,author,publish_time,publish_house,capacity))
        print('进书成功')

# 操作界面
    def run(self):
        while True:
            print('1.登录 2.注册 3.退出系统')
            choice=input('请输入你的选择：')
            if choice=='1':
                account=input('请输入账号：')
                password=input('请输入密码：')
                a = self.login(account,password)
                if a:
                    while True:
                        print('1.借书 2.还书 3.查询书籍 4.升级VIP 5.退出')
                        choice=input('请输入你的选择：')
                        if choice=='1':
                            book_name=input('请输入书名：')
                            for i in self.book:
                                if i.book_name==book_name:
                                    if a.add_book(book_name) is not None:
                                        i.borrow_book()
                                    break
                        elif choice=='2':
                            book_name=input('请输入书名：')
                            if book_name in a.book:  # 先检查用户列表里有没有
                                a.del_book(book_name)
                                for i in self.book:
                                    if i.book_name == book_name                :
                                        i.return_book()
                                        break
                            else:
                                print('你没有借这本书')
                        elif choice=='3':
                            book_name=input('请输入书名：')
                            for i in self.book:
                                if i.book_name==book_name:
                                    i.get_book_info()
                                    break
                        elif choice=='4':
                            a.Upgrade_vip()
                        elif choice=='5':
                            break
                        else:
                            print('输入错误')
            elif choice=='2':
                account=input('请输入账号：')
                password=input('请输入密码：')
                self.register(account,password)
            elif choice=='3':
                break
            else:
                print('输入错误')


if __name__ == '__main__':
    library_system = Library_system()
    library_system.add_book('Python程序设计','张三','2020-01-01','电子工业出版社',10)
    library_system.run()


















