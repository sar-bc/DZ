from employee import employee
# from employee import Employee


class HourlyEmployee(employee.Employee):
    """Сотрудники с почасовой оплатой"""

    def __init__(self, kod, name, hours_worked, house_rate):
        super().__init__(kod, name)
        self.hours_worked = hours_worked
        self.house_rate = house_rate

    def calculate_payroll(self):
        return self.hours_worked * self.house_rate

if __name__ == '__main__':
    hourly_employee = HourlyEmployee(2, "Илья Кромин", 40, 15)
    print(hourly_employee.calculate_payroll())
