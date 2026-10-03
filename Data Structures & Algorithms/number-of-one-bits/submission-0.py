class Solution:
    def hammingWeight(self, n: int) -> int:
        count = 0
        while n>0:
            if n % 2 == 0:
                n = n//2
            else:
                count += 1
                n = (n-1)//2
        
        return count