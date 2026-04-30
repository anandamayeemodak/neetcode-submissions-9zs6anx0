class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        hand.sort()

        if len(hand)%groupSize != 0:
            return False

        numGroups = len(hand)//groupSize
        groups = [(-1,0)]*numGroups

        for card in hand:
            prev_card = card - 1
            for i in range(numGroups):
                l_card, size = groups[i]
                if (l_card == -1 or l_card == prev_card) and size < groupSize:
                    print("group: ", i)
                    print("top_card: ", card)
                    print("size: ", size+1)
                    groups[i] = (card, size+1)
                    break
        
        print(groups)
        for group in groups:
            top_card, size = group
            if size < groupSize:
                return False
        
        return True


        
