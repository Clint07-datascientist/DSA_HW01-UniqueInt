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
