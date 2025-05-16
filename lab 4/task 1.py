import sqlite3

# Класс Студент
class Student:
    def __init__(self, name, surname, patronymic, group, grade1, grade2, grade3, grade4):
        self.name = name
        self.surname = surname
        self.patronymic = patronymic
        self.group = group
        self.grade1 = grade1
        self.grade2 = grade2
        self.grade3 = grade3
        self.grade4 = grade4

# Подключение к базе данных
conn = sqlite3.connect("students.db")
cursor = conn.cursor()

# Создание таблицы
cursor.execute('''
CREATE TABLE IF NOT EXISTS students (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    surname TEXT,
    patronymic TEXT,
    group_name TEXT,
    grade1 INTEGER,
    grade2 INTEGER,
    grade3 INTEGER,
    grade4 INTEGER
)
''')
conn.commit()

# Добавление студента
def add_student():
    name = input("Имя: ")
    surname = input("Фамилия: ")
    patronymic = input("Отчество: ")
    group = input("Группа: ")
    grade1 = int(input("Оценка 1: "))
    grade2 = int(input("Оценка 2: "))
    grade3 = int(input("Оценка 3: "))
    grade4 = int(input("Оценка 4: "))

    student = Student(name, surname, patronymic, group, grade1, grade2, grade3, grade4)

    cursor.execute('''
        INSERT INTO students (name, surname, patronymic, group_name, grade1, grade2, grade3, grade4)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?)
    ''', (student.name, student.surname, student.patronymic, student.group,
          student.grade1, student.grade2, student.grade3, student.grade4))
    conn.commit()
    print(" Студент добавлен.\n")

# Показ всех студентов
def show_all():
    cursor.execute("SELECT * FROM students")
    students = cursor.fetchall()
    for student in students:
        print(student)
    print()

# Показ одного студента
def show_one():
    id = input("ID студента: ")
    cursor.execute("SELECT * FROM students WHERE id = ?", (id,))
    student = cursor.fetchone()
    if student:
        print("Имя:", student[1])
        print("Фамилия:", student[2])
        print("Отчество:", student[3])
        print("Группа:", student[4])
        print("Оценки:", student[5], student[6], student[7], student[8])
        average = (student[5] + student[6] + student[7] + student[8]) / 4
        print("Средний балл:", average)
    else:
        print(" Студент не найден.")
    print()

# Удаление студента
def delete_student():
    id = input("ID студента для удаления: ")
    cursor.execute("DELETE FROM students WHERE id = ?", (id,))
    conn.commit()
    print("🗑 Удалено.\n")

# Средний балл по группе
def group_avg():
    group = input("Название группы: ")
    cursor.execute("SELECT grade1, grade2, grade3, grade4 FROM students WHERE group_name = ?", (group,))
    rows = cursor.fetchall()
    if rows:
        total = 0
        count = 0
        for row in rows:
            total += row[0] + row[1] + row[2] + row[3]
            count += 4
        print("Средний балл по группе:", total / count)
    else:
        print(" Студентов нет.")
    print()

# Редактирование студента
def edit_student():
    id = input("ID студента для редактирования: ")
    cursor.execute("SELECT * FROM students WHERE id = ?", (id,))
    student = cursor.fetchone()
    if not student:
        print(" Не найден.")
        return

    print("Оставь поле пустым, если менять не нужно.")

    name = input(f"Имя ({student[1]}): ")
    if name == "":
        name = student[1]

    surname = input(f"Фамилия ({student[2]}): ")
    if surname == "":
        surname = student[2]

    patronymic = input(f"Отчество ({student[3]}): ")
    if patronymic == "":
        patronymic = student[3]

    group = input(f"Группа ({student[4]}): ")
    if group == "":
        group = student[4]

    grade1 = input(f"Оценка 1 ({student[5]}): ")
    if grade1 == "":
        grade1 = student[5]
    else:
        grade1 = int(grade1)

    grade2 = input(f"Оценка 2 ({student[6]}): ")
    if grade2 == "":
        grade2 = student[6]
    else:
        grade2 = int(grade2)

    grade3 = input(f"Оценка 3 ({student[7]}): ")
    if grade3 == "":
        grade3 = student[7]
    else:
        grade3 = int(grade3)

    grade4 = input(f"Оценка 4 ({student[8]}): ")
    if grade4 == "":
        grade4 = student[8]
    else:
        grade4 = int(grade4)

    cursor.execute('''
        UPDATE students SET
            name = ?, surname = ?, patronymic = ?, group_name = ?,
            grade1 = ?, grade2 = ?, grade3 = ?, grade4 = ?
        WHERE id = ?
    ''', (name, surname, patronymic, group, grade1, grade2, grade3, grade4, id))
    conn.commit()
    print(" Обновлено.\n")

# Меню
def menu():
    while True:
        print("1 - Добавить")
        print("2 - Показать всех")
        print("3 - Показать одного")
        print("4 - Удалить")
        print("5 - Средний балл по группе")
        print("6 - Редактировать")
        print("0 - Выход")

        choice = input("Выберите: ")
        if choice == "1":
            add_student()
        elif choice == "2":
            show_all()
        elif choice == "3":
            show_one()
        elif choice == "4":
            delete_student()
        elif choice == "5":
            group_avg()
        elif choice == "6":
            edit_student()
        elif choice == "0":
            break
        else:
            print(" Неверный выбор.\n")

# Запуск
menu()
conn.close()