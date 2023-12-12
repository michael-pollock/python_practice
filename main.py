import sys

file = open('test.txt', 'r+')
print("Name of the file: ", file.name)
print("Closed: ", file.closed)
print("Opening mode: ", file.mode)
file.close()


