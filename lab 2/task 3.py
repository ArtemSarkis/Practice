class NumberPair:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def show(self):
        print("Число 1:", self.a)
        print("Число 2:", self.b)

    def change(self):
        print("Изменение чисел:")
        self.a = int(input("Введите новое значение для числа 1: "))
        self.b = int(input("Введите новое значение для числа 2: "))

    def get_sum(self):
        return self.a + self.b

    def get_max(self):
        if self.a > self.b:
            return self.a
        else:
            return self.b

# Создание объекта
print("Введите два целых числа:")
x = int(input("Число 1: "))
y = int(input("Число 2: "))
pair = NumberPair(x, y) #создает обьект x, y и сохраняет в pair, позволяет обращаться к медотам обьекта

# Меню для пользователя
while True:
    print("\nМеню:")
    print("1 - Показать числа")
    print("2 - Изменить числа")
    print("3 - Найти сумму")
    print("4 - Найти наибольшее число")
    print("5 - Выход")

    choice = input("Выберите действие: ")

    if choice == "1":
        pair.show()
    elif choice == "2":
        pair.change()
    elif choice == "3":
        print("Сумма чисел:", pair.get_sum())
    elif choice == "4":
        print("Наибольшее число:", pair.get_max())
    elif choice == "5":
        print("Программа завершена.")
        break
    else:
        print("Неверный выбор. Попробуйте снова.")