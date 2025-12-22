

def main():
    filepath = 'input.txt'
    rows = get_rows(filepath)
    total = 0
    for r in rows:
        row = r.split('')
        



def get_rows(filepath):
    with open(filepath, 'r') as file:
        return [line.strip() for line in file.readlines()]


if __name__ == "__main__":
    print(main())