#Patrick Roscio
# Lab_8 HRManager.py
#Description: Main function for HR manager lab_8. call from worker and supervisor files apprpriate classes and constrcauts the database according
# to the desired number of empoyees. Returns the list of all employees as well as their level, Id number, and approptiate pay, and for worker, shift
# Calculates total cost for the pay per week. 

from worker import Worker
from Supervisor import Supervisor

def calcTotalPay(employees):
    total_pay = 0
    for emp in employees:
        total_pay += emp.calcPay(40)  
    return total_pay

def listEmployees(employees):
    for emp in employees:
        if isinstance(emp, Supervisor):
            print("Supervisor:")
            print("Name:", emp.get_name())
            print("ID:", emp.get_ID())
            print("Pay Rate:", emp.get_pay())
            print("Level:", emp.get_level())
        elif isinstance(emp, Worker):
            print("Worker:")
            print("Name:", emp.get_name())
            print("ID:", emp.get_ID())
            print("Pay Rate:", emp.get_pay())
            print("Shift:", emp.getShift())
        print()

def main():
    employees = []
    num_employees = int(input("How many employees do you wish to add? "))
    while len(employees) <= num_employees - 1:
        emp_type = input("Do you want to add a Supervisor or a Worker? ").lower()
        if emp_type == "supervisor":
            name = input("Enter supervisor's name: ")
            ID = int(input("Enter supervisor's ID: "))
            pay_rate = float(input("Enter supervisor's pay rate: "))
            level = int(input("Enter supervisor's level: "))
            supervisor = Supervisor(name, ID, pay_rate, level)
            employees.append(supervisor)
        elif emp_type == "worker":
            name = input("Enter worker's name: ")
            ID = int(input("Enter worker's ID: "))
            pay_rate = float(input("Enter worker's pay rate: "))
            shift = int(input("Enter worker's shift (1 for day shift, 2 for night shift): "))
            worker = Worker(name, ID, pay_rate, shift)
            employees.append(worker)
        else:
            print(f"{emp_type} is not a worker or supervisor. Try again!")


    print("\nEmployee Information:\n")
    listEmployees(employees)

    total_pay = calcTotalPay(employees)
    print(f"\nTotal Pay for all employees: ${total_pay: 0.2f}")


main()