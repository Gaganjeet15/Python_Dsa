class Solution:
    def maxPower(self, s: str) -> int:
        
        current = 1 
        ans = 1

        for i in range(len(s)-1):
            if s[i] == s[i+1]:
                current+=1
            else:
                ans = max(current, ans)
                current = 1
        
        return max(current, ans)


        