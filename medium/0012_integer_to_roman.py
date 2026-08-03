"""Given an integer, convert it to a Roman numeral."""

class Solution:
    def intToRoman(self, num: int) -> str:
        converts = {
            1:"I", 
            5:"V", 
            10:"X", 
            50:"L", 
            100:"C", 
            500:"D", 
            1000:"M"}
        roman = []
        i = 1
        while num//i != 0:
            digit = num // i % 10
            if digit <= 3:
                roman = digit*[converts[i]] + roman
            elif digit == 4:
                roman = [converts[i], converts[i*5]] + roman
            elif digit <= 8:
                roman = [converts[i*5]] + digit%5*[converts[i]] + roman
            else:
                roman = [converts[i], converts[i*10]] + roman
            i = i*10
        return "".join(roman)