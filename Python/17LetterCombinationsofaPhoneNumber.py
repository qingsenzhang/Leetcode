class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        mapping = {
            "1" : "",
            "2" : "abc",
            "3" : "def",
            "4" : "ghi",
            "5" : "jkl",
            "6" : "mno",
            "7" : "pqrs",
            "8" : "tuv",
            "9" : "wxyz"
        }
        ans = []
        if not digits or len(digits) == 0 or (len(digits) == 1 and digits[0] == "1"):
            return ans
            
        self.dfs("", digits, mapping, ans)
        return ans
        
    def dfs(self, current_str, remaining_str, mapping, ans):
        if remaining_str == "":
            ans.append(current_str)
            return 
        
        for letter in mapping[remaining_str[0]]:
            current_str += letter
            self.dfs(current_str, remaining_str[1:], mapping, ans)
            current_str = current_str[:-1]

        
