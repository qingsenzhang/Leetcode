class Solution {
public:
    vector<int> plusOne(vector<int>& digits) {
        bool carryOn = true;
        for (int i = digits.size() - 1; i >= 0; i--) {
            if (digits[i] == 9 && carryOn) {
                digits[i] = 0;
            } else if (carryOn) {
                digits[i]++;
                carryOn = false;
            } else {
                break;
            }
        }

        if (carryOn) digits.insert(digits.begin(), 1);

        return digits;
    }
};
