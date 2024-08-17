class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        D={}
        for i in set(nums) :
            D[i]=0
        for i in nums :
            D[i]+=1
        n = len(nums)
        for el,count in D.items():
            if count > n//2 :
                return el
            