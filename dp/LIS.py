nums = [10,9,2,5,3,7,101,18]
nums2=[0,1,0,3,2,3]


# memo

def lis_memo(nums):
    n=len(nums)
    dp=[[None for _ in range(n+1)] for __ in range(n)]

    def solve(ind,prev_ind):
        if ind==n:
            return 0
        if dp[ind][prev_ind]!=None:
            return dp[ind][prev_ind]
        
        pick=float("-inf")
        if prev_ind==n or nums[ind]>nums[prev_ind]:
            pick=1+solve(ind+1,ind)
        not_pick=0+solve(ind+1,prev_ind)

        dp[ind][prev_ind]=max(pick,not_pick)
        return dp[ind][prev_ind]
    return solve(0,n)
print(lis_memo(nums))



def lis_best(nums):
    n=len(nums)
    result=[]

    def bisect_left(arr,target):
        left,right=0,len(arr)

        while left<right:
            mid=(left+right)//2
            if arr[mid]<target:
                left=mid+1
            else:
                right=mid
        return left
    
    for i in range(n):
        position=bisect_left(result,nums[i])
        if position==len(result):
            result.append(nums[i])
        else:
            result[position]=nums[i]
    
    return len(result)


print(lis_best(nums))