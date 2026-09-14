class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_sum = nums[0]
        cur_sum = -100000

        for n in nums:
            cur_sum = max(0, cur_sum) + n
            max_sum = max(max_sum, cur_sum)

        return max_sum