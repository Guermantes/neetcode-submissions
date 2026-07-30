class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        nums1_copy = nums1.copy()
        i, j = 0, 0
        while i < m and j < n:
            if nums1_copy[i] <= nums2[j]:
                nums1[i+j] = nums1_copy[i]
                i += 1
            else:
                nums1[i+j] = nums2[j]
                j += 1
        
        if i >= m:
            nums1[i+j:] = nums2[j:]
        else:
            nums1[i+j:] = nums1_copy[i:m]