
try:
    class_file = open("class.py")
except BaseException as msg:
    print("Error Message: ", msg)
else:
    print(class_file.read())

class_file.close()

print("classFile: isClosed: ", class_file.closed)

print(" > open: using block")

with open("class.py") as opFile:
    print("opFile: ", opFile.read())

print("opFile: isClosed: ", opFile.closed)


