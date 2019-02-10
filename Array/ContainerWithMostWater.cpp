class Solution {
public:
    int maxArea(vector<int>& height) {
        int max = 0;
        for (int i = 0; i < height.size(); i++) {
            for (int j = 0; j < i; j++) {
                max = ((min(height[i], height[j]) * (i - j)) > max) ? (min(height[i], height[j]) * (i - j)) : max;
            }
        }       
        return max;
    }
};
