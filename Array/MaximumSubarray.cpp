 class Solution {
 public:
     int maxSubArray(vector<int>& nums) {
         int max_sum, sum;
         max_sum = sum = accumulate(nums.begin(), nums.end(), 0);
         int front = 0, back = nums.size() - 1;
         while (front < back) {
             if (nums[front] < nums[back]) {
                 sum = sum - nums[front];
                 max_sum = (sum > max_sum) ? sum : max_sum;
                 front++;
             } else {
                 sum = sum - nums[back];
                 max_sum = (sum > max_sum) ? sum : max_sum;
                 back--;
             }
         }

         return max_sum;
     }
 };
