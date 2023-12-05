# Aoc Day-3 Gear Ratios
# Solution-1

with open("input.txt") as file:
    data = file.read()
    lines = data.strip().split("\n")

n = len(lines)
m = len(lines[0])
solution = 0

def is_symbol(i, j):
    if not (0 <= i < n and 0 <= j < m):
        return False

    return lines[i][j] != "." and not lines[i][j].isdigit()

for i, line in enumerate(lines):
    _var = 0

    j = 0

    while j < m:
        _var = j
        num = ""
        while j < m and line[j].isdigit():
            num += line[j]
            j += 1

        if num == "":
            j += 1
            continue

        num = int(num)

        if is_symbol(i, _var-1) or is_symbol(i, j):
            solution += num
            continue

        for k in range(_var-1, j+1):
            if is_symbol(i-1, k) or is_symbol(i+1, k):
                solution += num
                break

print(solution)