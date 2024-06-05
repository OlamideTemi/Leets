"""
Given a non-negative integer x, return the square root of x rounded down to the nearest integer. The returned integer should be non-negative as well.

You must not use any built-in exponent function or operator.

For example, do not use pow(x, 0.5) in c++ or x ** 0.5 in python.
 

Example 1:

Input: x = 4
Output: 2
Explanation: The square root of 4 is 2, so we return 2.
Example 2:

Input: x = 8
Output: 2
Explanation: The square root of 8 is 2.82842..., and since we round it down to the nearest integer, 2 is returned.
 

Constraints:

0 <= x <= 231 - 1
"""


def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """

        a = 0
        l =x
        if x == 0:
            return 0
        elif x == 1:
            return 1

        while True:

            sqrt = (l+a) // 2
            y = sqrt + 1

            temp = sqrt * sqrt
            temp2 = y * y

            if (temp == x) or (temp < x and temp2 > x):
                return sqrt
            else:
                if temp < x:
                    a = sqrt
                elif temp > x:
                    l = sqrt


def mySqrtv2( x ):
    """
    :type x: int
    :rtype: int
        """
    if x == 0:
        return 0
    elif x == 1:
        return 1
    
    prime = [2,3,5,7,11,13,17,19, 23, 31, 37]

    square = [x*x for x in prime]

    sqrt = 1
    length = len(prime)

    x_copy = x
    i = 0
    while i < length:
        if x_copy % square[i] == 0:
            sqrt = sqrt * prime[i]
            x_copy = x_copy/square[i]
        else:
            i+=1

    return sqrt
        
