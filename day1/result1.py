# AOC Day-1 Trebuchet!?

def strip_chars(input_file, output_file): # strips all chars except integers
    with open(input_file, 'r') as infile, open(output_file, 'w') as outfile:
        for line_number, line in enumerate(infile, start=1):
            stripped_line = ''.join(char for char in line if char.isdigit())
            if stripped_line:
                outfile.write(stripped_line + '\n')
            else:
                print(f"Warning: Line {line_number} in {input_file} contains no integers.")

input_file_path = 'input.txt'
total_sum = 0

refined_file_path = "refined_input.txt"
with open(refined_file_path, 'r') as file:
    for line_number, line in enumerate(file, start=1):
        stripped_line = line.strip()

        if stripped_line:
            first_digit = str(stripped_line[0])
            last_digit = str(stripped_line[-1])
            digit_sum = first_digit + last_digit

            total_sum = total_sum + int(digit_sum)
print(total_sum)
