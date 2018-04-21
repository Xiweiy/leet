####O(n) use stack
class Solution(object):
    def nextGreaterElement(self, findNums, nums):
        stack = []
        nextLargestMap = {}
        for i in nums[::-1]:
            while stack:
                if i < stack[-1]:
                    nextLargestMap[i] = stack[-1]
                    stack.append(i)
                    break
                else:
                    stack.pop(-1)
            if not stack:
                nextLargestMap[i] = -1
                stack.append(i)
        return [nextLargestMap[i] for i in findNums]
