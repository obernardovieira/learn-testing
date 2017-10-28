class Calculator(object):
    
    def __init__(self):
        self.history = []

    def sum(self, x, y):
        result = x + y
        self.history += [[x, '+', y]]
        return result

    def sub(self, x, y):
        result = x - y
        self.history += [[x, '-', y]]
        return result

    def mul(self, x, y):
        result = x * y
        self.history += [[x, '*', y]]
        return result

    def div(self, x, y):
        result = x / y
        self.history += [[x, '/', y]]
        return result

    def get_history(self):
        return self.history

    def clear_history(self):
        self.history = []