# AoC/3/output.py

class Output:
    def __init__(self, first, second):
        self.tens_digit = int(first)
        self.ones_digit = int(second)
        self.highest_ones = int(second)

    def compare(self, new_digit):
        new_digit = int(new_digit)
        if not self.eval_tens(new_digit):
            self.eval_highest_ones(new_digit)
        else:
            self.eval_ones(self.highest_ones)

            
        
    def eval_tens(self, new_digit):
        if new_digit >= self.tens_digit:
            self.eval_highest_ones(self.tens_digit)
            self.tens_digit = new_digit
            return True
        return False
    
    def eval_ones(self, new_digit):
        if new_digit >= self.ones_digit:
            self.ones_digit = new_digit
            return True
        return False
    
    def eval_highest_ones(self, new_digit):
        if new_digit >= self.highest_ones:
            self.highest_ones = new_digit
            return True
        return False

    def total_value(self):
        return (int(self.tens_digit) * 10) + int(self.ones_digit)

    