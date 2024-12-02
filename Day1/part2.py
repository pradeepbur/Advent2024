first_list = []
second_list_dict = {}
lenght = 0
file_path = "part2-input.txt"
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
            if second_number not in second_list_dict:
                second_list_dict[second_number] = 1
            else:
                second_list_dict[second_number] += 1
    total = 0
    for i in range(len(first_list)):
        number = first_list[i]
        if number not in second_list_dict:
            total = total
        else:
            total = total + number * second_list_dict[number]

    print(f"The total is {total}.")


except FileNotFoundError:
    print(f"The file was not found at {file_path}.")
