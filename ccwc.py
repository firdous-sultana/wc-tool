import argparse
import os

def count_bytes(file_path):
    try:
        total_bytes = 0
        with open(file_path, 'rb') as file:
            while chunk := file.read(8192):
                total_bytes += len(chunk)
            # content = file.read()
            # byte_count = len(content)  # NOTE: It is not a good practice to read all the content at once into the memory
        print(f"{total_bytes} {file_path}")
    except Exception as e:
        print(f"Error: Unable to read file '{file_path}'. {e}")


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("file", help="The file to count bytes for")
    args = parser.parse_args()
    count_bytes(args.file)

if __name__ == "__main__":
    main()
