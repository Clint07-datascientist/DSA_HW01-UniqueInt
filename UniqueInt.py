import os

def unique_integers(input_file_path, output_file_path):
    # Read integers from file and add to a set for uniqueness
    unique_numbers = set()
    with open(input_file_path, 'r') as file:
        for line in file:
            line = line.strip()
            if line.isdigit():  # Check if the line is a digit
                unique_numbers.add(int(line))

    # Sort the unique integers
    sorted_numbers = sorted(unique_numbers)

    # Write the sorted unique integers to the output file
    with open(output_file_path, 'w') as file:
        for number in sorted_numbers:
            file.write(f"{number}\n")

def main():
    input_dir = "../sample_inputs/"
    output_dir = "../sample_results/"
    input_files = [
        "sample_01.txt", "sample_02.txt", "sample_03.txt", "sample_04.txt",
        "small_sample_input_01.txt", "small_sample_input_02.txt", "small_sample_input_03.txt", "small_sample_input_04.txt"
    ]

    # Process each file
    for input_file in input_files:
        input_file_path = os.path.join(input_dir, input_file)
        output_file_path = os.path.join(output_dir, f"{input_file}_result.txt")
        unique_integers(input_file_path, output_file_path)
        print(f"Processed {input_file} -> {output_file_path}")

if __name__ == "__main__":
    main()

