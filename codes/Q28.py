class Solution(object):
    def strStr(self, haystack: str, needle: str) -> int:
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        a = len(haystack)
        b = len(needle)
        
        i = 0
        j = 0
        for i in range(a):
            if (haystack[i] == needle[j]):
                j += 1
            else:
                j = 0
            i += 1
            if j == b-1:
                return i-j
        return -1

    def strStrEditted(self, haystack: str, needle: str) -> int:
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        a = len(haystack)
        b = len(needle)

        firstLetter = []
        needle0 = needle[0]

        for i in range(a):
            if haystack[0] == needle0:
                firstLetter.append(i)
            
        # i = 0
        j = 0
        if len(firstLetter) > 0:
            for i in firstLetter:
                for d in range(i,a)
                    if (haystack[d] == needle[j]):
                        j += 1
                    else:
                        j = 0
                        break
                    # a += 1
                    if j == b-1:
                        return i-j
        return -1
        
