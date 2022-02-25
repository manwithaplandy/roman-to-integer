class Solution(object):
    values = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}

    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        Iterate through each letter, determine if the value is higher or lower than the preceding       letter, add or subtract as necessary
        """
        total = 0
        prevnum = 0
        firstnum = False
        addnum = 0
        skip = False

        for a in s:
            if prevnum == 0:  # Set first number to a
                prevnum = a
            elif skip:
                skip = False
                prevnum = a
                continue
            else:
                if self.values[prevnum] > self.values[a] or self.values[prevnum] == self.values[a]:
                    total += self.values[prevnum]
                    prevnum = a
                else: # prevnum < a
                    total += self.values[a] - self.values[prevnum]
                    prevnum = a
                    skip = True
        if not skip:
            total += self.values[prevnum]
        print(total)
        return total

solution = Solution()

solution.romanToInt('III')
solution.romanToInt('LVIII')
solution.romanToInt('MCMXCIV')
