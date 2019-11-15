class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        count1, count2 = collections.Counter(), collections.Counter()
        for num in nums1:
            count1[num] += 1
        for num in nums2:
            count2[num] += 1
        
        ans = []
        for num in count1:
            if num in count2:
                for i in range(min(count1[num], count2[num])):
                    ans.append(num)
                    
        return ans
        
        
