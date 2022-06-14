# -*- coding: utf-8 -*-

###################################################################################################
# Python data model (mutable and immutable objects)
###################################################################################################
#http://stackoverflow.com/questions/8056130/immutable-vs-mutable-types
#https://docs.python.org/3/reference/datamodel.html
# You have to understand that Python represents all its data as objects. Some of these objects like lists and dictionaries are mutable, 
# meaning you can change their content without changing their identity. Other objects like integers, floats, strings and tuples are 
# objects that can not be changed. An easy way to understand that is if you have a look at an objects ID.

#Below you see a string that is immutable. You can not change its content. It will raise a TypeError if you try to change it. Also, 
#if we assign new content, a new object is created instead of the contents being modified.

>>>s = "abc"
>>>id(s)
#4702124
>>> s[0] 
#'a'
>>>s[0] = "o"
#Traceback (most recent call last):
#  File "<stdin>", line 1, in <module>
#TypeError: 'str' object does not support item assignment
>>> s = "xyz" # compile-time
>>>id(s)
#4800100
>>> s += "uvw" # operator evaluation: run-time
>>> id(s)
#4800500
#You can do that with a list and it will not change the objects identity

>>> i = [1,2,3]
>>>id(i)
#2146718700
>>> i[0] 
#1
>>> i[0] = 7
>>> id(i)
#2146718700

###################################################################################################
# is vs ==
###################################################################################################
# is tests object identity. Do the two operands refer to the same object? - id(obj1) == id(obj2)
# == tests equality of value. Do the two operands have the same value?

##
>>> a = [1, 2, 3]
>>> b = a
>>> b is a 
True
>>> b == a
True
>>> b = a[:] # The return value is a new list containing all the elements of the list ref:http://www.diveintopython.net/native_data_types/lists.html
>>> b is a
False
>>> b == a
array([ True,  True,  True])

# A little example on how is and == are involved in immutable types. Try that:
a = 19998989890
b = 19998989889 +1
>>> a is b
False
>>> a == b
True
# is compares two objects in memory, == compares their values. For example, you can see that small integers are cached by Python, but not big integers:
c = 1
b = 1
>>> b is c
True
>>> float(1) is float(1) # non integers are never cached
False

# Direct comparisons: Instantiation of primitive types like bool, int, string(with some exception), NoneType having a 
# same value will always be in the same memory location.
# http://stackoverflow.com/questions/26595/is-there-any-difference-between-foo-is-none-and-foo-none
# http://stackoverflow.com/questions/28329498/why-does-a-space-affect-the-identity-comparison-of-equal-strings
# i.e Direct comparisons (instantiation happen in the same line)
>>> int(1) is int(1) # small integers
True
>>> int(10000000) is int(10000000) # large integers (no problem)
True
>>> bool(1) is bool(2) # True, False objects are singletons (like None object)
True
>>> bool(0) is bool(0)
True
>>> bool(0)
False
>>> bool(1)
True

#
# Indirect comparisons (instantiation happen in the another line)
#
>>> i1 = 10000000 # or int(10000000) # Large integers (not cached)
>>> i2 = int(10000000) # Large integers (not cached)
>>> i1 is i2
False

# Only EXCEPTION in python !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
>>> float('nan') is float('nan') 
True
>>> float('nan') == float('nan') 
False
# How to check for NaN in python?
# http://stackoverflow.com/questions/944700/how-to-check-for-nan-in-python
>>> math.isnan(float('nan'))

###################################################################################################
# The internals of Python string interning
###################################################################################################
# Ref: http://stackoverflow.com/questions/28329498/why-does-a-space-affect-the-identity-comparison-of-equal-strings
# The python interpreter caches some strings based on certain criteria, the first abc string is cached 
# and used for both but the second is not. It is the same for small ints from -5 to 256.
# Because the strings are interned/cached assigning a and b to "abc" makes a and b point to the 
# same objects in memory so using is, which checks if two objects are actually the same object, 
# returns True.
# The second string abc abc is not cached so they are two entirely different object in memory so out 
# identity check using is returns False. This time a is not b. They are both pointing to different 
# objects in memory.

In [43]: a = "abc" # python caches abc
In [44]: b = "abc" # it reuses the object when assigning to b
In [45]: id(a)
Out[45]: 139806825858808    # same id's, same object in memory
In [46]: id(b)
Out[46]: 139806825858808    
In [47]: a = 'abc abc'   # not cached  
In [48]: id(a)
Out[48]: 139806688800984    
In [49]: b = 'abc abc'    
In [50]: id(b)         # different id's different objects
Out[50]: 139806688801208
# The criteria for caching strings is if the string only has letters, underscores and numbers in the 
# string so in your case the space does not meet the criteria.

# EXCEPTION (for all immutable objects)
# Using the interpreter there is one case where you can end up pointing to the same object even when 
# the string does not meet the above criteria, multiple assignments.
In [51]: a,b  = 'abc abc','abc abc' # or a,b = 257, 257 or a,b = int(257), 257

