'''The algorithm explores to find the largest sum of the subarray'''
# solution
def maxSubarraySum(self, arr):
        res=arr[0]
        ans=arr[0]
        res=max(ans,res)
        for i in range(1,len(arr)):
            if ans<0:
                ans=0
            ans+=arr[i]
            res=max(res,ans)
        return res
