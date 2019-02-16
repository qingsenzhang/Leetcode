class Solution {
public:
	// The key of this problem is to break the multipying process into two distinct 
	//passes: one pass multiplying all the numbers from left and the other 
	//multipying from right
    vector<int> productExceptSelf(vector<int>& nums) {
    	if (nums.size() == 0) return vector<int>();
    	/**
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
        **/
    	vector<int> ret(nums.size(), 1);
    	int left = 1, right = 1, n = nums.size();
    	for (int i = 0; i < n; i++) {
    		ret[i] *= left;
    		left *= nums[i];
    		ret[n - i - 1] *= right;
    		right *= nums[n - i - 1];
    	}

        return ret;
    }
};