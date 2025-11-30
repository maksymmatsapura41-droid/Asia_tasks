class Manager:
    def __init__(self, name, leads_department):
        self.name = name
        self.leads_department = leads_department

class Programmer:
    def __init__(self, name, billable, programming_language):
        self.name = name
        self.billable = billable
        self.programming_language = programming_language


def show_employees(employee_list):
    for employee in employee_list:
        if type(employee) is Manager:
            print(f"employee {employee.name} is managing {employee.leads_department}")
        elif type(employee) is Programmer:
            print(f"employee programmer {employee.name} is programming {employee.programming_language}")


def show_billable(employee_list):
    billable = 0
    for employee in employee_list:
        if type(employee) is Programmer:
            billable += employee.billable
    print(f"total billable: {billable}")


employees = [
    Manager("John", "QA"),
    Programmer("Mark", 30, "Java"),
]

show_employees(employees)
show_billable(employees)

