class Solution:
    def myAtoi(self, s: str) -> int:
        res = 0
        i = 0
        sign = 1
        n = len(s)

        # Skip leading whitespaces
        while i < n and s[i] == ' ':
            i += 1

        # Check if the next character is a sign
        if i < n and (s[i] == '-' or s[i] == '+'):
            sign = -1 if s[i] == '-' else 1
            i += 1

        # Convert the digits to an integer
        while i < n and s[i].isdigit():
            res = res * 10 + int(s[i])
            i += 1

        return max(-2**31, min(sign * res, 2**31 - 1))
        
        