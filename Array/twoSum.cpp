class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        map<int, int> numbers;
        vector<int> vect;
        for (int i = 0; i < nums.size(); i++) {
            if (numbers.find(target - nums[i]) != numbers.end()) {
                vect = {numbers[target - nums[i]], i};
                return vect;
            }
            numbers[nums[i]] = i;
        }

        return vect;
    }
}

