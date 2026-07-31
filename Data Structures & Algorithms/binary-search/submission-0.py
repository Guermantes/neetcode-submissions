class Solution:
    def search(self, nums: List[int], target: int) -> int:
        L = 0
        R = len(nums) 
        mid = (L + R) // 2
        while L < R:
            if target < nums[mid]:
                R = mid
                mid = (L + R) // 2
            elif target > nums[mid]:
                L = mid + 1
                mid = (L + R) // 2
            else:
                return mid
        return -1

