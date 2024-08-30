class Solution {
    public double findMaxAverage(int[] nums, int k) {
        int current_sum = 0;
        for (int i = 0; i<k; i++){
            current_sum += nums[i];
        }
        int max_sum = current_sum;

        int start = 0;
        int end = k;

        while (end < nums.length){
            current_sum += nums[end] - nums[start];
            max_sum = Math.max(current_sum, max_sum);
            start++;
            end++;
        }
        return (double) max_sum / k;

        
    }
}