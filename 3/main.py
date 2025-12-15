

def main():
    filepath = 'input.txt'
    banks = get_banks(filepath)
    #print(banks) #debug print

    results = []
    for bank in banks:
        bank_str = str(bank)
        length = len(bank_str)
        n = 9
        highest = []
        while n > 0:
            if n in bank_str:
                if n == bank_str[length]:
                    break

        n -= 1

def get_banks(filepath):
    with open(filepath) as file:
        text = file.read()
    banks = list(map(int, text.split()))
    return banks

if __name__ == "__main__":
    print(main())