class Train:
    def __init__(self, destination, number, time):
        self.destination = destination
        self.number = number
        self.time = time

    def show(self):
        print("Пункт назначения:", self.destination)
        print("Номер поезда:", self.number)
        print("Время отправления:", self.time)


trains = []

while True:
    print("\n1. Добавить поезд\n2. Найти поезд\n3. Выход")
    choice = input("Выберите: ")

    if choice == "1":
        d = input("Пункт назначения: ")
        n = input("Номер: ")
        t = input("Время: ")
        trains.append(Train(d, n, t))

    elif choice == "2":
        n = input("Введите номер поезда: ")
        for train in trains:
            if train.number == n:
                train.show()
                break
        else:
            print("Не найден.")

    elif choice == "3":
        break