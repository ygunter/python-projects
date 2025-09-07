#!/usr/bin/env python37
# Line above useful for Unix-based
# operating systems like Linux and OSX.

# ex-3.py

a = 0
b = 1

print("\n***Using standard syntax***\n")
while b < 8:
    print("Before operations: \t", "a ", a, "  b ", b)
    a = b
    b = a+b
    print("After operations: \t", "a ", a,  "  b ", b)
    
print('\n')

print("***Using compact syntax***\n")
a, b = 0, 1
while b < 8:
    print("Before operations: \t", "a ", a, "  b ", b)
    a, b = b, a+b
    print("After operations: \t", "a ", a, "  b ", b)