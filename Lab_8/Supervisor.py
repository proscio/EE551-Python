#Patrick Roscio
# Lab_8 supervisor.py
#Description: class deffinition for the supervisor employee type. Subset of employee with added private variable: level. Also includes
# modicication to the calc_pay to add bonus pay according to supervsior level.  

from Employee import Employee

class Supervisor(Employee):
    def __init__(self, name, ID, pay_rate, level):
        super().__init__(name, ID, pay_rate)
        self.__level = level

    def get_level(self):
        return self.__level

    def set_level(self, level):
        self.__level = level

    def calcPay(self, hours_worked):
        base_pay = super().calcPay(hours_worked) 
        bonus = 1000.00 * self.__level 
        return base_pay + bonus
