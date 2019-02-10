class Solution {
public:
    int majorityElement(vector<int>& nums) {
        /**
        unordered_map<int, int> hash;
        for (int i = 0; i < nums.size(); i++) {
            if (hash.find(nums[i]) != hash.end()) {
                if (hash[nums[i]] == nums.size() / 2) {
                    return nums[i];
                } else {
                    hash[nums[i]]++;
                }
            } else {
                hash[nums[i]] = 1;
            }
        }
        //note the case where  nums has length one
        return nums[0];
        **/

        //The key of this problem is to use a smart and intuitive moore voting algorithm
        int major = nums[0], count = 1;
        //note that since we initialized major with nums[0], we start i with 1
        for (int i = 1; i < nums.size(); i++) {
            if (count == 0) {
                major = nums[i];
                count++;
            } else if (nums[i] == major) {
                count++;
            } else {
                count--;
            }
        }

        return major;
    }
};
