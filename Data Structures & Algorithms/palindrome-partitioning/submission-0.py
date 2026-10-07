class Solution:
    def partition(self, s: str) -> List[List[str]]:
        # Recursive backtracking looking at the start of a word and finding the palindromes letter by letter

        def palindromes(word):
            if len(word) == 0:
                return [[]]
            
            output = []
            for i in range(len(word)):
                pal = word[:i+1]
                # Checking if we have a palindrome
                palindrome = True
                for j in range(len(pal)//2):
                    if pal[j] != pal[-j-1]:
                        palindrome = False
                
                if palindrome:
                    pals = []
                    for res in palindromes(word[i+1:]):
                        pals.append([pal] + res)
                
                    output.extend(pals)
            
            return output
        
        return palindromes(s)