'''
1. sort the points
2. choose the end of the 1 point as the shot position in the list
3. remove all ballons crossed by the arrow.
4. start from 2 until all baloons are burst.


state/structure:
points = [(x_start, x_end), (), ()]


logic:
greedy

'''


def dindMinArrowShot(points):
    if not points:
        return 0

    # frequently used utility function
    points.sort(key=lambda x: x[0])

    shots = 0
    while points:
        # select the shot position and pop the anchor ballon
        shots += 1
        point = points.pop(0)
        shot_x = point[1]
        # print(f'current_anchor_point={shot_x}')

        # pop the remaining ballons which will be busrt by the current shot
        while points:
            if points[0][0] > shot_x:
                break
            points.pop(0)
    
    return shots

print(f'{dindMinArrowShot([[10,16],[2,8],[1,6],[7,12]])}')
print(f'{dindMinArrowShot([[1,2],[3,4],[5,6],[7,8]])}')
print(f'{dindMinArrowShot([[1,2],[2,3],[3,4],[4,5]])}')
