class Expression:
    def __init__(self, operand1, operand2, operator):
        self.operand1 = operand1
        self.operand2 = operand2
        self.operator = operator

    def evaluate(self):
        if self.operator == '+':
            result = self.operand1 + self.operand2
        elif self.operator == '-':
            result = self.operand1 - self.operand2
        elif self.operator == '*':
            result = self.operand1 * self.operand2
        elif self.operator == '/':
            if self.operand2 == 0:
                return "Cannot divide by 0"
            result = self.operand1 / self.operand2
        elif self.operator == '%':
            if self.operand2 == 0:
                return "Cannot modulo by 0"
            result = self.operand1 % self.operand2
        elif self.operator == '^':
            result = self.operand1 ** self.operand2
        else:
            return "Invalid operator"
        return result
        
    def getOperand1(self):
        return self.operand1
    
    def getOperand2(self):
        return self.operand2
    
    def getOperator(self):
        return self.operator