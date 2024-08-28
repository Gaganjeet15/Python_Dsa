class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        
        i = 0  # Pointer for the position of the last unique element

        for j in range(i+1, len(nums)):
            if nums[j] != nums[i]:
                i += 1
                nums[i] = nums[j]
        
        return i + 1  # Return the length of the unique elements list
