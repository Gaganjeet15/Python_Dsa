class Solution:
    def missingNumber(self, nums: List[int]) -> int:

        i = 0
        n = len(nums)

        while i < n:
            correct = nums[i]
            
            if nums[i] < n and nums[i] != nums[correct]:
                nums[i], nums[correct] = nums[correct], nums[i]
            
            else:
                i = i +1
        
        for index in range(n):
            if index != nums[index]:
                return index
        
        return n
            
        



        