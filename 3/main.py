from output import Output

def main():
    filepath = 'input.txt'
    banks = get_banks(filepath)
    #print(banks) #debug print
    total_output = 0
    output = Output(0, 0)
    for bank in banks:
        digit_list = [int(d) for d in str(bank)]
        for digit in reversed(digit_list):
            output.compare(digit)
        total_output += output.total_value()
    return total_output


def get_banks(filepath):
    with open(filepath) as file:
        text = file.read()
    banks = list(map(int, text.split()))
    return banks

if __name__ == "__main__":
    print(main())