class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        self.op, self.cl = 0, 0
        self.op_b, self.cl_b = "(", ")"

        res = []
        cur = []

        def check_valid(cur):
            stack = []

            for char in cur:
                if char == self.op_b:
                    stack.append(char)
                else:
                    pop_char = stack.pop()
                    if pop_char == self.op_b:
                        continue
                    else:
                        return False
            
            if stack:
                return False
            else:
                return True


        def backtrack(i):
            if i == 2*n:
                if check_valid(cur):
                    res.append("".join(cur[:]))
                return

            if self.cl > self.op:
                return

            if self.op < n:
                cur.append(self.op_b)
                self.op += 1
                backtrack(i+1)

                cur.pop()
                self.op -= 1
            
            if self.cl < n:    
                cur.append(self.cl_b)
                self.cl += 1
                backtrack(i+1)

                cur.pop()
                self.cl -= 1

        backtrack(0)

        return res
        