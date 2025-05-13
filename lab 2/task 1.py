class Student:
    def __init__(self, name, birth, group, grades):
        # Сохраняем данные студента
        self.name = name
        self.birth = birth
        self.group = group
        self.grades = grades  # список оценок

    def show(self):
        # Вывод информации о студенте
        print("Фамилия:", self.name)
        print("Дата рождения:", self.birth)
        print("Группа:", self.group)
        print("Оценки:", self.grades)

    def update(self, name=None, birth=None, group=None):
        # Обновление данных, если введено новое значение
        if name:
            self.name = name
        if birth:
            self.birth = birth
        if group:
            self.group = group


students = []  # список всех студентов

while True:
    # Главное меню
    print("\n1. Добавить студента")
    print("2. Изменить данные студента")
    print("3. Показать информацию о студенте")
    print("4. Выход")

    choice = input("Выберите: ")

    if choice == "1":
        # Ввод данных нового студента
        name = input("Фамилия: ")
        birth = input("Дата рождения: ")
        group = input("Группа: ")
        grades_input = input("Оценки (через запятую): ")

        # Преобразуем строки в числа
        grades_str = grades_input.split(",")  # получаем список строк
        grades = []  # создаём пустой список оценок
        for g in grades_str:
            grades.append(int(g.strip()))  # преобразуем каждую строку в число и добавляем

        # Создаём и добавляем студента в список
        students.append(Student(name, birth, group, grades))
        print("Студент добавлен.")

    elif choice == "2":
        # Изменение данных студента
        name = input("Фамилия: ")
        birth = input("Дата рождения: ")
        found = False

        for s in students:
            if s.name == name and s.birth == birth:
                # Ввод новых данных
                new_name = input("Новая фамилия (Enter — не менять): ")
                new_birth = input("Новая дата (Enter — не менять): ")
                new_group = input("Новая группа (Enter — не менять): ")
                s.update(new_name if new_name else None, new_birth if new_birth else None, new_group if new_group else None)
                print("Данные обновлены.")
                found = True
                break

        if not found:
            print("Студент не найден.")

    elif choice == "3":
        # Поиск и вывод информации
        name = input("Фамилия: ")
        birth = input("Дата рождения: ")
        found = False

        for s in students:
            if s.name == name and s.birth == birth:
                s.show()
                found = True
                break

        if not found:
            print("Студент не найден.")

    elif choice == "4":
        # Завершение работы
        print("Выход.")
        break

    else:
        print("Неверный ввод.")
