import re

matches = []
total = 0

# file_path = "example.txt"
file_path = "input.txt"

regex = r"mul\(\d{1,3},\d{1,3}\)"
regexnum = r"\d{1,3}"

try:
    with open(file_path, "r") as file:
        lines = file.readlines()
        file.close()
        for i in range(len(lines)):
            matches += re.findall(regex, lines[i])
        for match in matches:
            nums = re.findall(regexnum, match)
            total += int(nums[0]) * int(nums[1])
        print(f"The total is {total}.")


except FileNotFoundError:
    print(f"The file was not found at {file_path}.")
