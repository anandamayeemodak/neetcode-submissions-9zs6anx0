class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        for row in matrix:
            l, r = 0, len(row)-1
            if row[l] <= target and target <= row[r]:
                while l<=r:
                    m = (l+r) // 2
                    if row[m] == target:
                        return True
                    elif row[m] < target:
                        l = m + 1
                    else:
                        r = m - 1

            else:
                continue

        return False



            
        