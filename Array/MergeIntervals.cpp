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

	//Improved version of merge interval. This approach does not need to 
	//sort the vector before processing it but its time complexity is 
	//still the same as before
    vector<Interval> merge(vector<Interval>& intervals) {
        if (intervals.size() == 0) return vector<Interval>();

        /**
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
        **/
        map<int, int> intervs;
        for (auto &i: intervals) {
        	int start = i.start, end = i.end;
        	auto itr = intervs.lower_bound(i.start);
        	while (itr != intervs.end() && itr->second <= i.end) {
        		start = min(start, itr->second);
        		end = max(end, itr->first);
        		itr = intervs.erase(itr);
        	}
        	intervs[end] = start;
        }

        vector<Interval> ret;
        for (auto itr = intervs.begin(); itr != intervs.end(); itr++)  {ret.push_back(Interval(itr->second, itr->first));}
        return ret;
    }
};