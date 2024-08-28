class Solution:
    def findTheArrayConcVal(self, nums: List[int]) -> int:

        total=0

        i=0
        j = len(nums)-1

        while i < j:
            val = int(f"{nums[i]}{nums[j]}")
            total = val + total
            i+=1
            j-=1
        if len(nums) % 2 == 1:
            total += nums[i]
        return total
        