class Solution {
    public int findMaxConsecutiveOnes(int[] nums) {
       int cur = 0;
       int ans = 0;

       for (int i = 0; i < nums.length; i++) {
        if(nums[i] == 1){
            cur++;
        }
        else{
            ans = Math.max(ans, cur);
            cur = 0;
        }
       } 
       return Math.max(ans, cur);
    }
}