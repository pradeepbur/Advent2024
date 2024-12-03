safe = 0
file_path = "part1-example.txt"
# file_path = "part1-input.txt"
try:
    with open(file_path, "r") as file:
        lines = file.readlines()
        file.close()
        lenght = len(lines)
        for report in range(len(lines)):
            compare_list = lines[report].strip().split()

            compare_list = [int(s) for s in compare_list]

            for i in range(1, len(compare_list)):
                if compare_list[0] - compare_list[-1] < 0:
                    if (
                        compare_list[i] - compare_list[i - 1] >= 1
                        and compare_list[i] - compare_list[i - 1] <= 3
                    ):
                        if i == len(compare_list) - 1:
                            safe += 1
                    else:
                        break
                elif compare_list[0] - compare_list[-1] > 0:
                    if (
                        compare_list[i] - compare_list[i - 1] <= -1
                        and compare_list[i] - compare_list[i - 1] >= -3
                    ):
                        if i == len(compare_list) - 1:
                            safe += 1
                    else:
                        break
                else:
                    break

    print(f"The total safe reports are {safe}.")

except FileNotFoundError:
    print(f"The file was not found at {file_path}.")
