class Solution:
    def myAtoi(self, s: str) -> int:
        str = s.strip()
        negative = False
        if str and str[0] == '-':
            negative = True
        if str and (str[0] == '+' or str[0] == '-'):
            str = str[1:]
        if not str:
            return 0
        
        digits = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}
        result = 0
        for c in str:
            if c not in digits:
                break
            result = result * 10 + digits[c]
        if negative:
            result = -result
        
        result = max(min(result,2**31-1),-2**31)
        return result

if __name__ == "__main__":
    s = Solution()
    print(s.myAtoi("-42"))
