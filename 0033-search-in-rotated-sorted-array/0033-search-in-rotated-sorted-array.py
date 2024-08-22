class Solution:
    def search(self, arr: List[int], target: int) -> int:
        start = 0
        end = len(arr)-1
        while start <= end:
            mid = (start + end) // 2

            # if mid points the target
            if arr[mid] == target:
                return mid

            # if left part is sorted
            if arr[start] <= arr[mid]:
                if arr[start] <= target and target <= arr[mid]:
                    # element exists
                    end = mid - 1
                else:
                    # element does not exist
                    start = mid + 1
            else:  # if right part is sorted
                if arr[mid] <= target and target <= arr[end]:
                    # element exists
                    start = mid + 1
                else:
                    # element does not exist
                    end = mid - 1
        return -1
        