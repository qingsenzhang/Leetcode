class Solution {
public:
    vector<int> plusOne(vector<int>& digits) {
        /**
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
        **/

        //The improved version abuse the structure of the number
        //if the digit is 9, make it 0, if it's not, add one and return
        int n = digits.size() - 1;
        for (int i = n; i >= 0; i--) {
            if (digits[i] == 9) {
                digits[i] = 0;
            } else {
                digits[i]++;
                return digits;
            }
        }

        //if the function didn't reuturn in the for loop, it means its all 9
        //make the first digit 1 and add 0 to the end of the vector
        digits[0] = 1;
        digits.push_back(0);
        return digits;
    }
};
