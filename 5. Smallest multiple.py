"""
2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?


2520 - самое маленькое число, которое делится без остатка на все числа от 1 до 10.

Какое самое маленькое число делится нацело на все числа от 1 до 20?

"""


def gcd(a, b): #НОД
    while b > 0:
        a, b = b, a % b
    return a

def lcm(a, b): #НОК
    return a * b // gcd(a, b)


d = 1
for i in range(2, 21):
    d = lcm(d, i)

print(d)
