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
        
