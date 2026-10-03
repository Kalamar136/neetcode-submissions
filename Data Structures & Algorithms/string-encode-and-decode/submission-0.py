class Solution:
    def encode(self, strs: list[str]) -> str:
        code = ''
        for s in strs:
            code += f'{len(s):03d}{s}'
        return code

    def decode(self, s: str) -> List[str]:
        list_str = []
        while len(s):
            length = int(s[:3])
            list_str.append(s[3:3+length])
            s = s[3+length:]
        return list_str