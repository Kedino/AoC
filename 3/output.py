class Output:
    def __init__(self, first, second):
        self.first_digit = int(first)
        self.second_digit = int(second)
        self.highest_skipped = 0

    def compare(self, new_digit):
        new_digit = int(new_digit)
        replaced = None
        if new_digit >= self.first_digit:
            replaced = self.first_digit
            self.first_digit = new_digit
        elif new_digit >= self.highest_skipped:
            self.highest_skipped = new_digit
        if replaced:
            if replaced >= self.second_digit:
                self.second_digit = replaced
        if self.highest_skipped:
            if self.highest_skipped >= self.second_digit:
                self.second_digit = self.highest_skipped
                self.highest_skipped = 0
        
        
    def total_value(self):
        return (self.first_digit * 10) + self.second_digit
        
        


    