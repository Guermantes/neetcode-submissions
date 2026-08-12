import itertools
import numpy as np

class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        '''max_apps = [target // num for num in nums]
        result = []
        
        ranges = [range(a+1) for a in max_apps]
        for indices in itertools.product(*ranges):
            if np.dot(nums, indices) == target:
                app = []
                for i in range(len(nums)):
                    if indices[i] != 0:
                        app += indices[i] * [nums[i]]
                result.append(app)

        return result'''
        res = []
        nums.sort()

        def dfs(i, cur_list, cur_sum):
            if cur_sum == target:
                res.append(cur_list.copy())
                return
            elif cur_sum > target:
                return
            else:
                for j in range(i, len(nums)):
                    cur_list.append(nums[j])
                    dfs(j, cur_list, cur_sum + nums[j])
                    cur_list.pop()

        dfs(0, [], 0)
        return res



        
        

