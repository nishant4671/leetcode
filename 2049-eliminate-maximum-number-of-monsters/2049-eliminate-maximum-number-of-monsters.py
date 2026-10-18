class Solution:
    def eliminateMaximum(self, dist: list[int], speed: list[int]) -> int:
        n = len(dist)
        
        # Calculate the critical arrival time for each monster.
        # This is the latest minute (0-indexed) at which we must eliminate
        # the monster to prevent it from reaching the city.
        # A monster at distance `d` with speed `s` takes `d / s` minutes to reach the city.
        # According to the problem: "If a monster reaches the city at the exact moment
        # the weapon is fully charged, it counts as a loss, and the game ends before you can use your weapon."
        # This implies that if a monster reaches at time `T` (e.g., `dist[i]/speed[i]`),
        # we must have eliminated it at some integer minute `k` such that `k < T`.
        # The largest such integer `k` is `floor(T - epsilon)`, which for positive `dist[i]`
        # and `speed[i]` can be computed as `(dist[i] - 1) // speed[i]`.
        # Example: dist=1, speed=1 => T=1. Must kill at minute 0. (1-1)//1 = 0.
        # Example: dist=3, speed=1 => T=3. Must kill by minute 2. (3-1)//1 = 2.
        # Example: dist=4, speed=3 => T=1.33... Must kill by minute 1. (4-1)//3 = 1.
        
        critical_elimination_minutes = []
        for i in range(n):
            critical_elimination_minutes.append((dist[i] - 1) // speed[i])
        
        # Sort these critical times in ascending order.
        # To maximize the number of eliminated monsters, we should always eliminate
        # the monsters that pose the most immediate threat (i.e., those that arrive earliest).
        critical_elimination_minutes.sort()
        
        eliminated_count = 0
        
        # Iterate through the sorted critical elimination times.
        # `k` represents the current minute (0-indexed) at which we are ready to fire
        # our (k+1)-th weapon shot.
        # We fire the 1st shot at minute 0, 2nd shot at minute 1, and so on.
        # So, the (k+1)-th shot is available at minute `k`.
        for k in range(n):
            # If the k-th monster (in the sorted list) must be eliminated
            # by minute `critical_elimination_minutes[k]`, and our (k+1)-th shot
            # is available at minute `k`.
            # If `critical_elimination_minutes[k] >= k`, it means this monster will not
            # reach the city *before* or *at* the moment our weapon is charged at minute `k`.
            # Therefore, we can eliminate it.
            if critical_elimination_minutes[k] >= k:
                eliminated_count += 1
            else:
                # If `critical_elimination_minutes[k] < k`, it means this monster
                # would reach the city *before* minute `k` (the time our current shot is ready).
                # Since we cannot eliminate it in time, we lose.
                # We cannot eliminate any more monsters, so we break and return the count.
                break
                
        return eliminated_count