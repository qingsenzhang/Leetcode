class Solution {
 public:
     int maxSubArray(vector<int>& nums) {
         int sum = 0;
         for (auto& num : nums) {
             sum += num;
         }
         return sumSub(nums, 0, nums.size() - 1, sum);
     }
     
     int sumSub(vector<int>& nums, int front, int back, int currentSum) {
         if (front == back) return nums[front];
         int result = max(max(sumSub(nums, front + 1, back, currentSum - nums[front]), 
                              sumSub(nums, front, back - 1, currentSum - nums[back])), 
                          currentSum);
         //printf("Current max is %d with front = %d and back = %d\n", result, front, back);
         return result;
     }
 };
