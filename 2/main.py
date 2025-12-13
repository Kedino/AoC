

def main():
    filepath = 'input.txt'
    ranges = get_ranges(filepath)
    # print(ranges) # Debug print
    repeated_numbers = []
    for section in ranges:
        start, end = map(int, section.split("-"))
        for i in range(start, end):
            if is_repeated(i):
                repeated_numbers.append(i)
    total = sum(repeated_numbers)
    print(total)

def is_repeated(number):
    num_str = str(number)
    length = len(num_str)

    for size in range(1, length):
        if length % size != 0:
            continue
        
        value = num_str[:size]
        repeated = value * (length // size)
        if repeated == num_str:
            return True
    return False


def is_double(number):
    num_str = str(number)
    length = len(num_str)

    if length % 2 != 0:
        return False
    
    half = length // 2
    first_half = num_str[:half]
    second_half = num_str[half:]
    return first_half == second_half

def get_ranges(filepath):
    with open(filepath) as file:
        text = file.read()
    ranges = text.split(",")
    return ranges
    
if __name__ == "__main__":
    print(main())