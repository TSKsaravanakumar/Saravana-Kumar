class Calculator:

    def __init__(self,num1,num2):
        self.num1=num1
        self.num2=num2

    def add(self):
        return print(self.num1+self.num2)
    def subtract(self):
        return print(self.num2-self.num1)
    def multiply(self):
        return print(self.num1*self.num2)
    def divide(self):
        return print(self.num2/self.num1)
obj = Calculator(10,94)
obj.add()
obj.subtract()
obj.multiply()
obj.divide()