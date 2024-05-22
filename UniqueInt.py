import os

class UniqueInt:
    @staticmethod
    def process_file(input_file_path, output_file_path):
        unique_integers = set()
        
        with open(input_file_path, 'r') as file:
            for line in file:
                line = line.strip()  # Remove any surrounding whitespace
                if line:  # Skip empty lines
                    try:
                        number = int(line)
                        unique_integers.add(number)
                    except ValueError:
                        # Line is not an integer, skip it
                        pass
        
        sorted_unique_integers = sorted(unique_integers)
        
        with open(output_file_path, 'w') as file:
            for number in sorted_unique_integers:
                file.write(f"{number}\n")

def main():
    input_dir = "../sample_inputs/"
    output_dir = "../sample_results/"
    
    input_files = [
        "sample_01.txt", "sample_02.txt", "sample_03.txt", "sample_04.txt",
        "small_sample_input_01.txt", "small_sample_input_02.txt", "small_sample_input_03.txt", "small_sample_input_04.txt"
    ]
    
    for input_file in input_files:
        input_file_path = os.path.join(input_dir, input_file)
        output_file_path = os.path.join(output_dir, f"{input_file}_result.txt")
        UniqueInt.process_file(input_file_path, output_file_path)
        print(f"Processed {input_file} -> {output_file_path}")

if __name__ == "__main__":
    main()
