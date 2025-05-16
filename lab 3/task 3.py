class Calculation:
    def __init__(self):
        self.line = ""

    def set(self, text):
        self.line = text

    def add(self, symbol):
        self.line += symbol

    def get(self):
        return self.line

    def last(self):
        if len(self.line) == 0:
            return ""
        else:
            return self.line[-1]

    def delete_last(self):
        self.line = self.line[:-1]



calc = Calculation()

# Устанавливаем начальную строку
calc.set("12389")
print("Текущая строка:", calc.get())


# Добавляем символ
calc.add("6")
print("После добавления символа:", calc.get())
# Выведет: После добавления символа: 123456

# Получаем последний символ
last_char = calc.last()
print("Последний символ:", last_char)
# Выведет: Последний символ: 6

# Удаляем последний символ
calc.delete_last()
print("После удаления последнего символа:", calc.get())
# Выведет: После удаления последнего символа: 12345
