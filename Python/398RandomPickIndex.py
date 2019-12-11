class Solution:

    def __init__(self, nums: List[int]):
        self.mapping = {}
        for i in range(len(nums)):
            if nums[i] not in self.mapping:
                self.mapping[nums[i]] = [i]
            else:
                self.mapping[nums[i]].append(i)

    def pick(self, target: int) -> int:
        return random.choice(self.mapping[target])
        


# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.pick(target)
