from typing import List

from calculator.calculation import Calculation

class Calculations_History:
    history:List[Calculation] =[]

    @classmethod #They are class methods because they are referencing the class method of hystory. Have access to the global data inside the class
    def add_calculation(cls,calculation:Calculation):
        '''Adding new calculation to list'''
        cls.history.append(calculation)


    @classmethod
    def get_history(cls) -> List[Calculation]:
        '''Get the entire list'''
        return cls.history

    @classmethod
    def clear_history(cls):
        '''Clears the history of calculations'''
        cls.history.clear()

    @classmethod
    def get_latest(cls) -> Calculation:
        '''Getting the latest in the list'''
        if cls.history:
            return cls.history[-1]
        return None
    
    @classmethod
    def find_by_operation(cls,operation_name:str) -> List[Calculation]:
        '''Finding a list of operations by operation'''
        return [calc for calc in cls.history if calc.operation.__name__ == operation_name]