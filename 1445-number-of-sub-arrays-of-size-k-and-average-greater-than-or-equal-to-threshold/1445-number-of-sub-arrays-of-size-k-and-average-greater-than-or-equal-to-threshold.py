class Solution:
    def numOfSubarrays(self, nums: List[int], k: int, threshold: int) -> int:
        
        current_sum = 0
        count = 0

        for i in range(k):
            current_sum += nums[i]
        
        start = 0
        end = k 

        while end <= len(nums):
            if current_sum / k >= threshold:
                count+=1

            if end< len(nums):
                current_sum+= nums[end] - nums[start]
            start += 1
            end += 1

        return count
            