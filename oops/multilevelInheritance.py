class GrandFather:
    def __init__(self, a):
        self.a = a

    def displayGrandFather(self):
        print("I am GrandFather : A : ", self.a)


class Father(GrandFather):
    def __init__(self, b):
        self.b = b

    def displayFather(self):
        print("I am Father : B : ", self.b)


class Son(Father):
    def __init__(self, c):
        Father.__init__(self, 15)
        GrandFather.__init__(self, 10)
        self.c = c

    def displaySon(self):
        super().displayGrandFather()
        super().displayFather()
        print("I am Son : C : ", self.c)


s = Son(25)
s.displaySon()
