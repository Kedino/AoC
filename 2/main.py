

def main():
    filepath = 'input.txt'
    ranges = get_ranges(filepath)
    print(ranges) # Debug print
    

def get_ranges(filepath):
    with open(filepath) as file:
        text = file.read()
    ranges = text.split(",")
    return ranges
    
if __name__ == "__main__":
    print(main())