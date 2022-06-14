import itertools


# Make an iterator returning elements from the iterable and saving a copy of each. When the 
# iterable is exhausted, return elements from the saved copy. Repeats indefinitely. 
# Roughly equivalent to:
# cycle('ABCD') --> A B C D A B C D A B C D ...
t = itertools.cycle([None]) # will 
print(list(zip([1, 2, 3, 4], t)))

t = itertools.cycle(['A', 'B']) # will 
print(list(zip([1, 2, 3, 4], t)))



def accumulate():

    # import the itertool module 
    # to work with it
    import itertools
    
    # import operator to work 
    # with operator
    import operator
    
    # creating a list GFG
    GFG = [1, 2, 3, 4, 5]
    
    # using the itertools.accumulate() 
    result = itertools.accumulate(GFG, 
                                operator.mul)
    
    # printing each item from list
    for each in result:
        print(each)
        
        
    result = itertools.accumulate(GFG)  # default is addition accumulation
    for each in result:
        print(each)
            
accumulate()