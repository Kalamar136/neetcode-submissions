class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        str_dict = {}
        for s in strs:
            sig = Solution.str_sig(s)
            str_dict[sig] = str_dict.get(sig, [])
            str_dict[sig].append(s)
        return list(str_dict.values())
    
    @staticmethod
    def str_sig(s : str):
        # Compute list signature of string
        sig = [0]*26
        for c in s:
            sig[ord(c)-ord('a')] += 1
        return tuple(sig)