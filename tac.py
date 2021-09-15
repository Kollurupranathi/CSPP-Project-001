"""Implementing the tac shell command in python."""
#the first line is a comment
import sys
#importing sys library using "import" keyword
from lib.helper import tac, readfile
#Importing "cat" "readfile" functions from helper library using "from" "import" keywords
TEXT = None
#TEXT is a variable which is initialized with none
ARG_CNT = len(sys.argv) - 1
#length is a function containing a predefined argument "sys.argv" and it is used to length of the file
#ARG_CNT is a variable assigned with len(sys.argv) minus one
if ARG_CNT == 0:
    TEXT = sys.stdin.read()
#"if" is a conditional statement used to perform multiple outcomes of a previous step
# if the value of ARG_CNT varialble is zero, the condition will be true. This makes to execute the next line
#As the condition is true, sys.stdin.read() is stored in a variable named "TEXT"
if ARG_CNT == 1:
    filename = sys.argv[1]
    TEXT = readfile(filename)
#if the value of ARG_CNT variable is one, the condition will be true. This makes to execute the next line
#As the condition is true, sys.argv[1] is stored in a variable named "filename" 
# read(filename) is stored in a variable named "TEXT"
if ARG_CNT > 1:
    print(sys.argv[0], "doesn't handle more than one argument")
#if the value of ARG_CNT varialble greater than one, the condition will be true. 
#This makes to execute the next line
#print is a function used to print the data given in it
#Here, it prints "sys.argv[0], "doesn't handle more than one argument""
print(tac(TEXT))
#print the function tac containing TEXT as an argument
#it will print all the lines in the file from bottom to top
