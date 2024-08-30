class Solution {
    public int numOfSubarrays(int[] nums, int k, int threshold) {
        
        int current_sum = 0;
        int count = 0;

        for(int i = 0; i<k; i++){
            current_sum += nums[i];
        }

        int start = 0;
        int end = k;

        while(end <= nums.length){
            if(current_sum / k >= threshold){
                count++;
            }
            if(end < nums.length){
                current_sum += nums[end] - nums[start];
            }
            start++;
            end++;
        }
        return count;
    }
}