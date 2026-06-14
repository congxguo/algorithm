def combine(nums, k):
    n = len(nums)
    ans = []
    path = []

    def backtrack(start):
        # 如果已经选够 k 个，加入答案
        if len(path) == k:
            ans.append(path[:])
            return

        # 从 start 开始继续选
        for i in range(start, n):
            path.append(nums[i])
            backtrack(i + 1)
            path.pop()

    backtrack(0)
    print(f'{ans}')
    return ans


combine([1, 2, 3, 6, 8, 9], 4)