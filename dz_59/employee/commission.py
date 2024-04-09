from employee import salary


class CommissionEmloyee(salary.SalaryEmployee):
    """Торговые представители, фиксированная зарплата + коммисия"""

    def __init__(self, kod, name, weekly_salary, commission):
        super().__init__(kod, name, weekly_salary)
        self.commission = commission

    def calculate_payroll(self):
        fixid = super().calculate_payroll()
        return fixid + self.commission

if __name__ == '__main__':
    commision_employee = CommissionEmloyee(3, "Николай Хорольский", 1000, 250)
    print(commision_employee.calculate_payroll())
