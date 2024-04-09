from employee import employee


class SalaryEmployee(employee.Employee):
    """Административные сотрудники, имеют фиксированную зарплату"""

    def __init__(self, kod, name, weekly_salary):
        super().__init__(kod, name)
        self.weekly_salary = weekly_salary

    def calculate_payroll(self):
        return self.weekly_salary

if __name__ == '__main__':
    salary_employee = SalaryEmployee(1, "Валерий Задорожный", 1500)
    print(salary_employee.calculate_payroll())

