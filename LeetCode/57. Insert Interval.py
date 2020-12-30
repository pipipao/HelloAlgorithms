class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        res=[]
        left,right=newInterval
        inserted=False
        for l,r in intervals:
            if l>right:
                if not inserted:
                    res.append([left,right])
                    inserted=True
                res.append([l,r])
            elif r<left:
                res.append([l,r])
            else:
                left=min(left,l)
                right=max(r,right)
        if not inserted:
            res.append([left,right])
        return res


class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        res=[]
        left,right=newInterval
        for l,r in intervals:
            if r<left:
                res.append([l,r])
                continue
            elif l<=right:
                right=max(r,right)
                left=min(l,left)
            else:
                res.append([l,r])
        res.append([left,right])
        res.sort(key= lambda x:x[0])
        return res