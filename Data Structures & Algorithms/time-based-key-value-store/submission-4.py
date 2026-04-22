class TimeMap:

    def __init__(self):
        self.timestamp_map = {}
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key in self.timestamp_map:
            self.timestamp_map[key].append([timestamp, value])
        else:
            self.timestamp_map[key] = [[timestamp, value]]
        

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.timestamp_map:
            return ""

        value_arr = self.timestamp_map[key]

        l, r = 0, len(value_arr)-1
        m = 0
        result_idx = -1

        if timestamp < value_arr[l][0]:
            return ""

        while l<=r:
            m = (l+r)//2
                
            if value_arr[m][0] < timestamp:
                result_idx = m
                l = m + 1
            elif value_arr[m][0] > timestamp:
                r = m - 1
            else:
                return value_arr[m][1]
        
        return value_arr[result_idx][1]
        
