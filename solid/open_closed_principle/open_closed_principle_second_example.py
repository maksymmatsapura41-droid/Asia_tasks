class Manager:
    billable = 0
    def __init__(self, name, leads_department):
        self.name = name
        self.leads_department = leads_department

    def show_info(self):
        print(f"employee {self.name} is managing {self.leads_department}")


class Programmer:
    def __init__(self, name, billable, programming_language):
        self.name = name
        self.billable = billable
        self.programming_language = programming_language

    def show_info(self):
        print(f"employee programmer {self.name} is programming {self.programming_language}")


class Designer:
    def __init__(self, name, billable, tool):
        self.name = name
        self.billable = billable
        self.tool = tool

    def show_info(self):
        print(f"employee programmer {self.name} using {self.tool}")


def show_employees(employee_list):
    for employee in employee_list:
        employee.show_info()

def show_billable(employee_list):
    billable = 0
    for employee in employee_list:
        billable += employee.billable
    print(f"total billable: {billable}")


employees = [
    Manager("John", "QA"),
    Programmer("Mark", 30, "Java"),
    Designer("Mark", 300, "PhotoShop"),
]

show_employees(employees)
show_billable(employees)

