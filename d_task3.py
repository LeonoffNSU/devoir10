import random


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
        if NavalBattle.playing_field == [[0 for x in range(10)] for y in range(10)]:
            print('игровое поле не заполнено')
            return None

        if NavalBattle.playing_field[y - 1][x - 1] == 0:
            print('мимо')
            NavalBattle.playing_field[y - 1][x - 1] = 'o'
        elif NavalBattle.playing_field[y - 1][x - 1] == 1:
            print('попал')
            NavalBattle.playing_field[y - 1][x - 1] = self.__symbol
        else:
            print('ошибка')

    @classmethod
    def random_fields(cls, k: int):
        list_input = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
        while True:
            result = random.sample(list_input, k)
            result.sort()
            if k == 4:
                if result[-1] == result[-2] + 1 == result[-3] + 2 == result[-4] + 3:
                    break
            elif k == 3:
                if result[-1] == result[-2] + 1 == result[-3] + 2:
                    break
            elif k == 2:
                if result[-1] == result[-2] + 1:
                    break
            else:
                break

        return result

    @classmethod
    def add_ship(cls, field_matrix: list, k: int):
        output_field = field_matrix.copy()

        while True:
            orientation = random.choice(['vert', 'hor'])
            axis = random.choice([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
            fields = NavalBattle.random_fields(k)

            if orientation == 'hor':
                cnt = 0
                for i in fields:
                    if output_field[axis][i] == 1 or output_field[axis][i] == '^':
                        cnt += 1
                if cnt == 0:
                    break

            if orientation == 'vert':
                cnt = 0
                for i in fields:
                    if output_field[i][axis] == 1 or output_field[i][axis] == '^':
                        cnt += 1
                if cnt == 0:
                    break

        if orientation == 'hor':
            for i in fields:
                output_field[axis][i] = 1

            if fields[0] - 1 != -1:
                output_field[axis][fields[0] - 1] = '^'

                if axis == 0:
                    output_field[axis + 1][fields[0] - 1] = '^'
                elif axis == 9:
                    output_field[axis - 1][fields[0] - 1] = '^'
                else:
                    output_field[axis + 1][fields[0] - 1] = '^'
                    output_field[axis - 1][fields[0] - 1] = '^'

            if fields[-1] + 1 != 10:
                output_field[axis][fields[-1] + 1] = '^'

                if axis == 0:
                    output_field[axis + 1][fields[-1] + 1] = '^'
                elif axis == 9:
                    output_field[axis - 1][fields[-1] + 1] = '^'
                else:
                    output_field[axis + 1][fields[-1] + 1] = '^'
                    output_field[axis - 1][fields[-1] + 1] = '^'

            if axis == 0:
                for field in fields:
                    output_field[axis + 1][field] = '^'
            elif axis == 9:
                for field in fields:
                    output_field[axis - 1][field] = '^'
            else:
                for field in fields:
                    output_field[axis + 1][field] = '^'
                    output_field[axis - 1][field] = '^'

        if orientation == 'vert':
            for i in fields:
                output_field[i][axis] = 1

            if fields[0] - 1 != -1:
                output_field[fields[0] - 1][axis] = '^'

                if axis == 0:
                    output_field[fields[0] - 1][axis + 1] = '^'
                elif axis == 9:
                    output_field[fields[0] - 1][axis - 1] = '^'
                else:
                    output_field[fields[0] - 1][axis + 1] = '^'
                    output_field[fields[0] - 1][axis - 1] = '^'

            if fields[-1] + 1 != 10:
                output_field[fields[-1] + 1][axis] = '^'

                if axis == 0:
                    output_field[fields[-1] + 1][axis + 1] = '^'
                elif axis == 9:
                    output_field[fields[-1] + 1][axis - 1] = '^'
                else:
                    output_field[fields[-1] + 1][axis + 1] = '^'
                    output_field[fields[-1] + 1][axis - 1] = '^'

            if axis == 0:
                for field in fields:
                    output_field[field][axis + 1] = '^'
            elif axis == 9:
                for field in fields:
                    output_field[field][axis - 1] = '^'
            else:
                for field in fields:
                    output_field[field][axis - 1] = '^'
                    output_field[field][axis + 1] = '^'

        return output_field

    @classmethod
    def new_game(cls):
        playing_field = [[0 for x in range(10)] for y in range(10)]
        playing_field = NavalBattle.add_ship(playing_field, 4)
        playing_field = NavalBattle.add_ship(playing_field, 3)
        playing_field = NavalBattle.add_ship(playing_field, 3)
        playing_field = NavalBattle.add_ship(playing_field, 2)
        playing_field = NavalBattle.add_ship(playing_field, 2)
        playing_field = NavalBattle.add_ship(playing_field, 2)
        playing_field = NavalBattle.add_ship(playing_field, 1)
        playing_field = NavalBattle.add_ship(playing_field, 1)
        playing_field = NavalBattle.add_ship(playing_field, 1)
        playing_field = NavalBattle.add_ship(playing_field, 1)

        index_sym = []
        y = -1
        for row in playing_field:
            y += 1
            for x, elem in enumerate(row):
                if elem == '^':
                    index_sym.append((x, y))

        for coords in index_sym:
            playing_field[coords[1]][coords[0]] = 0

        NavalBattle.playing_field = playing_field
