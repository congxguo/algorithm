# [1, 2, 3] -> [1, 2], [1, 3], [2, 3]


def combine_array(nums, k):
    res = []
    path = []
    n = len(nums)

    def backtrack(i):
        # If we have k elements, record the combination
        if len(path) == k:
            res.append(path.copy())
            return

        # If not enough elements remain, prune
        if len(path) + (n - i) < k:
            return

        # Option 1: choose nums[i]
        # make sure the content of the path out is the same with path in
        path.append(nums[i])
        backtrack(i + 1)
        path.pop()

        # Option 2: skip nums[i]
        backtrack(i + 1)

    backtrack(0)
    print(res)
    return res


combine_array([1, 2, 3, 6, 8, 9], 4)