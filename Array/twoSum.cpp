class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        //here remember to use unordered_map rather than map, the data is faster for retrieval 
        //map has O(log(n)) for search/insertion/deletion, while unordered_map has O(1) (best) and O(n) (worst)
        unordered_map <int, int> numbers;
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
};

