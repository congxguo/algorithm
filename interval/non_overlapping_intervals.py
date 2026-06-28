'''
1. sort intervals
2. select the first interval as anchor
3. compare with the remaining intervals one by one
   - if overlaps
     - remove the interval with larger end
   - if not
     - pop current interval, and go to step 2
'''


def eraseOverlapIntervals(intervals):
    if not intervals:
        return 0

    intervals.sort(key=lambda x:x[0])

    remove_intervals = []
    remove_intervals_count = 0
    while intervals:
        anchor_inverval = intervals.pop(0)

        while intervals:
            # no overlap
            if intervals[0][0] >= anchor_inverval[1]:
                break

            # has overlap, anchor ends before current interval
            if intervals[0][1] >= anchor_inverval[1]:
                remove_intervals.append(intervals.pop(0))
                remove_intervals_count += 1
            else:
                remove_intervals.append(anchor_inverval)
                remove_intervals_count += 1
    
    print(f'removed_intervals={remove_intervals}')
    return remove_intervals_count


intervals = [[1,2],[2,3],[3,4],[1,3]]
print(f'{eraseOverlapIntervals(intervals)}')

intervals = [[1,2],[1,2],[1,2]]
print(f'{eraseOverlapIntervals(intervals)}')

intervals = [[1,2],[2,3]]
print(f'{eraseOverlapIntervals(intervals)}')