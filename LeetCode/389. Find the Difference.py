class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        org=dict()
        after=dict()
        for c in s:
            if c not in org.keys():
                org[c]=0
            org[c]=org[c]+1
        for c in t:
            if c not in after.keys():
                after[c]=0
            after[c]=after[c]+1
        for k,v in after.items():
            if k not in org.keys() or org[k]!=after[k]:
                return k