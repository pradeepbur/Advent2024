import re

matched = {}
matched_mul = []
matched_do = []
matched_dont = []
total = 0
calculation = True

# file_path = "example.txt"
file_path = "input.txt"

regex = r"mul\(\d{1,3},\d{1,3}\)"
regexnum = r"\d{1,3}"
regexdo = r"do\(\)"
regexdont = r"don't\(\)"

concatinated_string = ""


def calc(sorted_values):
    global total
    global calculation
    for i in range(len(sorted_values)):
        if sorted_values[i][0] == "mul" and calculation:
            total += sorted_values[i][1] * sorted_values[i][2]
        elif sorted_values[i][0] == "mul" and not calculation:
            continue
        elif sorted_values[i][0] == "do":
            calculation = True
        elif sorted_values[i][0] == "dont":
            calculation = False


try:
    with open(file_path, "r") as file:
        lines = file.readlines()
        file.close()
        for i in range(len(lines)):
            concatinated_string += lines[i]
        matched_mul += re.finditer(regex, concatinated_string)
        matched_do += re.finditer(regexdo, concatinated_string)
        matched_dont += re.finditer(regexdont, concatinated_string)

        for match in matched_mul:
            nums = re.findall(regexnum, match.group())
            matched[match.start()] = ["mul", int(nums[0]), int(nums[1])]
        for match in matched_do:
            matched[match.start()] = ["do"]
        for match in matched_dont:
            matched[match.start()] = ["dont"]

        sorted_values = [value for key, value in sorted(matched.items())]
        calc(sorted_values)

        print(total)


except FileNotFoundError:
    print(f"The file was not found at {file_path}.")
