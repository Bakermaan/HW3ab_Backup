def get_user_input():
    # Prompting user for input for matrix A
    print("Enter the values for matrix A (4x4 matrix), row by row, separated by spaces:")
    A = []
    for i in range(4):
        row = input(f"Row {i + 1}: ").strip().split()
        A.append([float(num) for num in row])

    # Prompting user for input for vector b
    print("\nEnter the values for vector b, separated by spaces:")
    b = input("b: ").strip().split()
    b = [float(num) for num in b]

    # Validate the input sizes
    if len(A) != 4 or any(len(row) != 4 for row in A) or len(b) != 4:
        raise ValueError("Error: Please enter a 4x4 matrix for A and a vector of size 4 for b.")

    return A, b
