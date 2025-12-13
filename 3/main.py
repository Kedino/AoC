

def main():
    filepath = 'input.txt'
    banks = get_banks(filepath)
    print(banks) #debug print

def get_banks(filepath):
    with open(filepath) as file:
        text = file.read()
    banks = list(map(int, text.split()))
    return banks

if __name__ == "__main__":
    print(main())