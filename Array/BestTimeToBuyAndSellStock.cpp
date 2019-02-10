class Solution {
public:
    int maxProfit(vector<int>& prices) {
        if (prices.size() == 0) return 0;
        int max_profit = 0, current_min = prices[0];
        
        for (int i = 1; i < prices.size(); i++) {
            if (prices[i] - current_min > 0) {
                max_profit = max(prices[i] - current_min, max_profit);
            } else if (prices[i] < current_min) {
                current_min = prices[i];
            }
        }
        
        return max_profit;
    }
};
