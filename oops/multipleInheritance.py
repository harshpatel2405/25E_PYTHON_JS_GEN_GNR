class Parent1:
    def __init__(self, a):
        self.a = a

    def displayParent1(self):
        print("(Parent1) A : ", self.a)


class Parent2:
    def __init__(self, b):
        self.b = b

    def displayParent2(self):
        print("(Parent2) B : ", self.b)


class Child(Parent1, Parent2):
    def __init__(self, a, b, c):
        Parent1.__init__(self, a)
        Parent2.__init__(self,b)
        self.c = c

    def displayChild(self):
        super().displayParent1()
        super().displayParent2()
        print("(Child)   C : ", self.c)


c = Child(10, 20, 30)
c.displayChild()
