
class   Iterator:

    def __iter__(self):
        self.var=0
        return self

    def __next__(self):
        self.var += 1
        return self.var

aList = [1, 3, "Hello, World!"]

listIter = iter(aList)

it = iter(Iterator())

print(next(it))
print(next(it))
print(next(it))


# This exactly how [ for element in iterable ] works


#print(next(listIter))
#print(next(listIter))

# while True:

 #   print(listIter)

 #   try:
 #       next(listIter);

 #   except StopIterator:
 #       break
