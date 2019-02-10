class Solution {
 public:
     /**
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
     **/

     //The key of this problem is to look back to previous sum as we traverse the array
     //i.e. if previous sum is greater than 0, keep them, otherwise start from current num
     int maxSubArray(vector<int>& nums) {
         int sum = 0, max_sum = nums[0];
         for (int i = 0; i < nums.size(); i++) {
             sum = ((nums[i] + sum) > nums[i]) ? (nums[i] + sum) : nums[i];
             max_sum = (sum > max_sum) ? sum : max_sum;
         }
         return max_sum;
     }
 };
