# Aoc Day-2 Cube Conundrum
# Solution-1

with open("input.txt") as fin:
    data = fin.read().strip().split("\n")

result = 0

for line in data:
    game, parts = line.split(": ")
    game_id = int(game.split(" ")[1])

    passed = True
    for part in parts.split("; "):
        for cubes in part.split(", "):
            num, color = cubes.split(" ")
            num = int(num)

            if color == "red" and num > 12:
                passed = False
            if color == "blue" and num > 14:
                passed = False
            if color == "green" and num > 13:
                passed = False

            if not passed:
                break

        if not passed:
            break

    if passed:
        result += game_id

print(result)