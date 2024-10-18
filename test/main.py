import module
import module as mod
from module import *
from module import print_hello_world

a=5
b=2

print("[fun & loop: ] >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
for index in range(1, 5):
    print(index);

index = 0;
while index < 5:
    print(index)
    index += 1;
else:
    print("loop: is done");

def fun(var):
    print("Hello World")

fun(20);

print("type: ", type(index));
print("a^b: ", a ** b);
print("E(X): ", a // b);

print("[list : ] >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
list1 = [1, "hello", "World", 2]
list2 = [None] * 4

for element in list1:
    print(element);

for element in list2:
    print(element);

print("[variadic: ] >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")

def varFun(*args):
    for arg in args:
        print("args -> ", arg);

varFun(1, 2);

print("[Lambda: ] >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")

fun = lambda arg1, arg2: arg1 + arg2

print(fun(3, 4));

print("[import module:] >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
module.print_hello_world()
module.print_msg("msg: Hello, World!")

print("[import module as mode: ] >>>>>>>>>>>>>>>>>>>>>")
mod.print_hello_world()

print("[from module improt *: ] >>>>>>>>>>>>>>>>>>>>>>")
print_hello_world()

print("[print module members: ] >>>>>>>>>>>>>>>>>>>>>>")
print(dir(module))
