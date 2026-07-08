class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        #ans = nums + nums
        #return ans
        n = len(nums)
        ans = [0 for i in range(2*n)]
        for i in range(n):
            ans[i] = nums[i]
        for i in range(n, 2*n):
            ans[i] = nums[i-n]
        return ans
        