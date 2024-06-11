class Calculation:
    def __init__(self, num1, num2, operation):
        self.num1 = num1
        self.num2 = num2
        self.operation = operation

    def get_result(self):
        
        return self.operation(self.num1,self.num2)