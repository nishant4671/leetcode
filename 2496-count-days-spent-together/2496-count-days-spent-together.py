class Solution:
    def countDaysTogether(self, arriveAlice: str, leaveAlice: str, arriveBob: str, leaveBob: str) -> int:
        days_in_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        
        prefix_sum_days = [0] * 13
        for i in range(12):
            prefix_sum_days[i+1] = prefix_sum_days[i] + days_in_month[i]

        def date_to_day_of_year(date_str: str) -> int:
            month = int(date_str[:2])
            day = int(date_str[3:])
            return prefix_sum_days[month - 1] + day

        alice_arrive_day = date_to_day_of_year(arriveAlice)
        alice_leave_day = date_to_day_of_year(leaveAlice)
        bob_arrive_day = date_to_day_of_year(arriveBob)
        bob_leave_day = date_to_day_of_year(leaveBob)
        
        overlap_start = max(alice_arrive_day, bob_arrive_day)
        overlap_end = min(alice_leave_day, bob_leave_day)

        if overlap_start > overlap_end:
            return 0
        else:
            return overlap_end - overlap_start + 1