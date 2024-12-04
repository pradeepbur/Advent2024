total = 0
input = []
# file_path = "example.txt"
file_path = "input.txt"


def parse(input):
    global total
    for i in range(len(input)):
        for j in range(len(input[i])):
            if (
                j <= (len(input[i]) - 4)
                and input[i][j] == "X"
                and input[i][j + 1] == "M"
                and input[i][j + 2] == "A"
                and input[i][j + 3] == "S"
            ):
                print({i, j})
                total += 1
            if (
                j <= (len(input[i]) - 4)
                and input[i][j] == "S"
                and input[i][j + 1] == "A"
                and input[i][j + 2] == "M"
                and input[i][j + 3] == "X"
            ):
                print({i, j})
                total += 1
            if (
                i <= (len(input) - 4)
                and input[i][j] == "X"
                and input[i + 1][j] == "M"
                and input[i + 2][j] == "A"
                and input[i + 3][j] == "S"
            ):
                print({i, j})
                total += 1
            if (
                i <= (len(input) - 4)
                and input[i][j] == "S"
                and input[i + 1][j] == "A"
                and input[i + 2][j] == "M"
                and input[i + 3][j] == "X"
            ):
                print({i, j})
                total += 1
            if (
                j <= (len(input[i]) - 4)
                and i <= (len(input) - 4)
                and input[i][j] == "X"
                and input[i + 1][j + 1] == "M"
                and input[i + 2][j + 2] == "A"
                and input[i + 3][j + 3] == "S"
            ):
                print({i, j})
                total += 1
            if (
                j <= (len(input[i]) - 4)
                and i <= (len(input) - 4)
                and input[i][j] == "S"
                and input[i + 1][j + 1] == "A"
                and input[i + 2][j + 2] == "M"
                and input[i + 3][j + 3] == "X"
            ):
                print({i, j})
                total += 1
            if (
                i <= (len(input) - 4)
                and j >= 3
                and input[i][j] == "X"
                and input[i + 1][j - 1] == "M"
                and input[i + 2][j - 2] == "A"
                and input[i + 3][j - 3] == "S"
            ):
                print({i, j})
                total += 1
            if (
                i <= (len(input) - 4)
                and j >= 3
                and input[i][j] == "S"
                and input[i + 1][j - 1] == "A"
                and input[i + 2][j - 2] == "M"
                and input[i + 3][j - 3] == "X"
            ):
                print({i, j})
                total += 1


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
