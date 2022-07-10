class Solution:
    def romanToInt(self, s: str) -> int:
        # this one is faster
        roman_dict = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000,
        }
        num = 0
        for i in range(len(s)):
            if i == len(s) - 1:
                num += roman_dict[s[i]]
            elif roman_dict[s[i]] >= roman_dict[s[i + 1]]:
                num += roman_dict[s[i]]
            else:
                num -= roman_dict[s[i]]
        return num

    def romanToInt2(self, s: str) -> int:
        double_digit_roman = {
            "CM": 900,
            "CD": 400,
            "XC": 90,
            "XL": 40,
            "IX": 9,
            "IV": 4,
        }
        single_digit_roman = {
            "M": 1000,
            "D": 500,
            "C": 100,
            "L": 50,
            "X": 10,
            "V": 5,
            "I": 1,
        }
        integer_output = 0
        i = 0  # string pointer
        while i < len(s):
            # check if 2 characters are in the double_digit_roman dictionary
            if (i < len(s) - 1) and (s[i : i + 2] in double_digit_roman):
                # then get the integer from dictionary and add to output
                integer_output += double_digit_roman[s[i : i + 2]]
                # skip the next character by adding 2 to the pointer
                i += 2
            elif s[i] in single_digit_roman:
                # this string is a single digit roman numeral
                integer_output += single_digit_roman[s[i]]
                # go to next character
                i += 1
        return integer_output


if __name__ == "__main__":
    s = Solution()
    print(s.romanToInt("III"))
    print(s.romanToInt("LVIII"))
    print(s.romanToInt("MCMXCIV"))

    print(s.romanToInt2("III"))
    print(s.romanToInt2("LVIII"))
    print(s.romanToInt2("MCMXCIV"))
