class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        if len(s3) != len(s1) + len(s2):
            return False
        if len(s3) == 0:
            return True
        
        interleave_table = [[()] * (len(s3) + 1) for _ in range(2)]
        interleave_table[0][0] = interleave_table[1][0] = (0, 0)

        for i in range(1, len(s3) + 1):
            s1_last = interleave_table[0][i-1]
            s2_last = interleave_table[1][i-1]

            if not s1_last and not s2_last:
                return False

            if s1_last and s1_last[0] < len(s1)and s3[i-1] == s1[s1_last[0]]:
                interleave_table[0][i] = (s1_last[0]+1, s1_last[1])
            elif s2_last and s2_last[0] < len(s1) and s3[i-1] == s1[s2_last[0]]:
                interleave_table[0][i] = (s2_last[0]+1, s2_last[1])
            else:
                interleave_table[0][i] = False

            if s1_last and s1_last[1] < len(s2) and s3[i-1] == s2[s1_last[1]]:
                interleave_table[1][i] = (s1_last[0], s1_last[1]+1)
            elif s2_last and s2_last[1] < len(s2) and s3[i-1] == s2[s2_last[1]]:
                interleave_table[1][i] = (s2_last[0], s2_last[1]+1)
            else:
                interleave_table[1][i] = False
        
        return bool(interleave_table[0][len(s3)] or interleave_table[1][len(s3)])