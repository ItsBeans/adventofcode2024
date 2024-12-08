import re

# task 1

def calculate(file_path):
    with open(file_path, 'r') as file:
        data = file.read().replace("\n", "")
    
    # regex for the pattern we looking for
    pattern = r"mul\((\d{1,3}),(\d{1,3})\)"
    
    matches = re.findall(pattern, data)
    total = 0
    
    for x, y in matches:
        total += int(x) * int(y)
    
    return total

file_path = 'day3.txt'
result = calculate(file_path)
print("Sum of all valid multiplications:", result)


# task 2

def calculate_sum_with_conditions(file_path):
    with open(file_path, 'r') as file:
        data = file.read().replace("\n", "")

    # regex for the pattern we looking for
    pattern = r"(do\(\))|(don't\(\))|mul\((\d{1,3}),(\d{1,3})\)"
    
    mul_enabled = True
    total = 0

    # Scan the string and process instructions in sequence
    for match in re.finditer(pattern, data):
        if match.group(1):  # do()
            mul_enabled = True
        elif match.group(2):  # don't()
            mul_enabled = False
        elif mul_enabled and match.group(3) and match.group(4):  # mul(X,Y)
            x, y = int(match.group(3)), int(match.group(4))
            total += x * y

    return total

result = calculate_sum_with_conditions(file_path)
print("Sum of all enabled multiplications:", result)