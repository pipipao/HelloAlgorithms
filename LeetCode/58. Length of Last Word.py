class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        length=0
        start=False
        finish=False
        for c in s[::-1]:
            if c!=' ':
                length+=1
                start=True
            if start and c==' ':
                break
        return length