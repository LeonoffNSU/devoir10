import re


class RomanNumber:

    def __init__(self, roman_number: int | str):
        if isinstance(roman_number, str):
            self.rom_value = roman_number
            if not self.is_roman(roman_number):
                print('ошибка')
                self.rom_value = None

            if self.rom_value is not None:
                self.int_value = self.decimal_number()
            else:
                self.int_value = None

        else:
            self.int_value = roman_number
            if not self.is_int(roman_number):
                print('ошибка')
                self.int_value = None

            if self.int_value is not None:
                self.rom_value = self.roman_number()
            else:
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

    @staticmethod
    def is_int(value: int):
        if 0 < value <= 3999:
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

    def roman_number(self):
        int_to_str = str(self.int_value)
        size = len(int_to_str)
        roman = ''
        translator_units = {1: 'I', 2: 'II', 3: 'III', 4: 'IV', 5: 'V', 6: 'VI', 7: 'VII', 8: 'VIII', 9: 'IX'}
        translator_tens = {1: 'X', 2: 'XX', 3: 'XXX', 4: 'XL', 5: 'L', 6: 'LX', 7: 'LXX', 8: 'LXXX', 9: 'XC'}
        translator_hundreds = {1: 'C', 2: 'CC', 3: 'CCC', 4: 'CD', 5: 'D', 6: 'DC', 7: 'DCC', 8: 'DCCC', 9: 'CM'}
        translator_thousands = {1: 'M', 2: 'MM', 3: 'MMM'}

        if '0' in int_to_str:
            if size == 2:
                roman = translator_tens[int(int_to_str[0])]

            if size == 3:
                if self.int_value % 100 == 0:
                    roman = translator_hundreds[int(int_to_str[0])]
                elif self.int_value % 10 == 0:
                    roman = translator_hundreds[int(int_to_str[0])] + translator_tens[int(int_to_str[1])]
                else:
                    roman = translator_hundreds[int(int_to_str[0])] + translator_units[int(int_to_str[2])]

            if size == 4:
                roman = translator_thousands[int(int_to_str[0])]
                if int_to_str[1] != '0':
                    roman += translator_hundreds[int(int_to_str[1])]
                if int_to_str[2] != '0':
                    roman += translator_tens[int(int_to_str[2])]
                if int_to_str[3] != '0':
                    roman += translator_units[int(int_to_str[3])]
            return roman

        else:
            if size == 1:
                roman = translator_units[int(int_to_str)]
            if size == 2:
                roman = translator_tens[int(int_to_str[0])] + translator_units[int(int_to_str[1])]
            if size == 3:
                roman = (translator_hundreds[int(int_to_str[0])] + translator_tens[int(int_to_str[1])] +
                         translator_units[int(int_to_str[2])])
            if size == 4:
                roman = (translator_thousands[int(int_to_str[0])] + translator_hundreds[int(int_to_str[1])] +
                         translator_tens[int(int_to_str[2])] + translator_units[int(int_to_str[3])])
            return roman
