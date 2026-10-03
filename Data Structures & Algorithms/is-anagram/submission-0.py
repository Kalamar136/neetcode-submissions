class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sDict = Solution.dictString(s)
        tDict = Solution.dictString(t)
        return sDict == tDict
    
    @staticmethod
    def dictString(s: str) -> dict[str:int]:
        sDict = {}
        for letter in s:
            if sDict.get(letter, None):
                sDict[letter] += 1
            else:
                sDict[letter] = 1
        return sDict