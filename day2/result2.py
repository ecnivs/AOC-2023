# Aoc Day-2 Cube Conundrum
# result-2

with open("input.txt") as fin:
    data = fin.read().strip().split("\n")

result = 0

for line in data:
    game, parts = line.split(": ")
    r, g, b = 0, 0, 0

    passed = True
    for part in parts.split("; "):
        for cubes in part.split(", "):
            num, color = cubes.split(" ")
            num = int(num)

            if color == "red":
                r = max(r, num)
            if color == "blue":
                b = max(b, num)
            if color == "green":
                g = max(g, num)

    if passed:
        result += r * b * g

print(result)