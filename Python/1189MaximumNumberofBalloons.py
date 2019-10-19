class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        if not text or len(text) < 7:
            return 0
        balloons = {}
        for c in text:
            if c in 'balon':
                balloons[c] = balloons.get(c, 0) + 1
                
        if 'l' in balloons:
            balloons['l'] = balloons['l'] // 2
        else: 
            return 0
    
        if 'o' in balloons:
            balloons['o'] = balloons['o'] // 2
        else:
            return 0
        
        return min(balloons.values())
        
