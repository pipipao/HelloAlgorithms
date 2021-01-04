class Solution:
    def minWindow(self, s: str, t: str) -> str:
        n = len(s)
        res = ""
        rLeft = -1
        rRight = -1
        left = 0
        right = 0
        big = dict()
        small = dict()
        flag = False
        endRes=False
        for c in t:
            if c not in small.keys():
                small[c] = 1
            else:
                small[c] += 1

        def satisfy():
            for k in small.keys():
                if k not in big.keys():
                    return False
                else:
                    if small[k] > big[k]:
                        return False
            return True

        while left < n and right < n:
            if satisfy():
                if (rLeft == -1 and rRight == -1) or rRight - rLeft > (right - left):
                    if flag:
                        endRes=True
                    rLeft = left
                    rRight = right
                big[s[left]] -= 1
                left += 1
            else:
                if flag:
                    break
                if s[right] not in big.keys():
                    big[s[right]] = 0

                big[s[right]] += 1
                if right + 1 == n and satisfy():
                    flag = True
                    continue
                else:
                    right += 1
        if rLeft == -1 or rRight == -1:
            return ""
        return s[rLeft:rRight + 1] if endRes else s[rLeft:rRight]


if __name__ == '__main__':
    s = Solution()
    res = s.minWindow(s="abcabdebac", t="cda")
    print(res)
