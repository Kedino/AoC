# AoC/3/main.py

from output import Output

def main():
    filepath = 'input.txt'
    banks = get_banks(filepath)
    #print(banks) #debug print
    total_output = 0
    k = 12
    
    #for bank in banks:
    #    output = Output(bank[-2], bank[-1])  # Initialize with reversed digits
    #    digit_list = [d for d in str(bank)]
    #    for digit in reversed(digit_list[:-2]):
    #        output.compare(digit)
    #    value = output.total_value()
    #    print(bank, "->", output.tens_digit, output.ones_digit, "=", value) 
    #    total_output += value
    #return total_output
    for bank in banks:
        best_value = best_k_digits(bank, k)
        #print(bank, "->", best_value) #debug print
        total_output += best_value
    return total_output

def best_k_digits(num_str: str, k: int) -> int:
    to_remove = len(num_str) - k
    stack = []

    for d in num_str:
        while to_remove > 0 and stack and stack[-1] < d:
            stack.pop()
            to_remove -= 1
        stack.append(d)

    if to_remove > 0:
        stack = stack[:-to_remove]

    return int(''.join(stack[:k]))


def get_banks(filepath):
    with open(filepath) as file:
        text = file.read()
    banks = list(map(str, text.split()))
    return banks

if __name__ == "__main__":
    print(main())