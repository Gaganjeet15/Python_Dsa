class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        cur = 0
        ans = 0
        
        
        for i in range(len(nums)):
            if (nums[i] == 1):
                cur+=1
            elif (nums[i] == 0):
                ans = max(ans, cur)
                cur = 0
        
        return max(cur,ans)