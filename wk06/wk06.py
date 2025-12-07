with open("wk06/hr_system.txt") as employees:
    next(employees)
    for employee in employees:
        employee_info = employee.strip().split()
        pay_check = float(employee_info[3]) / 24
        if employee_info[2].lower() == "engineer":
            pay_check += 1000
        print(f"{employee_info[0]} (ID: {employee_info[1]}), {employee_info[2]} - ${pay_check:.2f}")