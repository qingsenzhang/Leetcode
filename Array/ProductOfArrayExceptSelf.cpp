class Solution {
public:
    vector<int> productExceptSelf(vector<int>& nums) {
    	if (nums.size() == 0) return vector<int>();
        vector<int> ret(nums.size());

        ret[0] = 1;
        for (int i = 1; i < nums.size(); i++) {
        	ret[i] = ret[i - 1] * nums[i - 1];
        }

        int right = 1;
        for (int i = nums.size() - 1; i >= 0; i--) {
        	ret[i] *= right;
        	right *= nums[i];
        }

        return ret;
    }
};