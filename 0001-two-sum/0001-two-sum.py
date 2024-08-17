class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        D = {}
        for i in range(len(nums)) :
            extra = target-nums[i]
            if extra in D.keys():
                return [D[extra] , i]
            else :
                D[nums[i]] = i
        return [-1,-1]