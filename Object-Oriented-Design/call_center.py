"""
Imagine you have a call center with three levels of employees: respondents, manager, and director. An incoming
telephone call must be first allocated to a respondent who is free. If the respondent can't handle the call, 
he or she must escalate the call to a manager. If the the manager is not free or not able to handle it, then
the call should be escalated to a director. Design the classes and data stuctures for this problem. Implement
a method dispactchCall() which assigns a call to the first available employee. 

Notes:
Need an Employee Class - should have methods take_call or end_call
Need a Call class
Needs Respondent, Manager, Director class that inherits from Employee to represent different employee levels
Needs Call Center- manages employees and handles call dispatching 
"""

class Call:
    def __init__(self,caller):
        self.caller = caller
        self.handler = None
    
    def set_handler(self,employee):
        self.handler = employee

    def end_call(self):
        self.handler = None

class Employee:
    def __init__(self, name, title, is_free=True):
        self.name = name
        self.title = title
        self.is_free = is_free

    def take_call(self,call):
        self.is_free = False
        call.set_handler(self)

    def end_call(self,call):
        call.end_call()
        self.is_free = True

class Respondent(Employee):
    def __init__(self,name):
        super().__init__(name,"Respondent")

class Manager(Employee):
    def __init__(self,name):
        super().__init__(name,"Manager")

class Director(Employee):
    def __init__(self, name,):
        super().__init__(name, "Director")


class CallCenter:
    def __init__(self):
        self.respondents = []
        self.managers = []
        self.directors = []

        # Initialize employees
        self._initialize_employees()

    def _initialize_employees(self):
        # Create instance of Respondents, Managers, and Directors
        # Add them to the appropriate lists
        self.respondents = [Respondent("Respondent 1"),Respondent("Respondent 2")]
        self.managers = [Manager("Manager 1"), Manager("Manager 2")]
        self.directors = [Director("Director 1")]


    def _dispatch_call(self,employee_type):
        employees = getattr(self,employee_type.lower() + 's')
        for employee in employees:
            if employee.is_free:
                return employee
        return None
    
    def dispatch_call(self):
        for employee_type in ["Respondent","Manager","Director"]:
            employee = self._dispatch_call(employee_type)
            if employee:
                return employee
        return None # no available employee
    
    def handle_call(self,call):
        employee = self.dispatch_call()
        if employee:
            employee.take_call(call)
            print(f"{employee.title}{employee.name} is handling the call from {call.caller}")
        else:
            print("No available employee to handle the call")


call_center = CallCenter()
call1 = Call("Caller 1")
call_center.handle_call(call1)

call2 = Call("Caller 2")
call_center.handle_call(call2)
call3 = Call("Caller 3")
call_center.handle_call(call3)

