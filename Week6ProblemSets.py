# lines.py
import sys

def main():
    if check_args():
        count = count_lines(sys.argv[1])
        print(count)
        sys.exit(0)
    else:
        sys.exit(1)

def check_args():
    code = 0
    if len(sys.argv) > 2:
        print("Too many command-line arguments")
        code = 1
    elif len(sys.argv) < 2:
        print("Too few command-line arguments")
        code = 1
    elif sys.argv[1][-3:] != ".py":
        print("Not a Python file")
        code = 1
    return True if code == 0 else False

def count_lines(file_path):
    count = 0
    try:
        with open(file_path) as file:
            for line in file:
                count += check_line(line)
    except FileNotFoundError:
        sys.exit(print("File does not exist"))
    return count

def check_line(line):
    if line.strip() != "" and line.lstrip(" ")[0] != "#":
        return 1
    else:
        return 0

if __name__ == "__main__":
    main()

# pizza.py
import tabulate
import sys

def main():
    if check_args(2, ".csv"):
        file = get_file_content(file_name = sys.argv[1])
        print(file)
        sys.exit(0)
    else:
        sys.exit(1)

def check_args(count, file_format):
    code = 0
    if len(sys.argv) > count:
        print("Too many command-line arguments")
        code = 1
    elif len(sys.argv) < count:
        print("Too few command-line arguments")
        code = 1
    elif sys.argv[1][-len(file_format):] != file_format:
        print(f"Not a {file_format[1:].upper()} file")
        code = 1
    return True if code == 0 else False

def get_file_content(file_name):
    file_content= []
    with open(file_name) as file:
        for line in file:
            file_content.append(line.rstrip().split(","))
    file_content = tabulate.tabulate(file_content, headers="firstrow", tablefmt="grid")
    return file_content

if __name__ == "__main__":
    main()

# scourgify.py
import sys, csv

def main():
    if check_args(3, ".csv"):
        format_file(sys.argv[1], sys.argv[2])
        sys.exit(0)
    else:
        sys.exit(1)


def format_file(source, destination):
    try:
        with open(source) as file:
            reader = csv.DictReader(file)
            with open(destination,"w") as file:
                writer = csv.DictWriter(file, fieldnames= ["first", "last", "house"] )
                writer.writeheader()
                for row in reader:
                    last, first = row["name"].split(",")
                    formattd_row = {"first": first.strip(), "last":  last.strip(), "house": row["house"] }
                    writer.writerow(formattd_row)
        sys.exit(0)
    except FileNotFoundError:
        print(f"Could not read {source}")
        sys.exit(1)
    except FileExistsError:
        print(f"Could not write to {destination}")
        sys.exit(1)



def check_args(count, file_format):
    code = 0
    if len(sys.argv) > count:
        print("Too many command-line arguments")
        code = 1
    elif len(sys.argv) < count:
        print("Too few command-line arguments")
        code = 1
    elif sys.argv[1][-len(file_format):] != file_format or sys.argv[2][-len(file_format):] != file_format:
        print(f"Both files should be {file_format[1:].upper()}")
        code = 1
    return True if code == 0 else False

if __name__ ==  "__main__":
    main()


# shirt.py
import sys
from PIL import Image, ImageOps

def main():
    if check_args(3):
        transform_image()
        sys.exit(0)
    else:
        sys.exit(1)
      

def transform_image(source = sys.argv[1], destination = sys.argv[2]):
   with Image.open(source) as img:
       shirt = Image.open("shirt.png")
       new_image = ImageOps.fit(img, size = shirt.size, centering = (0.5,0.5))
       new_image.paste(shirt,shirt)
       new_image.save(destination)
       return


def check_args(count, file_formats=[".jpeg",".png", ".jpg"]):
    code = 0
    if len(sys.argv) > count:
        print("Too many command-line arguments")
        return False
    elif len(sys.argv) < count:
        print("Too few command-line arguments")
        return False
    frmt = ""
    for format in file_formats:
        if sys.argv[1][-len(format):] == format:
            frmt = format
            break
    if frmt == "":
        print("Invalid input")
        code = 1
    elif sys.argv[1][-len(frmt):] != sys.argv[2][-len(frmt):] :
        print("Input and output have different extensiosn")
        code = 1
    return code == 0

if __name__ == "__main__":
    main()
