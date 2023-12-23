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

def solve(lines: list[str]) -> int:
    cp = [1 for _ in lines]
    for current_index, line in enumerate(lines):
        nums = parse_line(line)
        score = num_of_intersections(*nums)
        for i in range(score):
            new_index = current_index + 1 + i
            cp[new_index] += cp[current_index]

    return sum(cp)


def num_of_intersections(win_nums: list[int],
                            c_num: list[int],
                            ) -> int:
    intersection = set(win_nums).intersection(set(c_num))
    return len(intersection)


def main():
    lines = read_input()
    result = solve(lines)
    print(result)


if __name__ == "__main__":
    main()