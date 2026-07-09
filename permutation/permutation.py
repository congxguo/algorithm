def permutation(nums):
    ans = []
    n = len(nums)
    
    def backtrace(start):
        # reach the end
        if start == n:
            ans.append(nums[:])
            return
        
        # choose who is the start of the permutation
        for u in range(start, n):
            nums[start], nums[u] = nums[u], nums[start]
            # here is start + 1
            backtrace(start + 1)
            nums[start], nums[u] = nums[u], nums[start]

    
    backtrace(0)
    print(f'{ans}')
    return ans

permutation([1, 2, 3, 4])



