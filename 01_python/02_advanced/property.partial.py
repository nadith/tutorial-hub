from functools import partial

def multiply(x,y):
    return x * y

# Ref: https://www.learnpython.org/en/Partial_functions
# create a new function that multiplies by 2
dbl = partial(multiply,2)
print(dbl(4))


# Ref: https://www.programiz.com/python-programming/methods/built-in/property
class Person:
    def __init__(self, name):
        self._name = name

    @property
    def name(self):
        print('Getting name')
        return self._name

    @name.setter
    def name(self, value):
        print('Setting name to ' + value)
        self._name = value

    @name.deleter
    def name(self):
        print('Deleting name')
        del self._name

    def __getitem__(self, index):
        return list(range(index))

p = Person('Adam')
print('The name is:', p.name)
p.name = 'John'
# del p.name
print(p[5])

####################################################################################################
# Simple example (fget, fset, del)
test = property(lambda x: print(x))
test.fget(10)

# Complex example
def add_props(f, g=None, n=2):  # f is the fget, g is fset
    "Create properties passing each of `range(n)` to f"
    if g is None: return (property(partial(f,i)) for i in range(n))
    return (property(partial(f,i), partial(g,i)) for i in range(n))

train, valid = add_props(lambda i,x: print(i, x))
print(train, valid)
train.fget(10)
valid.fget(20)

Person.train, Person.valid = add_props(lambda i,x: print(i, x))

print(p.train)  # this will call property's fget function with i = 0 (from partial), x = p object
print(p.valid)  # this will call property's fget function with i = 1 (from partial), x = p object
# 0 <__main__.Person object at 0x000001DA27C30790>
# None
# 1 <__main__.Person object at 0x000001DA27C30790>
# None

print(Person.train)  # <property object at 0x000001DA27C50720>
print(Person.train.fget(p))  # 0 <__main__.Person object at 0x000001DA27C30790>
                             # None
# IMPORTANT
# None is because, print(...) expects a value to be returned

Person.train, Person.valid = add_props(lambda i,x: x[5]) 
print(p.train[0])
print(p.valid[0])

s = 0



