##SOLUTION 1: iterate over all cells
class Solution(object):
    def perimeter_percell(self, i,j, grid):
        perimeter=0
        if not grid[i][j]:
            return 0
        adjacent = [(i-1,j), (i,j-1), (i+1,j), (i, j+1)]
        for x,y in adjacent:
            if x<0 or y<0 or x==len(grid) or y==len(grid[0]) or grid[x][y]==0:
                perimeter+=1
        return perimeter
    
    def islandPerimeter(self, grid):
        return sum([self.perimeter_percell(i,j, grid) for i in range(len(grid)) for j in range(len(grid[0]))])
   

##SOLUTION 2: SEARCH AROUND OCCUPIED CELLS
class Solution(object):
    def find_first(self,grid):
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]==1:
                    return i,j
        
    def islandPerimeter(self, grid):
        
        start_i,start_j = self.find_first(grid)
        dics = {(start_i,start_j):4}
        nodes = [(start_i,start_j)]
        
        while nodes:
            i,j = nodes[0]
            adjacent = [(i-1, j), (i,j-1), (i+1,j), (i, j+1)]
            for x,y in adjacent:
                if x>=0 and y>=0 and x<len(grid) and y <len(grid[0]) and grid[x][y]==1:
                    if (x,y) in dics:
                        dics[(x,y)] -=1
                    else:
                        nodes.append((x,y))
                        dics[(x,y)]=3
            nodes.pop(0)
        return sum(dics.values())
