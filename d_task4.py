import re


class RomanNumber:

    def __init__(self, roman_number: str):
        self.rom_value = roman_number
        if not self.is_roman(roman_number):
            print('ошибка')
            self.rom_value = None

    @staticmethod
    def is_roman(value: str):
        valid_symbols = ('I', 'V', 'X', 'L', 'C', 'D', 'M')

        if len(value) == 0:
            return False
        if type(value) != str:
            print('Введенное значение не является строкой')
            return False
        for sym in value:
            if sym not in valid_symbols:
                return False

        pattern = r'^M{0,3}(CM|CD|D?C{0,3})?(XC|XL|L?X{0,3})?(IX|IV|V?I{0,3})?$'
        if re.match(pattern, value):
            return True
        return False

    def decimal_number(self):
        try:
            cnt = 0
            valid_symbols = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
            roman = self.rom_value
            if 'IX' in roman:
                cnt += 9
                roman = roman.replace('IX', '')
            if 'IV' in roman:
                cnt += 4
                roman = roman.replace('IV', '')
            if 'XC' in roman:
                cnt += 90
                roman = roman.replace('XC', '')
            if 'XL' in roman:
                cnt += 40
                roman = roman.replace('XL', '')
            if 'CM' in roman:
                cnt += 900
                roman = roman.replace('CM', '')
            if 'CD' in roman:
                cnt += 400
                roman = roman.replace('CD', '')

            for sym in roman:
                cnt += valid_symbols[sym]
            return cnt
        except TypeError:
            pass
