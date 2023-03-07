class Solution:
    def minimumTime(self, time: List[int], totalTrips: int) -> int:
        left=1
        right=(min(time))*totalTrips
        
        def helper(mid):
            totaltrip=0
            for t in time:
                totaltrip+=mid//t
            return totaltrip

        while(left<right):
            mid=(left+right)//2
            totalformid=helper(mid)
            if totalformid<totalTrips:
                left=mid+1
            else:
                right=mid
          
        return left


        