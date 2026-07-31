class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        
        if k == 0:
            return []
        else:
            points = self.push_min(points)
            return [points[0]] + self.kClosest(points[1:], k-1)
        
    def dist_squared(self, point: List[int]):
        return point[0] ** 2 + point[1] ** 2

    def push_min(self, points: List[List[int]]):
        for i in range(len(points)):
            if self.dist_squared(points[i]) < self.dist_squared(points[0]):
                temp = points[0]
                points[0] = points[i]
                points[i] = temp
        return points