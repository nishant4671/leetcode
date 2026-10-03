class Solution:
    def daysBetweenDates(self, date1: str, date2: str) -> int:

        # Days in months for a non-leap year (index 0 is a dummy)
        days_in_month_common = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

        def is_leap(year):
            """Determines if a given year is a leap year."""
            return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

        def count_leap_years_from_1_to(year):
            """Counts the number of leap years from year 1 up to and including 'year'."""
            # Uses the Gregorian calendar rules.
            # For example, year 1900 is not a leap year, 2000 is.
            if year < 0: # Handle edge case for year 0 or negative years, though not relevant for problem constraints.
                return 0
            return year // 4 - year // 100 + year // 400

        def get_total_days_since_1970_01_01(date_str):
            """
            Calculates the total number of days from 1970-01-01 to the given date (inclusive).
            1970-01-01 is considered day 1 in this counting scheme.
            """
            year_str, month_str, day_str = date_str.split('-')
            year, month, day = int(year_str), int(month_str), int(day_str)

            total_days = 0
            
            # 1. Add days for all full years passed since 1970 (up to year-1)
            # Example: if year is 1971, this calculates days for 1970.
            # If year is 1970, this calculates days for an empty range (0 days).
            
            # Calculate the number of leap years between 1970 and (year-1) inclusive.
            # (year - 1) is the upper bound for the full years passed.
            # 1969 is the year before our reference epoch start (1970).
            num_leap_years_in_prev_full_years = count_leap_years_from_1_to(year - 1) - count_leap_years_from_1_to(1969)
            
            total_days += (year - 1970) * 365 + num_leap_years_in_prev_full_years

            # 2. Add days for all full months passed in the current year (January to month-1)
            for m in range(1, month):
                total_days += days_in_month_common[m]
                # If it's February and the current year is a leap year, add an extra day.
                if m == 2 and is_leap(year):
                    total_days += 1

            # 3. Add the day of the current month
            total_days += day

            return total_days

        # Calculate the total days for both dates from the common epoch (1970-01-01)
        days1_count = get_total_days_since_1970_01_01(date1)
        days2_count = get_total_days_since_1970_01_01(date2)

        # The absolute difference is the number of days between the two dates.
        return abs(days1_count - days2_count)