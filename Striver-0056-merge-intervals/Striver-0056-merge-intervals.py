class Solution:
    def merge(self, intervals: list[list[int]]) -> list[list[int]]:
        # Sort the intervals by their start times.
        # This is the crucial first step. If intervals are sorted, we only need to
        # compare the current interval with the last one added to our merged list.
        # Timsort (Python's default sort) is O(N log N) time complexity.
        intervals.sort(key=lambda x: x[0])

        merged_intervals = []
        for interval in intervals:
            # If the merged_intervals list is empty, or if the current interval does not overlap
            # with the last interval in merged_intervals, simply add it.
            # An overlap happens if interval[0] (current start) <= merged_intervals[-1][1] (last end).
            # So, no overlap if interval[0] > merged_intervals[-1][1].
            if not merged_intervals or interval[0] > merged_intervals[-1][1]:
                merged_intervals.append(interval)
            else:
                # Otherwise, there is an an overlap. Merge the current interval with the last one
                # in merged_intervals by extending its end point.
                # The new end point will be the maximum of the current interval's end
                # and the last merged interval's end.
                merged_intervals[-1][1] = max(merged_intervals[-1][1], interval[1])
        
        return merged_intervals