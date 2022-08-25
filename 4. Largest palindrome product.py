"""
A palindromic number reads the same both ways.
The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.
Find the largest palindrome made from the product of two 3-digit numbers.

"""

polindrome = []
for i in range(999, 100, -1):
    for j in range(999, 100, -1):
        ij = i * j
        if str(ij)==str(str(ij)[::-1]):
            polindrome.append(ij)

print(max(polindrome))
