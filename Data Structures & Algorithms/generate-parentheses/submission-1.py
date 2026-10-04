class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        # Strategy: Implement a recursive function that gets the substring and remaining pairs left and it either adds an open parenthesis or closes one
        # Adding closed or open parenthesis is subject to the number n of total parenthesis

        output = []
        def parenthesis_backtracking(substr, opened, closed):
            if opened == n:
                output.append(substr + ")"*(opened-closed))
                return

            if opened < n:
                parenthesis_backtracking(substr + "(", opened + 1, closed)
            if closed < opened:
                parenthesis_backtracking(substr + ")", opened, closed + 1)
                
        parenthesis_backtracking("", 0, 0)
        return output

        # For n=1:
        # Issue 2 times "()"
        # For n=2:
        # output = ["()()", "(())", "(())", ""()()""]
