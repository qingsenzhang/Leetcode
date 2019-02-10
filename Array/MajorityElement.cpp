class Solution {
public:
    int majorityElement(vector<int>& nums) {
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
    }
};
