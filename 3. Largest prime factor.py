"""
The prime factors of 13195 are 5, 7, 13 and 29.
What is the largest prime factor of the number 600851475143?
"""


def simpledev(n):
    answer = []
    d = 2
    while d * d <= n:
        if n % d == 0:
            answer.append(d)
            n //= d
        else:
            d += 1
    if n > 1:
        answer.append(n)
    return answer


print(simpledev(600851475143))
