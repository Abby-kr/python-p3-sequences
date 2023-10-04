#!/usr/bin/env python3

def print_fibonacci(length):
    num1 = 0
    num2 = 1
    sum = 0
    if length == 0:
        print([])
    elif length == 1:
        print([0])
    else:
        fibonacci_list = [0,1]
        for i in range(2,length):
            sum = num1 + num2
            num1 = num2
            num2 = sum
            fibonacci_list.append(sum)
        print(fibonacci_list)