safe_reports = []
# file_path = "part2-example.txt"
file_path = "part1-input.txt"


def is_safe(report):
    if report[0] - report[-1] < 0:
        for i in range(1, len(report)):
            if report[i] - report[i - 1] >= 1 and report[i] - report[i - 1] <= 3:
                if i == len(report) - 1:
                    return True
                else:
                    continue
            else:
                return False
    elif report[0] - report[-1] > 0:
        for i in range(1, len(report)):
            if report[i] - report[i - 1] <= -1 and report[i] - report[i - 1] >= -3:
                if i == len(report) - 1:
                    return True
                else:
                    continue
            else:
                return False
    else:
        return False


def retryreport(report):
    for i in range(len(report)):
        modified_report = report[:i] + report[i + 1 :]
        if is_safe(modified_report):
            safe_reports.append(modified_report)
            break
        else:
            continue


try:
    with open(file_path, "r") as file:
        lines = file.readlines()
        file.close()
        for i in range(len(lines)):
            report = lines[i].strip().split()
            report = [int(s) for s in report]

            if is_safe(report):
                safe_reports.append(report)
            else:
                retryreport(report)

    print(f"The total safe reports are {len(safe_reports)}.")

except FileNotFoundError:
    print(f"The file was not found at {file_path}.")
