class Parent(object):
    def __init__(self, name):
        print('Parent', name)

class Parent2(object):
    def __init__(self, name):
        print('Parent2', name)

class Child(Parent2, Parent):
    def __init__(self):
        Parent2.__init__(self, 'max')
        Parent.__init__(self, 'tom')
        print('Child')

child = Child()