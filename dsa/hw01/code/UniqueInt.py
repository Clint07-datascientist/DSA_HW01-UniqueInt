import os
import pandas as pd

class UniqueInt:
    @staticmethod
    def process_file(input_file_path, output_file_path):
        # Read the input file into a Pandas DataFrame
        df = pd.read_csv(input_file_path, header=None, names=["number"], dtype=int)

        # Remove duplicates and sort the unique integers
        unique_numbers = df["number"].drop_duplicates().sort_values()

        # Write the sorted unique integers to the output file
        unique_numbers.to_csv(output_file_path, index=False, header=False)

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
        UniqueInt.process_file(input_file_path, output_file_path)
        print(f"Processed {input_file} -> {output_file_path}")

if __name__ == "__main__":
    main()
