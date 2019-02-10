 class Solution {
 public:
     int maxArea(vector<int>& height) {
         int max_vol = 0;
         //the critical part of this problem is to use two pointer to measure the volume to avoid redundancy

         /**
         for (int i = 0; i < height.size(); i++) {
             for (int j = 0; j < i; j++) {
                 max = ((min(height[i], height[j]) * (i - j)) > max) ? (min(height[i], height[j]) * (i - j)) : max;
             }
         }
         **/
         int front = 0, back = height.size() - 1;
         while (front < back) {
             max_vol = ((min(height[front], height[back]) * (back - front)) > max_vol) ? (min(height[front], height[back]) * (back - front)) : max_vol;
             if (height[front] > height[back]) {
                 back--;
             } else {
                 front++;
             }
         }

         return max_vol;
     }
 };
