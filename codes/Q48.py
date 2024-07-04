class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """

        length = len(matrix)

        # For every n x n, 
        # n/ 2
        # 0...
        # 0,0 ... 0,4
        # 1,1 ... 1,3
        # 2,2 

        if length >= 2:

            middle = length // 2
            last_index = length - 2

            for i in range(middle):
                   
                r = i
                # c = i

                for j in range(i, last_index):
                    # r= 0
                    c = j

                    first_val = matrix[r][c]

                    while True:
                        next_r = c
                        next_c = last_index -r

                        temp_next = matrix[next_r][next_c]

                        matrix[next_r][next_c] = first_val

                        if next_r == i and next_c == j:
                            break

                        first_val = temp_next

                        r = next_r
                        c = next_c
                last_index-=1
                    
                    # m,n -> n,-m+(length-1)

            # if length != 2:
            #     doubles = length - 2

            #     last_r = doubles
            #     last_c = doubles


            #     first_val = matrix[last_r][last_c]

            #     while True:
            #         next_r = last_c
            #         next_c = last_index - last_r

            #         temp_next = matrix[next_r][next_c]

            #         matrix[next_r][next_c] = first_val

            #         if next_r == doubles and next_c == doubles:
            #             break

            #         first_val = temp_next

            #         last_r = next_r
            #         last_c = next_c

            


            


"""
# You are given an n x n 2D matrix representing an image, rotate the image by 90 degrees (clockwise).

# You have to rotate the image in-place, which means you have to modify the input 2D matrix directly. DO NOT allocate another 2D matrix and do the rotation.

 
# Example 1:


# Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
# Output: [[7,4,1],[8,5,2],[9,6,3]]
# Example 2:


# Input: matrix = [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]
# Output: [[15,13,2,5],[14,3,4,1],[12,6,8,9],[16,7,10,11]]
 

# Constraints:

# n == matrix.length == matrix[i].length
# 1 <= n <= 20
# -1000 <= matrix[i][j] <= 1000

# """
   

# Thought Process

"""
Size 2

[[1,2],
 [3,4,]]

0,0 -> 0,1
0,1 -> 1,1

1,0 -> 0,0
1,1 -> 1,0


Size 3
 
[[1,2,3],
 [4,5,6],
 [7,8,9]]

temp = []

2,0 -> 0,0 --
1,0 -> 0,1 ---
0,0 -> 0,2 --

2,1 -> 1,0 ---
1,1 -> 1,1 
0,1 -> 1,2 ---

2,2 -> 2,0 --
1,2 -> 2,1 ---
0,2 -> 2,2 --


m,n -> n,-m+(length-1)

0,0 - 0,2 
0,2 - 2,2
2,2 - 2,0
2,0 - 0,0

0,1 - 1,2
1,2 - 2,1
2,1 - 1,0
1,0 - 0,1

1,1

Size 4
 
[[1,2,3, 4],
 [5,6,7,8],
 [9,10,11,12],
 [13,14,15,16] ]

3,0 -> 0,0 -
2,0 -> 0,1 --
1,0 -> 0,2
0,0 -> 0,3 -

3,1 -> 1,0 ---
2,1 -> 1,1
1,1 -> 1,2
0,1 -> 1,3 --

3,2 -> 2,0 --
2,2 -> 2,1
1,2 -> 2,2
0,2 -> 2,3 ---

3,3 -> 3,0 -
2,3 -> 3,1 ---
1,3 -> 3,2 --
0,3 -> 3,3 -

3-m
m,n -> n, (length-1)-m

0,0 - 0,3
0,3 - 3,3
3,3 - 3,0
3,0 - 0,0

0,1 - 1,3
1,3 - 3,2
3,2 - 2,0
2,0 - 0,1

0,2 - 2,3
2,3 - 3,1
3,1 - 1,0
1,0 - 0,2

2,2 

"""


