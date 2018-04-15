class Solution(object):
    def transformWord(self, word, mapping):
        morse = []
        for character in word:
            morse.append(mapping[character])
        return "".join(morse)
            
            
    def uniqueMorseRepresentations(self, words):
        import string
        transformList = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        transformMap = {i:j for i,j in zip(string.ascii_lowercase, transformList)}
        transformation = []
        for word in words:
            transformation.append(self.transformWord(word, transformMap))
        return len(set(transformation))



##Solution 2
class Solution(object):
            
    def uniqueMorseRepresentations(self, words):
        d = [".-", "-...", "-.-.", "-..", ".", "..-.", "--.", "....", "..", ".---", "-.-", ".-..", "--",
             "-.", "---", ".--.", "--.-", ".-.", "...", "-", "..-", "...-", ".--", "-..-", "-.--", "--.."]
        return len({''.join(d[ord(i) - ord('a')] for i in w) for w in words})
  
