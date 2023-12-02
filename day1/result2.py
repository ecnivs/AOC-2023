# AOC Day-1 Trebuchet!?
# Solution-2

replacements = {
     "one" : "o1e",
     "two" : "t2o",
     "three" : "th3ee",
     "four" : "fo4r",
     "five" : "fi5e",
     "six" : "s6x",
     "seven" : "se7en",
     "eight" : "ei8ht",
     "nine" : "ni9e",
     "zero" : "ze0o"
}

input_file_path = 'input.txt'
processed_file_path = 'processed_file.txt'
total_sum = 0
refined_file_path = "refined_input.txt"

def strip_chars(input_file, output_file): # strips all chars except integers
    with open(input_file, 'r') as infile, open(output_file, 'w') as outfile:
        for line_number, line in enumerate(infile, start=1):
            stripped_line = ''.join(char for char in line if char.isdigit())
            if stripped_line:
                outfile.write(stripped_line + '\n')
            else:
                print(f"Warning: Line {line_number} in {input_file} contains no integers.")

def process(input_file, output_file, replacements):
    try:
        with open(input_file, 'r') as file:
            content = file.read()

            for old_word, new_word in replacements.items():
                content = content.replace(old_word, new_word)

        with open(output_file, 'w') as file:
            file.write(content)

    except FileNotFoundError:
        print(f"Error: File '{input_file}' not found.")
    except Exception as e:
        print(f"An error occurred: {str(e)}")

process(input_file_path, processed_file_path, replacements)
strip_chars(processed_file_path, refined_file_path)

with open(refined_file_path, 'r') as file:
    for line_number, line in enumerate(file, start=1):
        stripped_line = line.strip()

        if stripped_line:
            first_digit = str(stripped_line[0])
            last_digit = str(stripped_line[-1])
            digit_sum = first_digit + last_digit

            total_sum = total_sum + int(digit_sum)
print(total_sum)
