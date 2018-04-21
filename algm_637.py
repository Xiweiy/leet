##Recursive DFS
class Solution(object):
    def getSumCount(self, root, level, sumList, countList):
        if len(sumList) == level:
            sumList.append(0)
            countList.append(0)
        if root:
            sumList[level] += root.val
            countList[level] += 1
            self.getSumCount(root.left, level+1, sumList, countList)
            self.getSumCount(root.right, level+1, sumList, countList)
        
            
    def averageOfLevels(self, root):
        sumList, countList = [], []
        self.getSumCount(root, 0, sumList, countList)
        return [x*1.0/y for x,y in zip(sumList, countList) if y]


