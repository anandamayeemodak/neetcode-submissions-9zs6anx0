class Solution:
    def partition(self, s: str) -> List[List[str]]:
        partitions = []
        cur_part = []

        def isPalindrome(subs):
            l, r = 0, len(subs)-1

            while l<=r:
                if subs[l] != subs[r]:
                    return False
                l += 1
                r -= 1

            return True

        def dfs(i):
            if i >= len(s):
                partitions.append(cur_part[:])
                return

            for j in range(i, len(s)):
                if isPalindrome(s[i:j+1]):
                    cur_part.append(s[i:j+1])
                    dfs(j+1)
                    cur_part.pop()
                
        dfs(0)
        return partitions
        