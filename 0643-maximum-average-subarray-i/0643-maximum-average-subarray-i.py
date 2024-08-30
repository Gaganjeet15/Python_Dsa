class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:

        sum_k = 0
        for i in range(k):
            sum_k += nums[i]
        
        max_sum = sum_k

        start = 0
        end = k

        while end < len(nums):
            sum_k += nums[end] - nums[start]
            max_sum = max(max_sum, sum_k)
            start += 1
            end += 1
        
        return max_sum /k



       