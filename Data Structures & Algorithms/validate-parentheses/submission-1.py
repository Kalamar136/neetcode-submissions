class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for bracket in s:
            if bracket in set(['(','{','[']):
                stack.append(bracket)
            else:
                if not stack:
                    return False
                opening_bracket = stack.pop(-1)
                closing_bracket = ')' if opening_bracket == '(' else (']' if opening_bracket == '[' else '}')
                if bracket != closing_bracket:
                    return False
        return not stack