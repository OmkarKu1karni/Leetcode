class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        st = []
        nge = {}
        for num in reversed(nums2):
            while st and st[-1] <= num:
                st.pop()
            nge[num] = st[-1] if st else -1
            st.append(num)
        return [nge[num] for num in nums1]