##SOLUTION 1: GET ALL INDICES OF C
class Solution(object):
    def shortestToChar(self, S, C):
        lenS = len(S)
        Cindices = [i for i in range(lenS) if S[i]==C]
        
        index = 0
        distances = []
        for i in range(lenS):
            if i < Cindices[0]:
                distances.append(Cindices[0]-i)
            elif i > Cindices[-1]:
                distances.append(i- Cindices[-1])
            elif i == Cindices[index]:
                distances.append(0)
                index += 1
            else:
                distances.append(min(i-Cindices[index-1], Cindices[index]-i))
        return distances

##SOLUTION 2: LOOP OVER FROM LEFT AND LOOP OVER AGAIN FROM RIGHT
def shortestToChar(self, S, C):
        n = len(S)
        res = [n] * n
        pos = -n
        for i in range(n) + range(n)[::-1]:
            if S[i] == C: pos = i
            res[i] = min(res[i], abs(i - pos))
        return res

##solution 3: same as solution 2
def shortestToChar(self, S, C):
        n = len(S)
        res = [0 if c == C else n for c in S]
        for i in range(n - 1): res[i + 1] = min(res[i + 1], res[i] + 1)
        for i in range(n - 1)[::-1]: res[i] = min(res[i], res[i + 1] + 1)
        return res
