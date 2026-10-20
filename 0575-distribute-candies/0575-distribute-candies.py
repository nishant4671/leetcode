class Solution:
    def distributeCandies(self, candyType: list[int]) -> int:
        n = len(candyType)
        max_candies_to_eat = n // 2
        
        unique_candy_types = set(candyType)
        num_unique_types = len(unique_candy_types)
        
        return min(num_unique_types, max_candies_to_eat)