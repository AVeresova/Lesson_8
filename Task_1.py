from datetime import date


class Data:
    def __init__(self, data):
        self.data = data.split('-')

    @classmethod
    def type(cls, data):
        try:
            day, month, year = [int(i) for i in data.split('-')]
            return f"{type(day), day}\n{type(month), month}\n{type(year), year}"
        except ValueError:
            return 'Указана неправильная дата!'

    @staticmethod
    def valid(data):
        try:
            day, month, year = data.split('-')
            date(int(year), int(month), int(day))
            return f'Дата'
        except ValueError:
            return 'Указана неправильная дата!'


print(Data.type('11-11-2020'))
print(Data.valid('11-11-2020'))
