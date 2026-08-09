class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = [[]]

        for num in nums:
            result = result + [lst + [num] for lst in result]
        
        return result

