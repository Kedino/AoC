class Output:
    def __init__(self, first, second):
        self.first_digit = first
        self.second_digit = second

    def compare(self, new_digit):
        replaced = None
        if new_digit >= self.first_digit:
            replaced = self.first_digit
            self.first_digit = new_digit
        if replaced:
            if replaced >= self.second_digit:
                self.second_digit = replaced
        
    def total_value(self):
        return self.first_digit * 10 + self.second_digit
        
        


    