class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """

        a = 0
        b = 0
        result = 1

        for i in range(1, n+1):
            a = b
            b = result
            result = a + b

        return result



"""
You are climbing a staircase. It takes n steps to reach the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

 
Example 1:

Input: n = 2
Output: 2
Explanation: There are two ways to climb to the top.
1. 1 step + 1 step
2. 2 steps
Example 2:

Input: n = 3
Output: 3
Explanation: There are three ways to climb to the top.
1. 1 step + 1 step + 1 step
2. 1 step + 2 steps
3. 2 steps + 1 step


Constraints:

1 <= n <= 45
"""

"""

Thought Process

2 - 1, 1
       2
2
3 - 1, 1, 1
       1, 2
       2, 1
3
4 - 1, 1, 1, 1
       1, 1, 2
        1, 2, 1
         2, 1, 1
         2, 2
5
5 - 1, 1, 1, 1, 1
       1, 2, 1, 1
       1, 1, 2, 1
        1, 1, 1, 2
        2, 1, 1, 1
         1, 2, 2
          2, 1, 2
           2, 2, 1
 8

6 - 1, 1, 1, 1, 1, 1
    2,1,1,1,1
1,2,1,1,1
1,1,2,1,1
1,1,1,2,1
1,1,1,1,2
2,2,1,1
2,1,2,1
2,1,1,2
1,2,2,1
1,2,1,2
1,1,2, 2
2,2,2
    
0, 1, 2, 3, 4, 5, 6 , 7,    8,    9
1, 1, 2, 3, 5, 8, 13, 21,  34,   55
"""
