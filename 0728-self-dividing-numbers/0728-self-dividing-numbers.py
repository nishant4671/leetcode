class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> list[int]:
        
        result = []
        
        def is_self_dividing(n: int) -> bool:
            temp_num = n
            while temp_num > 0:
                digit = temp_num % 10
                if digit == 0 or n % digit != 0:
                    return False
                temp_num //= 10
            return True

        for num in range(left, right + 1):
            if is_self_dividing(num):
                result.append(num)
                
        return result