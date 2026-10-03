class Solution:
    def isPalindrome(self, s: str) -> bool:
        lower = 0
        higher = len(s)-1
        while lower < higher:
            if(not s[lower].isalnum()):
                lower += 1
                continue
            if(not s[higher].isalnum()):
                higher -= 1
                continue
            if(s[lower].lower()!=s[higher].lower()):
                return False
            lower += 1
            higher -= 1
        return True
