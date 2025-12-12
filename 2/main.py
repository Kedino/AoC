

def main():
    filepath = 'input.txt'
    ranges = get_ranges(filepath)
    # print(ranges) # Debug print
    double_numbers = []
    for section in ranges:
        start, end = map(int, section.split("-"))
        for i in range(start, end):
            if is_double(i):
                double_numbers.append(i)
    total = sum(double_numbers)
    print(total)

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