#task 1

with open('day2.txt', 'r') as file:
    data = file.readlines()

results = [list(map(int, line.split())) for line in data]

def is_safe_report(report):

    differences = [report[i + 1] - report[i] for i in range(len(report) - 1)]
    
    is_increasing = all(1 <= diff <= 3 for diff in differences)
    is_decreasing = all(-3 <= diff <= -1 for diff in differences)
    
    return is_increasing or is_decreasing

safeCount = sum( 1 for result in results if is_safe_report(result))

print(safeCount)

#task 2

def is_safe_report2(report):
    def is_safe(report):
        differences = [report[i + 1] - report[i] for i in range(len(report) - 1)]
        is_increasing = all(1 <= diff <= 3 for diff in differences)
        is_decreasing = all(-3 <= diff <= -1 for diff in differences)
        return is_increasing or is_decreasing

    # Check if the report is already safe
    if is_safe(report):
        return True

    # Check if removing one keeps it true
    for i in range(len(report)):
        modified_report = report[:i] + report[i + 1:]
        if is_safe(modified_report):
            return True

    return False

safeCount2 = sum( 1 for result in results if is_safe_report2(result))

print(safeCount2)