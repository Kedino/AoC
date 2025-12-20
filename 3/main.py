# AoC/3/main.py

from output import Output

def main():
    filepath = 'input.txt'
    banks = get_banks(filepath)
    #print(banks) #debug print
    total_output = 0
    
    for bank in banks:
        output = Output(bank[-2], bank[-1])  # Initialize with reversed digits
        digit_list = [d for d in str(bank)]
        for digit in reversed(digit_list[:-2]):
            output.compare(digit)
        value = output.total_value()
        print(bank, "->", output.tens_digit, output.ones_digit, "=", value) 
        total_output += value
    return total_output


def get_banks(filepath):
    with open(filepath) as file:
        text = file.read()
    banks = list(map(str, text.split()))
    return banks

if __name__ == "__main__":
    print(main())