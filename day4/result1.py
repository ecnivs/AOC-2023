# AOC Day-4 Scratchcards
# result-1

def read_input() -> list[str]:
    with open("input.txt") as f:
        lines = f.read().splitlines()
    return lines

def parse_line(line: str) -> tuple[list[int], list[int]]:
    c_name, nums = line.split(": ")
    win_num_str, c_num = nums.split(" | ")
    win_nums = [int(n) for n in win_num_str.split()]
    c_num = [int(n) for n in c_num.split()]
    return win_nums, c_num

def score(win_nums: list[int], c_num: list[int]) -> int:
    intersection = set(win_nums).intersection(set(c_num))
    if len(intersection) == 0:
        return 0
    else:
        return 2 ** (len(intersection) - 1)

def solve(lines: list[str]) -> int:
    result = 0
    for line in lines:
        win_nums, c_num = parse_line(line)
        card_score = score(win_nums, c_num)
        result += card_score
    return result

def main():
    lines = read_input()
    result = solve(lines)
    print(result)

if __name__ == "__main__":
    main()