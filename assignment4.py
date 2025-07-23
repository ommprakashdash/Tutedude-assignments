def read_file(filename):
    try:
        with open(filename, 'r') as file:
            print(f"Contents of '{filename}':")
            for line in file:
                print(line.strip())
    except FileNotFoundError:
        print(f"Error: The file '{filename}' does not exist.")

# Example usage
read_file('sample.txt')

def write_and_append_file(filename):
    try:
        # Step 1: Write user input to the file
        data = input("Enter some data to write to the file: ")
        with open(filename, 'w') as file:
            file.write(data + '\n')

        # Step 2: Append more data to the file
        more_data = input("Enter more data to append: ")
        with open(filename, 'a') as file:
            file.write(more_data + '\n')

        # Step 3: Read and display final contents
        print(f"\nFinal contents of '{filename}':")
        with open(filename, 'r') as file:
            for line in file:
                print(line.strip())

    except Exception as e:
        print("An error occurred:", e)

# Example usage
write_and_append_file('output.txt')
