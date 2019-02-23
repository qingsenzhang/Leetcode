/**
 * Definition for an interval.
 * struct Interval {
 *     int start;
 *     int end;
 *     Interval() : start(0), end(0) {}
 *     Interval(int s, int e) : start(s), end(e) {}
 * };
 */
class Solution {
public:
	static bool compareInterval(Interval v1, Interval v2) {
		return (v1.start < v2.start);
	}

    vector<Interval> merge(vector<Interval>& intervals) {
        if (intervals.size() == 0) return vector<Interval>();

        sort(intervals.begin(), intervals.end(), compareInterval);

        int curr = 0;
        while (curr < intervals.size() - 1) {
        	if (intervals[curr].end >= intervals[curr + 1].start) {
        		intervals[curr].end = max(intervals[curr].end, intervals[curr + 1].end);
        		intervals.erase(intervals.begin() + curr + 1);
        	} else {
        		curr++;
        	}
        }

        return intervals;
    }
};