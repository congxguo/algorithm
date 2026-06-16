import math

class Solution(object):
    def longestCommonSubsequence(self, text1, text2):
        """
        :type text1: str
        :type text2: str
        :rtype: int
        """

        if not text1:
            return 0
        if not text2:
            return 0

        print(f'######################################################')
        print(f'input: text1={text1}, text2={text2}')

        dp = [[-1 for _ in range(0, len(text2))] for _ in range(0, len(text1))]
        print(dp)
        max_len = 0
        for i in range(0, len(text1)):
            for j in range(0, len(text2)):
                print(f'i={i}, j={j}')
                if i == 0 and j == 0:
                    if text1[i] == text2[j]:
                        dp[i][j] = 1
                    else:
                        dp[i][j] = 0
                elif i == 0 and j > 0:
                    if text1[i] == text2[j]:
                        dp[i][j] = dp[i][j - 1] + 1
                    else:
                        dp[i][j] = dp[i][j - 1]
                elif i > 0 and j == 0:
                    if text1[i] == text2[j]:
                        dp[i][j] = dp[i-1][j] + 1
                    else:
                        dp[i][j] = dp[i-1][j]
                else:
                    if text1[i] == text2[j]:
                        dp[i][j] = dp[i-1][j-1] + 1
                    else:
                        dp[i][j] = max(dp[i-1][j], dp[i][j-1])
                    
                max_len = max(max_len, dp[i][j])
                    
        return max_len
        
        
solution = Solution()
print(solution.longestCommonSubsequence('abcde', 'ace'))
print(f'######################################################')

print(solution.longestCommonSubsequence('abc', 'abc'))
print(f'######################################################')

print(solution.longestCommonSubsequence('abc', 'def'))
print(f'######################################################')
