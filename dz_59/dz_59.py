from employee import salary, hourly, commission

class PayrollSystem:
    def calculate(self, emplotees):
        print("Расчет заработной платы")
        print("=" * 50)
        for emplotee in emplotees:
            print(f"Заработная плата: {emplotee.id} - {emplotee.name}")
            print(f"- Проверить сумму: {emplotee.calculate_payroll()}")
            print()


salary_employee = salary.SalaryEmployee(1, "Валерий Задорожный", 1500)
hourly_employee = hourly.HourlyEmployee(2, "Илья Кромин", 40, 15)
commision_employee = commission.CommissionEmloyee(3, "Николай Хорольский", 1000, 250)

payroll_system = PayrollSystem()
payroll_system.calculate([
    salary_employee,
    hourly_employee,
    commision_employee
])
