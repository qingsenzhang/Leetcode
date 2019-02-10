class Solution {
public:
    void moveZeroes(vector<int>& nums) {
        int p1 = 0, p2 = 0;
        
        while (p1 < nums.size()) {
            if (nums[p1] != 0) nums[p2++] = nums[p1];
            p1++;
        }
        
        for (int i = p2; i < nums.size(); i++) {
            nums[i] = 0;
        }
    }
};
