class CountSquares:

    def __init__(self):
        self.point_map = {}
        

    def add(self, point: List[int]) -> None:
        tup_point = (point[0], point[1])
        if tup_point in self.point_map:
            self.point_map[tup_point] += 1
        else:
            self.point_map[tup_point] = 1
        

    def count(self, point: List[int]) -> int:
        res = 0

        qx, qy = point[0], point[1]

        #find diagonal
        for diag_pt in self.point_map.keys():
            dx, dy = diag_pt
            if abs(dx-qx) == abs(dy-qy) and dx!=qx and dy!=qy:
                #diagonal point found
                p1 = (dx, qy)
                p2 = (qx, dy)

                if p1 in self.point_map and p2 in self.point_map:
                    res += self.point_map[p1]*self.point_map[p2]*self.point_map[diag_pt]
        
        return res
        


        
