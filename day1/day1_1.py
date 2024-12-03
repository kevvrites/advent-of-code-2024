def sort_columns(input_file, output_file=None):
    # Read the numbers from the file
    with open(input_file, 'r') as f:
        lines = f.readlines()
    
    # Parse the numbers into two separate lists
    col1 = []
    col2 = []
    for line in lines:
        num1, num2 = map(int, line.strip().split())
        col1.append(num1)
        col2.append(num2)
    
    # Sort each column independently
    sorted_col1 = sorted(col1)
    sorted_col2 = sorted(col2)
    
    # Calculate differences
    differences = []
    for num1, num2 in zip(sorted_col1, sorted_col2):
        diff = abs(num1 - num2)  # Using absolute difference
        differences.append(diff)
    
    return sorted_col1, sorted_col2, differences  # Now returning three values

if __name__ == "__main__":
    input_file = "day1input.txt"
    output_file = "sorted_output.txt"
    
    sorted_col1, sorted_col2, differences = sort_columns(input_file, output_file)  # Unpacking three values
    
    # Print the sorted columns and differences to console
    print("\nResults:")
    print("Col1  Col2  Diff")
    print("-" * 20)
    for num1, num2, diff in zip(sorted_col1, sorted_col2, differences):
        print(f"{num1:4d} {num2:4d} {diff:4d}")
    
    print("\nSum of all differences:", sum(differences))
