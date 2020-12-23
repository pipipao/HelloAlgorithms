class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ans = []

        def rec(s, l, r):
            if l == 0 and r == 0:
                ans.append(s)
                return
            if l == r:
                rec(s + '(', l - 1, r)
            if l < r:
                if l > 0:
                    rec(s + '(', l - 1, r)
                rec(s + ')', l, r - 1)

        rec('', n, n)
        return ans

