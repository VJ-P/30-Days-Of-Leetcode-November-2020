class Solution:
    def atMostNGivenDigitSet(self, digits: List[str], n: int) -> int:
        total = 0
        digits.sort(key = lambda x : int(x))
        
        len_n = len(str(n))
        string_n = str(n)
        len_digits = len(digits)
        
        for i in range(1, len_n):
            total += len_digits ** i
        
        i = 0
        while i < len_n:
            j = 0
            while j < len_digits and digits[j] < string_n[i]:
                total += len_digits ** (len_n - 1 - i)
                j += 1
            if j == len_digits or digits[j] > string_n[i]:
                break
            i += 1
        
        if i == len(string_n):
            total += 1
        
        return total