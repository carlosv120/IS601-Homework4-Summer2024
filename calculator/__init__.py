from calculator.calculation import Calculation
from calculator.operations import add, subtract, multiply, divide

class Calculator:
    @staticmethod
    def addition(num1,num2):

        calculation = Calculation(num1, num2, add)
        return calculation.get_result()
    
    @staticmethod
    def subtraction(num1,num2):

        calculation = Calculation(num1, num2, subtract)
        return calculation.get_result()
    
    @staticmethod
    def multiplication(num1,num2):

        calculation = Calculation(num1, num2, multiply)
        return calculation.get_result()
    
    @staticmethod
    def division(num1,num2):
        
        calculation = Calculation(num1, num2, divide)
        return calculation.get_result()