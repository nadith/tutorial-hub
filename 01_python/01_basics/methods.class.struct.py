# -*- coding: utf-8 -*-

###################################################################################################
# Method Objects
###################################################################################################
# Functions are first class objects in Python: http://simeonfranklin.com/blog/2012/jul/1/python-decorators-in-12-steps/
# This is simply the observation that in Python, functions are objects like everything else. Ah, 
# function containing variable, you’re not so special!
"""
>>> issubclass(int, object) # all objects in Python inherit from a common baseclass
True
>>> def foo():
...     pass
>>> foo.__class__
<type 'function'>
>>> issubclass(foo.__class__, object)
True
"""

###################################################################################################
# User-defined function object
###################################################################################################
# Ref: https://docs.python.org/3/reference/datamodel.html
# A user-defined function object is created by a function definition (see section Function definitions). 
# It should be called with an argument list containing the same number of items as the function’s
# formal parameter list.

# Attributes
# __doc__	        The function’s documentation string, or None if unavailable; not inherited by subclasses
# __name__	        The function’s name
# __qualname__	    The function’s qualified name
# __module__	    The name of the module the function was defined in, or None if unavailable.
# __defaults__	    A tuple containing default argument values for those arguments that have defaults, or None if no arguments have a default value
# __code__	        The code object representing the compiled function body.	Writable
# __globals__	    A reference to the dictionary that holds the function’s global variables — the global namespace of the module in which the function was defined. Read-only
# __dict__	        The namespace supporting arbitrary function attributes.
# __closure__	    None or a tuple of cells that contain bindings for the function’s free variables. Read-only
# __annotations__	A dict containing annotations of parameters. The keys of the dict are the parameter names, and 'return' for the return annotation, if provided.
# __kwdefaults__	A dict containing defaults for keyword-only parameters.


###################################################################################################
# Instance method object
###################################################################################################
# An instance method object combines a class, a class instance and any callable object (normally a user-defined function).

# Special read-only attributes:
# __self__ is the class instance object, 
# __func__ is the function object; 
# __doc__ is the method’s documentation (same as __func__.__doc__); 
# __name__ is the method name (same as __func__.__name__); 
# __module__ is the name of the module the method was defined in, or None if unavailable.

# Ref: https://julien.danjou.info/blog/2013/guide-python-static-class-abstract-methods
# if you wanted to know which object this bound method is bound to? Here's a little trick:
"""
>>> m = Pizza(42).get_size
>>> m.__self__
<__main__.Pizza object at 0x7f3138827910>
>>> m == m.__self__.get_size
True
"""


###################################################################################################
# Generator functions
###################################################################################################
# A function or method which uses the yield statement (see section The yield statement) is called a 
# generator function. Such a function, when called, always returns an iterator object which can be 
# used to execute the body of the function: calling the iterator’s iterator.__next__() method will 
# cause the function to execute until it provides a value using the yield statement. When the function 
# executes a return statement or falls off the end, a StopIteration exception is raised and the 
# iterator will have reached the end of the set of values to be returned.

###################################################################################################
# Coroutine functions
###################################################################################################
# A function or method which is defined using async def is called a coroutine function. Such a function, 
# when called, returns a coroutine object. It may contain await expressions, as well as async with and
# async for statements. See also the Coroutine Objects section.

###################################################################################################
# Asynchronous generator functions
###################################################################################################
# A function or method which is defined using async def and which uses the yield statement is called 
# a asynchronous generator function. Such a function, when called, returns an asynchronous iterator 
# object which can be used in an async for statement to execute the body of the function.

# Calling the asynchronous iterator’s aiterator.__anext__() method will return an awaitable which when 
# awaited will execute until it provides a value using the yield expression. When the function executes 
# an empty return statement or falls off the end, a StopAsyncIteration exception is raised and the 
# asynchronous iterator will have reached the end of the set of values to be yielded.

###################################################################################################
# Nested functions
###################################################################################################
"""
>>> def outer():
...     x = 1
...     def inner():
...         print x
...     inner()
...
>>> outer()
"""

###################################################################################################
# Decorators
###################################################################################################
# A decorator is just a callable that takes a function as an argument and returns a replacement function. 
# We’ll start simply and work our way up to useful decorators.
"""
def outer(some_func):
    def inner():
        print("before some_func")
        ret = some_func()
        return ret + 1
    return inner

def foo():
    return 1

>>> decorated = outer(foo)
>>> decorated()
before some_func
2
"""

# or equivalently with decorator notation

"""
@outer
def foo():
    return 1

>>> foo()
before some_func
2
"""
###################################################################################################
# Decorators: Multiple decorators
###################################################################################################
"""
@dec2
@dec1
def func(arg1, arg2, ...):
    pass
"""

# This is equivalent to:

