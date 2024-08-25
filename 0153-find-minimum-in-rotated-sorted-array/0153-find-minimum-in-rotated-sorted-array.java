class Solution {
    public int findMin(int[] nums) {
        int start = 0;
        int end = nums.length - 1;
        
        while (start < end) {
            int mid = start + (end - start) / 2;
            
            if (nums[mid] > nums[end]) {
                // The minimum is in the right half.
                start = mid + 1;
            } else {
                // The minimum is in the left half, including mid.
                end = mid;
            }
        }
        
        return nums[start];
    }
}
