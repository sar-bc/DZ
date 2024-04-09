# from employee import salary, hourly, commission
from employee.salary import SalaryEmployee
from employee.hourly import HourlyEmployee
from employee.commission import CommissionEmloyee

class PayrollSystem:
    def calculate(self, emplotees):
        print("Расчет заработной платы")
        print("=" * 50)
        for emplotee in emplotees:
            print(f"Заработная плата: {emplotee.id} - {emplotee.name}")
            print(f"- Проверить сумму: {emplotee.calculate_payroll()}")
            print()


salary_employee = SalaryEmployee(1, "Валерий Задорожный", 1500)
hourly_employee = HourlyEmployee(2, "Илья Кромин", 40, 15)
commision_employee = CommissionEmloyee(3, "Николай Хорольский", 1000, 250)

payroll_system = PayrollSystem()
payroll_system.calculate([
    salary_employee,
    hourly_employee,
    commision_employee
])
