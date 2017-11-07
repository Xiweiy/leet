##SOLUTION 1: BEAT 46.85%
class Solution(object):
    def judgeCircle(self, moves):
        from collections import Counter
        dic = Counter(moves)
        result = True if dic["L"]==dic["R"] and dic["U"]==dic["D"] else False
        return result


##SOLUTION 2: BEAT 76.98%
class Solution(object):
    def judgeCircle(self, moves):
        return moves.count('L') == moves.count('R') and moves.count('U') == moves.count('D')
