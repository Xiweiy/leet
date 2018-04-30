class Solution(object):
    def letterCasePermutation(self, S):
        charList = []
        for i in S:
            if i.isalpha():
                charList.append([i.lower(), i.upper()])
            else:
                charList.append([i])
        
        resultList = [""]
        while charList:
            nextChar = charList.pop(0)
            resultList = [j+i for j in resultList for i in nextChar]
        return resultList
