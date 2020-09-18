class Parent(object):
    x = 1
class Child1(Parent):
    pass
class Child2(Parent):
    pass
print(Parent.x, Parent1.x, Parent2.x)
Child1.x = 2
print(Parent.x, Parent1.x, Parent2.x)
parent.x = 3
print(Parent.x, Parent1.x, Parent2.x)
