class Solution:
    def findJudge(self, N: int, trust: List[List[int]]) -> int:
        if N == 1:
            return 1
        elif not trust:
            return -1
        elif len(trust) == 1:
            return trust[0][1]
        
        trust_mapping = collections.defaultdict(set)
        for t in trust:
            trust_mapping[t[0]].add(t[1])
            
        judge = 1
        for i in range(1, N + 1):
            if judge not in trust_mapping[i]:
                judge = i
                
        for i in range(1, N + 1):
            if i != judge and judge not in trust_mapping[i] or i in trust_mapping[judge]:
                print(judge, i)
                return -1
            
        return judge
