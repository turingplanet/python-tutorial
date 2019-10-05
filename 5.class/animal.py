class Animal():
    def __init__(self, name):
        self.name = name
    def greet(self):
        print(f'Hello, I am {self.name}.')

class Dog(Animal):
    def greet(self):
        print(f'WangWang.., I am {self.name}.') 

class Cat(Animal):
    def greet(self):
        print(f'MiaoMiao.., I am {self.name}')