class Solution:
    def minimumAverage(self, nums: List[int]) -> float:

        nums.sort()
        mini =  float('inf')

        start = 0
        end = len(nums)-1

        while start < end:
            new =(nums[start]+nums[end])/2
            mini = min(new, mini)
            start+=1
            end-=1

        return mini

        