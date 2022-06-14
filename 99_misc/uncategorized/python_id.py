# Ref: https://www.journaldev.com/22925/python-id
# Python id() value is guaranteed to be unique and constant for an object.
# We can use this to make sure two objects are referring to the same object in memory or not.
# 'is' operator is the alternatives to check whether two objects refers to the same
#

def id_int_obj():
    # int objects
    a = 1000
    b = 1000
    c = 10
    d = 12 - 2

    # Notice that id() value of ‘a’ and ‘b’ are same, they have the same integer value.
    print(id(a))
    print(id(b))
    print(id(c))
    print(id(d))

    ll = [1000, 10, c, d]
    print("ll:", id(ll))
    print("ll[0]:", id(ll[0]))
    print("ll[1]:", id(ll[1]))
    print("ll[2]:", id(ll[2]))
    print("ll[3]:", id(ll[3]))

def id_float_obj():
    # float objects
    a = 10.1
    b = 10.1
    c = 11.0
    d = 12.0

    # Notice that id() value of ‘a’ and ‘b’ are same, they have the same integer value.
    print(id(a))
    print(id(b))
    print(id(c))
    print(id(d))


def id_mutable_obj():
    # id() with mutable objects

    # tuples
    t = ('A', 'B', 2-1)
    print(id(t))

    t1 = ('A', 'B', 1)
    print(id(t1))

    # strings
    s1 = 'ABC'
    s2 = 'ABC'
    print(id(s1))
    print(id(s2))

    # Caching can work only with immutable objects, notice that integer, string, tuples are immutable.
    # So Python implementation can use caching to save memory space and improve performance.

    # dict
    d1 = {"A": 1, "B": 2}
    d2 = {"A": 1, "B": 2}
    print(id(d1))
    print(id(d2))

def id_np():
    import numpy as np

    ll = np.array([10, 10, 999, 999])
    print("ll:", id(ll))

    x, y = id(ll[0]), id(ll[1])
    print(x, y)
    print("ll[0]:", id(ll[0]))
    print("ll[1]:", id(ll[1]))
    print("ll[2]:", id(ll[2]))
    print("ll[3]:", id(ll[3]))






# id_int_obj()
# id_float_obj()
# id_mutable_obj()
id_np()