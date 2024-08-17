class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        n = len(nums)
        if n == 0:
            return []

        el1, el2 = None, None
        count1, count2 = 0, 0
        
        for num in nums:
            if num == el1:
                count1 += 1
            elif num == el2:
                count2 += 1
            elif count1 == 0:
                el1, count1 = num, 1
            elif count2 == 0:
                el2, count2 = num, 1
            else:
                count1 -= 1
                count2 -= 1
    
        cnt1, cnt2 = 0, 0
        for num in nums:
            if num == el1:
                cnt1 += 1
            elif num == el2:
                cnt2 += 1
        
        result = []
        threshold = n // 3
        if cnt1 > threshold:
            result.append(el1)
        if cnt2 > threshold:
            result.append(el2)
        
        return result
            