"""
def func(arg1, arg2, ...):
    pass

func = dec2(dec1(func))
"""
###################################################################################################
# Decorators: Decorators with parameters (decorator replaced with a decorator)
###################################################################################################
"""
def decorator(dparam1, dparam2): # decorator(*args)
    def new_decorator(some_func):
        def inner():
            print("before some_func")
            ret = some_func()
            return ret + 1
        return inner
    return new_decorator

>>> ndecorator = decorator('dparam1', 'dparam2')  # replaced with a new decorator, ndecorator => new_decorator
>>> decorated = ndecorator(foo)  # decorated => inner
>>> decorated()
before some_func
2
"""

# or equivelantly with decorator notation

"""
@decorator('dparam1', 'dparam1')
def foo():
    return 1

>>> foo()
before some_func
2
"""

###################################################################################################
# Got cha !!!!
"""
def decorator(dparam1, dparam2): # decorator(*args)
    def new_decorator(some_func):
        def inner():
            print("before some_func")
            ret = some_func()
            return ret + 1
        return inner
    return new_decorator

@decorator('dparam1', 'dparam1') #1
def foo():
    return 1

>>> ndecorator = decorator('dparam1', 'dparam2')
>>> decorated = ndecorator(foo) # remember this foo is already decorated by #1
>>> decorated()
before some_func # from already decorated foo (by #1)
before some_func
3
"""
###################################################################################################
# Example 01
def decorator(func):
    print("Decorator: ARG: ", func);
    return func

@decorator
def test():
    print("TEST");


# Example 02
def decorator(*args):
    print(len(args))
    print(locals())
    return args[0] # the function 'test'

@decorator
def test(param1):
    print("TEST")

# Example 03 (GotCha, ERROR !)
def decorator(*args):   
    print(locals())
    return args[0] # will be 'param1'

@decorator('param1')
def test():
    print("TEST")

# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# TypeError: 'str' object is not callable


# Example 03 (CORRECT - replace the decorator with a new decorator)
def decorator(*args):   
    print(locals())
    def new_decorator(func):
        print(locals())
        return func
    return new_decorator

@decorator('param1') # => new_decorator, test = new_decorator(test) 
def test():
    print("TEST")



# Example 04 (Adding Attributes to Function)
"""
def attrs(**kwds):
    print(locals())
    def decorate(f):
        print(locals())
        for k in kwds:
            setattr(f, k, kwds[k])
        return f    
    return decorate

@attrs(version="2.2",
       author="Guido van Rossum")
def test(param):
    print("TEST")

>>> test.__dict__
{'author': 'Guido van Rossum', 'version': '2.2'}
"""
###################################################################################################
# Function Tools: wraps
###################################################################################################
# Ref: https://docs.python.org/3/library/inspect.html#introspecting-callables-with-the-signature-object
# https://stackoverflow.com/questions/308999/what-does-functools-wraps-do

from functools import wraps
def my_decorator(f):
    @wraps(f)
    def wrapper(*args, **kwds):
        print(locals())
        print('Calling decorated function')
        return f(*args, **kwds)
    return wrapper

@my_decorator
def example(i):
   """Docstring"""
   print('Called example function')


# Example 05 (Accepted params to Function)
# Ref: https://www.safaribooksonline.com/library/view/python-cookbook-3rd/9781449357337/ch09s07.html
from inspect import signature
from functools import wraps

def typeassert(*ty_args, **ty_kwargs):
    def decorate(func):
        # If in optimized mode, disable type checking
        if not __debug__:
            return func

        # Map function argument names to supplied types
        sig = signature(func)
        bound_types = sig.bind_partial(*ty_args, **ty_kwargs).arguments

        @wraps(func)
        def wrapper(*args, **kwargs):
            bound_values = sig.bind(*args, **kwargs)
            # Enforce type assertions across supplied arguments
            for name, value in bound_values.arguments.items():
                if name in bound_types:
                    if not isinstance(value, bound_types[name]):
                      raise TypeError(
                        'Argument {} must be {}'.format(name, bound_types[name])
                        )
            return func(*args, **kwargs)
        return wrapper
    return decorate

@typeassert(int, int)
def add(x, y):
    return x + y

>>> add(2, 3)
5
>>> add(2, 'hello')
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "contract.py", line 33, in wrapper
TypeError: Argument y must be <class 'int'>


###################################################################################################
# Sample class
###################################################################################################
# static variables http://stackoverflow.com/questions/68645/static-class-variables-in-python
class A:
    def __init__(self, param1):
        pass

    @property
    def imdb(self):
        return self.__imdb

    @imdb.setter
    def imdb(self, value):
        self.im_dim1, self.im_dim2, self.im_nch, self.im_count = np.uint16(value.shape)
        self.__imdb = value

    @imdb.deleter
    def imdb(self):
        del self.__imdb     

