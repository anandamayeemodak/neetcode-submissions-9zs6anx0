class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        list_s1 = list(s1)
        window = []
        removed = []
        streak = False

        for l in range(len(s2)):
            r = l
            list_s1.extend(removed)
            removed = []
            while r<len(s2):
                char = s2[r]
                
                if char in list_s1:
                    list_s1.remove(char)
                    removed.append(char)
                    if len(list_s1) == 0:
                        return True

                    r += 1
                else:
                    break
                

        return False



                




        