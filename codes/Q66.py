ss Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """

        length = len(digits)

        num = 0

        for i in range(length):
            num = num + (digits[i] * (10**(length-i-1)))
        result = num + 1

        str_digits = str(result)
        result_arr = [ int(x) for x in str_digits ]

        return result_arr