class B(A):
    
    # Public Static variable
    var = 100
    
    # Private Static variable
    __var = 10
    
    # Constructor
    def __init__(self):
        super().__init__(10) # (Python 3.x compatible) but same as  super(A, self).__init__(10)  or A.__init__(self, 10) (Python 2.x compatible)
        print('Costructor')
        print(self.var)                     # static variable via self instance
        self.var = 'instance'               # instance variable defnition shadows static
        self.__pvtvar = 'instance_private'  # private instance variable
        print(self.var)
        print(A.__var) 
        
        
#ii = A();

##
# Multiple Inheritance: http://python-history.blogspot.com.au/2010/06/method-resolution-order.html
##

##
# Static / Class / Instance / Abstract Methods: https://julien.danjou.info/blog/2013/guide-python-static-class-abstract-methods
##

##
# Python does not support method overloading officially, 
# for alternatives refer: http://stackoverflow.com/questions/6434482/python-function-overloading
##


###################################################################################################
# type Class / Meta Class / Class
###################################################################################################
# Ref: https://blog.ionelmc.ro/2015/02/09/understanding-python-metaclasses/
# A class is an object, and just like any other object, it's an instance of something: a metaclass. 
# The default metaclass is type. Unfortunately, due to backwards compatibility, type is a bit confusing: 
# it can also be used as a function that return the class [13] of an object:

# Dynamic class type creation
X = type('Alexnet', (object,), dict(a=1)) # returns a type object
Y = type('Alexnet', (object,), dict(a=1)) # returns a type object

a = X()
b = Y()
isinstance(X, type)         # True (X is a instance of meta class type)
isinstance(a, X)            # True
isinstance(a, Y)            # False
type(b) == Y                # True (type(b) : returns the class Object Y associated with b instance)
isinstance(type(b), type)   # True (type(b) : is a instance of the class Object Y thus a instance of class type)
print(type.__dict__)
type('abc') == 'str'        # False (type('abc') : returns the class Object associated with string instance)
type('abc') == type('def')  # True
type('abc') == str          # True (str is the class Object for string instances)

##### IMPORTANT #####
from Models.Alexnet import Alexnet
alex = Alexnet()    # alex is a instance of Models.Alexnet.Alexnet type, and Models.Alexnet.Alexnet type is a instance of type
isinstance(alex, Alexnet)
isinstance(Alexnet, type)

###################################################################################################
# Alternative struct implementation: http://stackoverflow.com/questions/35988/c-like-structures-in-python
###################################################################################################
class Bunch:
def __init__(self, **kwds):
    self.__dict__.update(kwds)
>>> mystruct = Bunch(field1=value1, field2=value2)

class Employee:
    pass

>>> e = Employee()
>>> Employee.age = 10   # static variable (check Employee.__dict__)
>>> emp1.age            # Access static variable via an instance 
10

# You can add, remove, or modify attributes of classes and objects at any time
>>> emp1.age = 7  # Add an 'age' attribute.
>>> emp1.age = 8  # Modify 'age' attribute.
>>> del emp1.age  # Delete 'age' attribute.

# NOTE: Got Cha !!
>>> ref_to_cls_obj = Employee # Does not create an object but a reference to Employee 'class object'
                            # Remember, class itself is an object


###################################################################################################
# collections.namedtuple(typename, field_names[, verbose=False][, rename=False])
# Ref: https://docs.python.org/2/library/collections.html#namedtuple-factory-function-for-tuples-with-named-fields
###################################################################################################
>>> Point = namedtuple('Point', ['x', 'y'], verbose=True)
>>> p = Point(11, y=22)     # instantiate with positional or keyword arguments
>>> p[0] + p[1]             # indexable like the plain tuple (11, 22)
33
>>> x, y = p                # unpack like a regular tuple
>>> x, y
(11, 22)
>>> p.x + p.y               # fields also accessible by name
33
>>> p                       # readable __repr__ with a name=value style
Point(x=11, y=22)





###################################################################################################
# Inner classes
# Ref: http://stackoverflow.com/questions/1765677/python-nested-classes-scope
###################################################################################################
# WRONG !
class OuterClass:
     outer_var = 1
     class InnerClass:
           inner_var = outer_var

# This isn't quite the same as similar things work in other languages, and uses global lookup instead 
# of scoping the access to outer_var. (If you change what object the name Outer is bound to, then this 
# code will use that object the next time it is executed.)

# CORRECT
class Outer(object):
  outer_var = 1

  class Inner(object):
    @property
    def inner_var(self):
      return Outer.outer_var

class OuterClass:
    outer_var = 1

    class InnerClass:
        pass
    InnerClass.inner_var = outer_var

# The problem you encountered is due to this:
# A block is a piece of Python program text that is executed as a unit. The following are blocks:
# a module, a function body, and a class definition.
# (...)
# A scope defines the visibility of a name within a block.
# (...)
# The scope of names defined in a class block is limited to the class block; it does not extend 
# to the code blocks of methods – this includes generator expressions since they are implemented 
# using a function scope. This means that the following will fail:

class A:  
    a = 42
    b = list(a + i for i in range(10))
# Ref: http://docs.python.org/reference/executionmodel.html#naming-and-binding