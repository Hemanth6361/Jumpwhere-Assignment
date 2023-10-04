# Write a python class to convert an integer into a roman numeral and viceversa
class RomanConverter:
    def int_to_roman(self, num):
        val = [
            1000, 900, 500, 400,
            100, 90, 50, 40,
            10, 9, 5, 4,
            1
            ]
        syb = [
            "M", "CM", "D", "CD",
            "C", "XC", "L", "XL",
            "X", "IX", "V", "IV",
            "I"
            ]
        roman_num = ''
        i = 0
        while  num > 0:
            for _ in range(num // val[i]):
                roman_num += syb[i]
                num -= val[i]
            i += 1
        return roman_num

    def roman_to_int(self, s):
        val_dict = {
            "I": 1, "V": 5, "X": 10,
            "L": 50, "C": 100, "D": 500,
            "M": 1000
            }
        num = 0
        prev_val = 0
        for c in s:
            if val_dict[c] > prev_val:
                num += val_dict[c] - 2 * prev_val
            else:
                num += val_dict[c]
            prev_val = val_dict[c]
        return num
converter = RomanConverter()
print(converter.int_to_roman(3549))  
print(converter.roman_to_int('MMMDXLIX')) 
