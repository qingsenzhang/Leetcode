class Solution:
    def videoStitching(self, clips: List[List[int]], T: int) -> int:
        if T == 0:
            return 0
        elif not clips:
            return -1
        
        clips = sorted(clips, key = lambda interval: interval[0])
        
        count, i, left, right = 0, 0, 0, 0
        
        while right < T and i < len(clips):
            if clips[i][0] > right:
                return -1
            
            while i < len(clips) and clips[i][0] <= left:
                right = max(right, clips[i][1])
                i += 1
                
            count += 1
            left = right
            
        if right < T:
            return -1
        else:
            return count
