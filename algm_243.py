##Condition:You may assume that word1 does not equal to word2, and word1 and word2 are both in the list.

class Solution(object):
    def shortestDistance(self, words, word1, word2):
        wordsdic = {}
        wordsLen = len(words)
        for i in range(wordsLen):
            if words[i] in wordsdic:
                wordsdic[words[i]].append(i)
            else:
                wordsdic[words[i]] = [i]

        word1pos = wordsdic[word1]
        word2pos = wordsdic[word2]
        i = 0
        j = 0
        shortest = wordsLen
        while i < len(word1pos) and j < len(word2pos):
            shortest = min(abs(word1pos[i]-word2pos[j]), shortest)
            if word1pos[i] > word2pos[j]:
                j += 1
            else:
                i += 1
        return shortest