In [52]: id(a)
Out[52]: 139806688801768

In [53]: id(b)
Out[53]: 139806688801768

In [54]: a is b
Out[54]: True

###################################################################################################
# Native string interning (The criteria for caching strings)
###################################################################################################
# Ref: http://guilload.com/python-string-interning/
# Under certain conditions, strings are natively interned. Recall the first example, if I had written 
# foo instead of foo!, the strings s1 and s2 would have been interned “automatically”:
>>> 'foo' is 'foo'
True
>>> 'foo!' is 'foo!'
True
>>> 'foo' + 'bar' is 'foobar'
True
>>> ''.join(['f']) is ''.join(['f'])
True
>>> ''.join(['f', 'o', 'o']) is ''.join(['f', 'o', 'o']) # run-time operation
False
>>> 'a' * 20 is 'aaaaaaaaaaaaaaaaaaaa'
True
>>> 'a' * 21 is 'aaaaaaaaaaaaaaaaaaaaa'
False
>>> 'foooooooooooooooooooooooooooooo' is 'foooooooooooooooooooooooooooooo'
True

# After looking at these examples, you have to admit that it is hard to tell on which basis a string is 
# natively interned or not. So let’s read some more CPython code and figure it out!

#
# Fact 1: all length 0 and length 1 strings are interned ##########################################
#
>>> '!' is '!'
True
#
# Fact 2: strings are interned at compile time ####################################################
#
# The Python code you write is not directly interpreted and goes through a classic compilation chain which 
# generates an intermediate language called bytecode. Python bytecode is a set of instructions executed by a 
# virtual machine: the Python interpreter. The list of these instructions can be found here and you can find 
# out what instructions are run by a particular function or module, by using the dis module:

>>> import dis
>>> def foo():
...     print 'foo!'
...
>>> dis.dis(foo)
  2           0 LOAD_CONST               1 ('foo!')
              3 PRINT_ITEM
              4 PRINT_NEWLINE       
              5 LOAD_CONST               0 (None)
              8 RETURN_VALUE

# Fact 2.1: Compile time declared strings are interned while runtime produced strings are not interned
# Fact 2.2: strings that are not composed of ascii letters, digits or underscores, 
#           i.e. strings do not look like identifiers, will not be interned
PyCodeObject *
PyCode_New(int argcount, int nlocals, int stacksize, int flags,
           PyObject *code, PyObject *consts, PyObject *names,
           PyObject *varnames, PyObject *freevars, PyObject *cellvars,
           PyObject *filename, PyObject *name, int firstlineno,
           PyObject *lnotab)

           ...
           /* Intern selected string constants */
           for (i = PyTuple_Size(consts); --i >= 0; ) {
               PyObject *v = PyTuple_GetItem(consts, i);
               if (!PyString_Check(v))
                   continue;
               if (!all_name_chars((unsigned char *)PyString_AS_STRING(v)))
                   continue;
               PyString_InternInPlace(&PyTuple_GET_ITEM(consts, i));
           }

# In codeobject.c, the tuple consts contains the literals defined at compile time: booleans, floating-point numbers, 
# integers, and strings declared in your program. The strings stored in this tuple and not filtered out by the 
# all_name_chars function are interned.

#
# Fact 3:   Bytecode optimization produces more string constants ##################################
#           Operations take place in compile time vs runtime.
>>> 'foo' + 'bar' is 'foobar'  # the outcome of the string literal/constant concatenation is not performed at runtime but at compile time:
True
>>> str('foo') + 'bar' is 'foobar'  # the outcome of the string concatenation is performed at runtime but not at compile time:
True

# How? The penultimate source code compilation step produces a first version of bytecode. 
# This “raw” bytecode finally goes into a last compilation step called “peephole optimization”.
# The goal of this step is to produce more efficient bytecode by replacing some instructions by faster ones.

#
# Fact 4: Immutability required (but only work with strings and short integers, not with float or complex)
#

###################################################################################################
# peephole optimization
###################################################################################################
# 1) Constant folding
#
# One of the techniques applied during peephole optimization is called constant folding and consists 
# in simplifying constant expressions in advance. Imagine you are a compiler and you come across this line:

SECONDS = 24 * 60 * 60
# What can you do to simplify this expression and save some clock cycles at runtime? You are going to 
# substitute this expression by the computed value 86400. This is exactly what happens to the 'foo' + 'bar' 
# expression. Let’s define the foobar function and disassemble the corresponding bytecode:

>>> import dis
>>> def foobar():
...         return 'foo' + 'bar'
>>> dis.dis(foobar)
  2           0 LOAD_CONST               3 ('foobar')
              3 RETURN_VALUE
# See? No sign of the addition and the two initial constants 'foo' and 'bar'. If CPython bytecode was not 
# optimized, the output would have been the following:

>>> dis.dis(foobar)
  2           0 LOAD_CONST               1 ('foo')
              3 LOAD_CONST               2 ('bar')
              6 BINARY_ADD    
              7 RETURN_VALUE

