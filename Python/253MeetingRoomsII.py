class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        if not intervals:
            return 0
    
        room_usage = {}
        times = set()
        for interval in intervals:
            room_usage[interval[0]] = room_usage.get(interval[0], 0) + 1
            times.add(interval[0])
            room_usage[interval[1]] = room_usage.get(interval[1], 0) - 1
            times.add(interval[1])
       
        times = sorted(list(times))
        room = max_room = 0
        for time in times:
            room += room_usage[time]
            max_room = max(max_room, room)
        
        return max_room
        
