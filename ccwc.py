import argparse
import os

def count_bytes(file_path):
    try:
        return os.path.getsize(file_path)
    except OSError as e:
        print(f"Error: {e}")
        return None

def count_lines(file_path):
    try:
        line_counter = 0
        with open(file_path, 'rb') as file:
            for _ in file:
                line_counter += 1
            return line_counter
    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
        return None


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("-c", "--bytes", action="store_true", help="print the byte counts")
    parser.add_argument("-l", "--lines", action="store_true", help="print the newline counts")
    parser.add_argument("file", help="The file to count bytes for")
    args = parser.parse_args()

    if args.bytes:
        byte_count = count_bytes(args.file)
        print(f"{byte_count} {args.file}")
    elif args.lines:
        line_count = count_lines(args.file)
        print(f"{line_count} {args.file}")
    else:
        print("Please pass an option!")

if __name__ == "__main__":
    main()
