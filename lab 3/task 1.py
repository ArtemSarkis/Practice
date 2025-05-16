class Worker:
    def __init__(self, name, surname, rate, days):
        self.name = name
        self.surname = surname
        self.rate = rate
        self.days = days

    def GetSalary(self):
        salary = self.rate * self.days
        print(f"Зарплата работника {self.name} {self.surname}: {salary}")

worker = Worker("Саркисян", "Артём", 70000, 31)
worker.GetSalary()