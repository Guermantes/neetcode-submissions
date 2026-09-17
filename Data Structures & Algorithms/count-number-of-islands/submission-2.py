from collections import deque

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        '''count = 0
        dq = deque([(i,j) for i in range(len(grid)) for j in range(len(grid[0]))])
        def neighbors(r, c):
            potential_neighbors = [(r+1,c),(r,c+1),(r-1,c),(r,c-1)]
            return [(i,j) for (i,j) in potential_neighbors 
            if 0 <= i < len(grid) and 0 <= j < len(grid[0])]

        while dq:
            r,c = dq.popleft()
            land = deque()
            if grid[r][c] == '1':
                land.append((r,c))
                while land:
                    cur_r, cur_c = land.popleft()
                    for i, j in neighbors(cur_r, cur_c):
                        if (i,j) in dq and (i,j) not in land:
                            if grid[i][j] == '1':
                                land.append((i,j))
                            dq.remove((i,j))

                count += 1

        return count'''

        '''count = 0
        R, C = len(grid), len(grid[0])

        def dfs(r,c):
            if r >= R or r < 0 or c >= C or c < 0 or grid[r][c] == '0':
                return
            grid[r][c] = '0'
            dfs(r+1,c)
            dfs(r-1,c)
            dfs(r,c+1)
            dfs(r,c-1)
            
        for r in range(R):
            for c in range(C):
                if grid[r][c] == '1':
                    dfs(r,c)
                    count += 1

        return count'''

        count = 0
        R, C = len(grid), len(grid[0])

        def neighbors(r, c):
            potential_neighbors = [(r+1,c),(r,c+1),(r-1,c),(r,c-1)]
            return [
                (i,j) for (i,j) in potential_neighbors 
                if 0 <= i < R and 0 <= j < C
            ]

        unvisited = {
            (r,c) for r in range(R)
            for c in range(C)
            if grid[r][c] == '1'
        }

        while unvisited:
            count += 1
            r, c = unvisited.pop()
            land = deque([(r,c)])
            while land:
                cur_r, cur_c = land.pop()
                for i, j in neighbors(cur_r,cur_c):
                    if (i,j) in unvisited:
                        land.append((i,j))
                        unvisited.remove((i,j))

        return count


        