# Initial approach => go over each row and run binary search only if row[l] <= target <= row[r] else skip row -> O(nlogm)
# Final approach => perform binary search over row selection too -> O(log (m*n)) 
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        # for row in matrix:
        #     l, r = 0, len(row)-1
        #     if row[l] <= target and target <= row[r]:
        #         while l<=r:
        #             m = (l+r) // 2
        #             if row[m] == target:
        #                 return True
        #             elif row[m] < target:
        #                 l = m + 1
        #             else:
        #                 r = m - 1

        #     else:
        #         continue

        # return False

        n, m = len(matrix), len(matrix[0])

        top, bottom = 0, n-1
        m_row = 0

        while top <= bottom:
            m_row = (top+bottom)//2
            
            if matrix[m_row][-1] < target:
                top = m_row + 1
            elif matrix[m_row][0] > target:
                bottom = m_row - 1
            else:
                break

        if not top<=bottom:
            return False

        l, r = 0, m-1

        while l<=r:
            m_cell = (l+r)//2

            if matrix[m_row][m_cell] < target:
                l = m_cell + 1
            elif matrix[m_row][m_cell] > target:
                r = m_cell - 1
            else:
                return True

        return False





            
        