# Ref: http://stackoverflow.com/questions/15541404/python-string-interning
# Note:  Python's peep-hole optimisation will pre-calculate arithmetic operations on constants 
# ("string1" + "s2", 10 + 3*20, etc.) at compile time, but limits resulting sequences to just 20 elements 
# (to prevent [None] * 10**1000 from overly expanding your bytecode).
>>> 'a' * 21 is 'aaaaaaaaaaaaaaaaaaaaa'
False
>>> 'fooooooooooooooooo'+'ooooooooooooo' is 'foooooooooooooooooooooooooooooo'
False
 
#
# 2) Direct constant comparison (no operators) - interned
#
>>> 'foooooooooooooooooooooooooooooo' is 'foooooooooooooooooooooooooooooo'
True
>>> 'foo!' is 'foo!'
True
#  NOTE: But in case there is a operation that results in a new string (non identifier like string), not interned !
>>> 'foo!' is 'foo' + '!' # compile-time, but not interned: results in a new string (non identifier like string)
False

#
# 3) Direct string comparison (no operators) - interned
#
>>> str("abcd") is str("abcd") # compile-time
True
>>> str("ab") + str("cd") is str("abcd") # run-time concatenation
False

###################################################################################################
# More Examples
###################################################################################################
>>> "string" is "string"
True
>>> "strin" + "g" is "string" # compile-time: constant folding
True
>>> s1 = "strin"
>>> s2 = "string"
>>> s1 + "g" is s2 # run-time concatenation, the result of which is not automatically interned:
False
>>> sys.intern(s2) is "string"
True
>>> s1 = str("abcd") # compile-time
>>> s2 = str("abcd") # compile-time
>>> s1 is s2
True
>>> str("aaa") is "aa" + "a" # compile-time
True
>>> "aaa" is "aa" + "a" # compile-time
True
s1 = 'foo!' # or str('foo!') - compile-time BUT no interning since it contains 'special characters'
s2 = 'foo!' # or str('foo!') - compile-time BUT no interning since it contains 'special characters'
>>> s1 is s2
False
>>> s1 = sys.intern('foo!') # to ensure that you're getting a reference to the same string
>>> s2 = sys.intern('foo!') # to ensure that you're getting a reference to the same string
>>> s1 is s2
True
>>> s1 is 'foo!' # s1 is not interned
False

#
# Immutable integer objects
#
>>> x = 257 # compile-time, not interned
>>> y = 257 # compile-time, not interned
>>> x is y
False
>>> x, y = 257, 257 # Exception of multiple assignment mentioned above
>>> x is y
True
>>> x, y = int(257), 257 # Exception of multiple assignment mentioned above
>>> x is y
True
>>> x, y = int(257), int(257) # Exception of multiple assignment mentioned above
>>> x is y
True
>>> int(257) is int(257) # direct constant comparison, int(...) do not result in new object
True
>>> int(257) is 257 # same as above
True
>>> int(257) is 256 + 1 # compile-time, but not interned: results in a new integer object (not short)
False
>>> x = int(257) # compile-time but not interned
>>> x is 257
False
>>> int('256') is int('256') # compile-time, interned: results in a new integer object (short)
True
>>> int('257') is int('257') # compile-time, but not interned: results in a new integer object (not short)
False


###################################################################################################
# Numpy Array Formulation
###################################################################################################
import numpy as np
a = np.array([1, 1, 1, 1])
b = np.array([10, 10, 10, 10])
c = np.array([100, 100, 100, 100])

A1 = np.array([[-1, -1, -1, -1], b, [100, 100, 100, 100]])
A2 = np.array([[-1, -1, -1, -1], [-2, -2, -2, -2], c])

# Equality
print("np.equal(A1[2], A2[2]):", np.equal(A1[2], A2[2]))
print("A1[2] == A2[2]:", A1[2] == A2[2])

# Object reference check (all return True)
print("id(A1) != id(A2):", id(A1) != id(A2))

# Numpy, id for axis in arrays are the same
print("A1:", id(A1))
for i in range(3):
    print("A1[" + str(i) +"]:", id(A1[i]))

print("A2:", id(A2))
for i in range(3):
    print("A2[" + str(i) +"]:", id(A2[i]))


print("Copying Values")
print("id(A1[2]) == id(A2[2]):", id(A1[2]) == id(A2[2]))
A1[2] = c  # Values will be copied
A1[2, 0] = 200
print("id(A1[2]) == id(A2[2]):", id(A1[2]) == id(A2[2]))

d = A1[2]
e = A1[2]

print("Slicing")
print("id(d) == id(e):", id(d) == id(e))


# Ref: https://stackoverflow.com/questions/49855586/numpy-array-memory-id
# Ref: https://stackoverflow.com/questions/40196986/numpy-arrays-changing-id

id(A1[2:3, 0:]) == id(A2[2])
id(A1[2]) == id(A2[2])
id(A1[2]) != id(c)