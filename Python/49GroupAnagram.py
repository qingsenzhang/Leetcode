class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = {}
        for string in strs:
            key = ''.join(sorted(string))
            if key not in groups:
                groups[key] = [string]
            else:
                groups[key].append(string)
        return groups.values()
