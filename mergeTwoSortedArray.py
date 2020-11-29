class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        p = m - 1
        q = n - 1
        while p > 0 and q > 0:
            if(nums1[p] > nums2[q]):
                nums1[p + q + 1] = nums1[p]
                p = p - 1
            else:
                nums1[p + q + 1] = nums2[q]
                q = q - 1
        nums1[:q + 1] = nums2[: q + 1]