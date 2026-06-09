# sys modulke gives us ability to use command line arguments.

import sys

# print("hello, my name is", sys.argv[1])

# PS C:\Users\Lenovo\OneDrive\Documents\GitHub\python-journey\4. Libraries> python name.py SHamit

# hello, my name is SHamit


# But what if the user puts just 
# PS C:\Users\Lenovo\OneDrive\Documents\GitHub\python-journey\4. Libraries> python name.py
# then it'll lead to index error as the list doesn't have 1st argument. It just has sys.argv[0] = "name.py" , so:

# try:
#     print("hello, my name is", sys.argv[1])
# except IndexError:
#     print("Too few arguments.")


# To clearly tell the user about the issue:
# if len(sys.argv) < 2:
#     print("Too less arguments.")
# elif len(sys.argv) > 2:
#     print("Too many arguments.")
# else:
#     print("hello, my name is", sys.argv[1])

# PS C:\Users\Lenovo\OneDrive\Documents\GitHub\python-journey\4. Libraries> python name.py
# Too less arguments.
# PS C:\Users\Lenovo\OneDrive\Documents\GitHub\python-journey\4. Libraries> python name.py Shamit MOllya
# Too many arguments.
# PS C:\Users\Lenovo\OneDrive\Documents\GitHub\python-journey\4. Libraries> python name.py Shamit MOllya
# Too many arguments.
# PS C:\Users\Lenovo\OneDrive\Documents\GitHub\python-journey\4. Libraries> python name.py Shamit 
# hello, my name is Shamit
# PS C:\Users\Lenovo\OneDrive\Documents\GitHub\python-journey\4. Libraries> python name.py "Shamit Moolya"
# hello, my name is Shamit Moolya


# But the actual piece of execution that matters is hiding in else block here which we don't want so, we can delegate tasks as:

# Checks for errors
# if len(sys.argv) < 2:
#     print("Too less arguments.")
# elif len(sys.argv) > 2:
#     print("Too many arguments.")

# # Prints name tags
# print("hello, my name is", sys.argv[1])

#But now this will introduce a new bug that is IndexError because if we input :

# PS C:\Users\Lenovo\OneDrive\Documents\GitHub\python-journey\4. Libraries> python name.py       
# Too less arguments.
# Traceback (most recent call last):
#   File "C:\Users\Lenovo\OneDrive\Documents\GitHub\python-journey\4. Libraries\name.py", line 49, in <module>
#     print("hello, my name is", sys.argv[1])
#                                ~~~~~~~~^^^
# IndexError: list index out of range

# the program give out "too less arguments" but still tries to implement print("hello, my name is", sys.argv[1]) which leads to the erropr as sys.argv[1] doesn't exit.

# So we want to exit prematurely once we have the "too few arguments" so:

# Checks for errors
# if len(sys.argv) < 2:
#     sys.exit("Too less arguments.")
# elif len(sys.argv) > 2:
#     sys.exit("Too many arguments.")

# # Prints name tags
# print("hello, my name is", sys.argv[1])


# If you want to take as any  names as i can take:
# if len(sys.argv) < 2:
#     sys.exit("Too less arguments.")

# for arg in sys.argv:
#     print("hello, my name is", arg)

# But i'll give us: 

# PS C:\Users\Lenovo\OneDrive\Documents\GitHub\python-journey\4. Libraries> python name.py Shamit Nathan David Manekshaw
# hello, my name is name.py
# hello, my name is Shamit
# hello, my name is Nathan
# hello, my name is David
# hello, my name is Manekshaw

# But we dont want "hello, my name is name.py"
# so we will slice the list. i.e. get a subset of the list set.

# if len(sys.argv) < 2:
#     sys.exit("Too less arguments.")

# for arg in sys.argv[1:]:
#     print("hello, my name is", arg)


# To slice the last person :
if len(sys.argv) < 2:
    sys.exit("Too less arguments.")

for arg in sys.argv[1:-1]:
    print("hello, my name is", arg)