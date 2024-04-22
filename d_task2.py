class NavalBattle:
    playing_field = [[0 for x in range(10)] for y in range(10)]

    def __init__(self, symbol: str):
        self.__symbol = symbol

    @staticmethod
    def show():
        for row in NavalBattle.playing_field:
            for index, value in enumerate(row):
                if type(value) == int and index != 9:
                    print('~', end='')
                elif type(value) == int and index == 9:
                    print('~')
                elif type(value) == str and index != 9:
                    print(value, end='')
                else:
                    print(value)

    def shot(self, x: int, y: int):
        if NavalBattle.playing_field[y - 1][x - 1] == 0:
            print('мимо')
            NavalBattle.playing_field[y - 1][x - 1] = 'o'
        elif NavalBattle.playing_field[y - 1][x - 1] == 1:
            print('попал')
            NavalBattle.playing_field[y - 1][x - 1] = self.__symbol
