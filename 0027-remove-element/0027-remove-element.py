class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:

        count = 0

        for i in range(len(nums)):
            if nums[i] != val:
                nums[count] = nums[i]  # Move the valid element to the 'count' index
                count += 1
        return count
        