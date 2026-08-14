class Solution:
    def rob(self, nums: List[int]) -> int:
        '''if len(nums) == 1:
            return nums[0]
        elif len(nums) == 2: 
            return max(nums[0], nums[1])
        elif len(nums) == 3:
            return max(nums[0] + nums[2], nums[1])
        else: 
            return max(nums[0] + self.rob(nums[2:]), nums[1] + self.rob(nums[3:]))'''
        def mem(n: int, cache):
            if n == 0: 
                return nums[0]
            elif n == 1:
                return max(nums[0], nums[1])
            elif n == 2: 
                return max(nums[0] + nums[2], nums[1])
            elif cache[n] != -1:
                return cache[n]
            
            cache[n] = max(nums[n] + mem(n-2, cache), 
            mem(n-1, cache))

            return cache[n]

        return mem(len(nums)-1, [-1]*len(nums))