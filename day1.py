# part 1

left_column = []
right_column = []

with open('day1.txt', 'r') as file:
    for line in file:
        left, right = map(int, line.split())
        left_column.append(left)
        right_column.append(right)


left_column.sort()
right_column.sort()

ans = 0

for i in range (len(left_column)):
    ans += abs(left_column[i] - right_column[i])

print(ans)

# part 2
from collections import Counter

ans2 = 0
countRight = Counter(right_column)

for i in left_column:
    if i in countRight:
        ans2 += (i * countRight[i])

print(ans2)