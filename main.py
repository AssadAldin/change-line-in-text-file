def replace_line_in_file(file_path, line_number, new_content):
    """
    Replace a specific line in a text file.
    :param file_path: Path to the text file
    :param line_number: Line number to replace (1-based index)
    :param new_content: New content for the line
    """
    try:
        with open(file_path, 'r') as file:
            lines = file.readlines()
        
        if 1 <= line_number <= len(lines):
            lines[line_number - 1] = new_content + '\n'  # Adjust for zero-based index
        
            with open(file_path, 'w') as file:
                file.writelines(lines)
            print("Line updated successfully.")
        else:
            print("Error: Line number out of range.")
    except FileNotFoundError:
        print("Error: File not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Example usage
file_path = "sample.txt"  # Replace with your file path
line_number = 3  # Replace the 3rd line
new_content = "This is the new line content."
replace_line_in_file(file_path, line_number, new_content)
