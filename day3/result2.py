with open("input.txt") as file:
    data = file.read()
    lines = data.strip().split("\n")

n = len(lines)
m = len(lines[0])
solution = 0

num2 = [[[] for _ in range(m)] for _ in range(n)]

def is_symbol(i, j, num):
    if not (0 <= i < n and 0 <= j < m):
        return False

    if lines[i][j] == "*":
        num2[i][j].append(num)
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

        is_symbol(i, _var-1, num) or is_symbol(i, j, num)

        for k in range(_var-1, j+1):
            is_symbol(i-1, k, num) or is_symbol(i+1, k, num)

for i in range(n):
    for j in range(m):
        nums = num2[i][j]
        if lines[i][j] == "*" and len(nums) == 2:
            solution += nums[0] * nums[1]

print(solution)