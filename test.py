import time
from tkinter import *


def print_lines():
    print(input("Enter Line: "))


def suv(massive):
    a = 0
    for i in massive:
        a = a + i
    return a


def sun(massive):
    a = 1
    for i in massive:
        a = a * i
    return a


def reverse(line):
    rev = line[::-1]
    return rev


def check_line(line):
    reverse_line = line[::-1]
    if line == reverse_line:
        print("Its Ok")
    else:
        print("Error")


def histogram(massive):
    for i in massive:
        time.sleep(0.5)
        print(i * "*")


print(suv([1, 2, 3, 4]))
print(sun([1, 2, 3, 4]))
print(reverse("Line"))
print(check_line("lil"))
print(histogram(range(1, 6)))
