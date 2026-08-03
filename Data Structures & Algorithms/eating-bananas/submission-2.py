class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        low = 1
        high = max(piles)

        while low < high:
            mid = (low + high) // 2
            if self.eatingHours(piles, mid) > h:
                low = mid + 1
            elif self.eatingHours(piles, mid) <= h:
                high = mid
        
        return low
            


    def eatingHours(self, piles: List[int], k: int) -> int:
        hours = [(pile + k - 1) // k for pile in piles]
        return sum(hours)