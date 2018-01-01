#SOLUTION 1: ITERATIVE BFS
class Solution(object):
    def floodFill(self, image, sr, sc, newColor):
        
        m = len(image)
        n = len(image[0])
        prevColor = image[sr][sc]
        flooded = {(sr,sc)}
        nodelist = [(sr,sc)]
        while nodelist:
            curx, cury = nodelist.pop(0)
            newnodes = [(x,y) for (x,y) in [(curx+1, cury), (curx, cury+1), (curx-1, cury), (curx, cury-1)] if x>=0 and y>=0 and x<m and y<n and image[x][y]== prevColor and (x,y) not in flooded]
            nodelist = nodelist + newnodes
            image[curx][cury] = newColor
            flooded.add((curx, cury))
        return image

#SOLUTION 2: RECURSIVE
class Solution(object):
    
    def floodFill(self, image, sr, sc, newColor):
        m = len(image)
        n = len(image[0])
        prevColor = image[sr][sc]
        flooded = [[False]*n for i in range(m)]
        
        def revertNode(curx, cury):
            print curx,cury
            image[curx][cury] = newColor
            flooded[curx][cury]=True
            adjacentNodes = [(curx+1,cury),(curx,cury+1),(curx-1,cury),(curx,cury-1)]
            for x,y in adjacentNodes:
                if x>=0 and y>=0 and x<m and y <n and image[x][y]==prevColor and (not flooded[x][y]):
                    revertNode(x,y)
        
        revertNode(sr,sc)
        
        return image
