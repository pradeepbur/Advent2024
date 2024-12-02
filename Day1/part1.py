first_list = []
second_list = []
lenght = 0
file_path = "part1-input.txt"
try:
    with open(file_path, "r") as file:
        lines = file.readlines()
        file.close()
        lenght = len(lines)
        for i in range(len(lines)):
            line = lines[i].strip().split()
            first_number = int(line[0])
            second_number = int(line[1])
            first_list.append(first_number)
            second_list.append(second_number)
    first_list.sort()
    second_list.sort()
    total = 0
    for i in range(lenght):
        distance = first_list[i] - second_list[i]
        total += abs(distance)
    print(f"The total distance is {total}.")

except FileNotFoundError:
    print(f"The file was not found at {file_path}.")
