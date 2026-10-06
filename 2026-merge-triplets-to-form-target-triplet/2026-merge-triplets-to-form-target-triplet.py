class Solution:
    def mergeTriplets(self, triplets: list[list[int]], target: list[int]) -> bool:
        found_max_components = [0, 0, 0]
        
        tx, ty, tz = target
        
        for a, b, c in triplets:
            if a <= tx and b <= ty and c <= tz:
                found_max_components[0] = max(found_max_components[0], a)
                found_max_components[1] = max(found_max_components[1], b)
                found_max_components[2] = max(found_max_components[2], c)
            
            if found_max_components[0] == tx and \
               found_max_components[1] == ty and \
               found_max_components[2] == tz:
                return True
                
        return found_max_components[0] == tx and \
               found_max_components[1] == ty and \
               found_max_components[2] == tz