class ZeroError(Exception):
    def __init__(self, txt):
        self.txt = txt


def div():
    try:
        number_1 = int(input('Введите делимое: '))
        number_2 = int(input('Введите делитель: '))
        if number_2 == 0:
            raise ZeroError("Делить на ноль нельзя!")
        else:
            result = number_1 / number_2
            return result
    except ValueError:
        return "Неверно"
    except ZeroError as err:
        return err


print(div())