import sys
import os
from datetime import datetime


def work_with_file(path: str) -> None:
    with open(path, "a") as file:
        file.write(datetime.now().strftime("%Y-%m-%d %H:%M:%S\n"))
        counter = 1
        while True:
            text = input("Enter content line: ")
            if text == "stop":
                file.writelines("\n")
                break
            file.write(f"{counter} {text}\n")
            counter += 1


def parse_arguments() -> tuple:
    directory_name = ""
    file_name = ""

    if "-d" in sys.argv:
        directory_name = (
            os.path.join(*sys.argv[sys.argv.index("-d") + 1:])
            if "-f" not in sys.argv
            else os.path.join(
                *sys.argv[sys.argv.index("-d") + 1: sys.argv.index("-f")]
            )
        )
        if not os.path.isdir(directory_name):
            os.makedirs(directory_name)

    if "-f" in sys.argv:
        file_name = sys.argv[sys.argv.index("-f") + 1]
        if not directory_name:
            directory_name = os.getcwd()

    return directory_name, file_name


def main() -> None:
    directory_name, file_name = parse_arguments()
    if file_name:
        path_name = os.path.join(directory_name, file_name)
        work_with_file(path_name)
    else:
        print("Filename not provided. "
              "Use the -f option to specify the filename.")


if __name__ == "__main__":
    main()
