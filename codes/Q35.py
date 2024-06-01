class Solution(object):

    def lessEqualTwo(self, nums, indexes, target):
        i = indexes[0]
        j = indexes[1]
        if target <= nums[i]:
            return i
        elif target > nums[i] and target <= nums[j]:
            return j
        elif target > nums[j]:
            return j+1
        
    def searchInsert(self, nums, target):
    # def searchInsert(nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """

        a = len(nums)

        if target > nums[a-1]:
            return a

        indexes = [ i for i in range(a)]

        while True:
            d = len(indexes)

            if d <= 2:
                return self.lessEqualTwo(nums, indexes, target)

            middle_index = int((d - 1)/2)

            nums_index = indexes[middle_index]
            
            middle = nums[nums_index]      
            left = nums[nums_index - 1]     
            right = nums[nums_index + 1]
            

            # deal with equal to left or right 
            if target == middle or ((target < middle) and (target > left)):
                return nums_index

            elif (target > middle) and (target <= right):
                return nums_index + 1
            
            elif target == left:
                return nums_index - 1

            elif (target < middle) and (target < left):
                indexes = indexes[:middle_index+1]
                
            elif (target > middle) and (target > right):
                indexes = indexes[middle_index+1:]
                
                

            