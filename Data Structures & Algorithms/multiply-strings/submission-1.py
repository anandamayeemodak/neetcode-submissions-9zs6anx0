class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        num_map = {"0":0, "1":1, "2":2, "3":3, "4":4, "5":5, "6":6, "7":7, "8":8, "9":9}

        int_num1 = 0
        int_num2 = 0


        for i in range(len(num1)-1, -1, -1):
            n = num1[i]
            digit = num_map[n]
            print(digit)
            int_num1 = int_num1 + (10**(len(num1)-i-1))*digit
            print(int_num1)
        
        for i in range(len(num2)-1, -1, -1):
            n = num2[i]
            digit = num_map[n]
            print(digit)
            int_num2 = int_num2 + (10**(len(num2)-i-1))*digit
            print(int_num2)

        print(int_num1)
        print(int_num2)
        
        ans = int_num1*int_num2
        return str(ans)
        