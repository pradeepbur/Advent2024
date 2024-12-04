total = 0
input = []
# file_path = "example.txt"
file_path = "input.txt"


def parse(input):
    global total
    for i in range(len(input)):
        for j in range(len(input[i])):
            if i <= (len(input) - 3) and j <= (len(input[i]) - 3):
                if (
                    input[i][j] == "M"
                    and input[i + 1][j + 1] == "A"
                    and input[i + 2][j + 2] == "S"
                ):
                    if input[i + 2][j] == "M" and input[i][j + 2] == "S":
                        total += 1
                        print({i, j})
                    elif input[i + 2][j] == "S" and input[i][j + 2] == "M":
                        total += 1
                        print({i, j})
                if (
                    input[i][j] == "S"
                    and input[i + 1][j + 1] == "A"
                    and input[i + 2][j + 2] == "M"
                ):
                    if input[i + 2][j] == "M" and input[i][j + 2] == "S":
                        total += 1
                        print({i, j})
                    elif input[i + 2][j] == "S" and input[i][j + 2] == "M":
                        total += 1
                        print({i, j})


try:
    with open(file_path, "r") as file:
        lines = file.readlines()
        file.close()
        for i in range(len(lines)):
            char = [char for char in lines[i].strip()]
            input.append(char)
        parse(input)
        print(total)

except FileNotFoundError:
    print(f"The file was not found at {file_path}.")
