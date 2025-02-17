def print_matrix(matrix, name):
    print(f"\n🟢 Matrix {name}:")
    for row in matrix:
        print("   ", row)

def calculate_determinant(matrix, name):
    det = (matrix[0][0] * (matrix[1][1] * matrix[2][2] - matrix[1][2] * matrix[2][1])
           - matrix[0][1] * (matrix[1][0] * matrix[2][2] - matrix[1][2] * matrix[2][0])
           + matrix[0][2] * (matrix[1][0] * matrix[2][1] - matrix[1][1] * matrix[2][0]))
    print(f"\n✨ The determinant of matrix {name} is: {det}\n")
    return det

# Define matrices
matrix_a = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

matrix_b = [
    [9, 8, 7],
    [6, 5, 4],
    [3, 2, 1]
]

# Print matrices
print_matrix(matrix_a, 'A')
print_matrix(matrix_b, 'B')

# Calculate and print determinants
det_a = calculate_determinant(matrix_a, 'A')
det_b = calculate_determinant(matrix_b, 'B')

# Fun fact 🤓
if det_a == 0 and det_b == 0:
    print("❌ Both matrices are singular (det = 0), so they are not invertible!")
elif det_a == 0:
    print("⚠️ Matrix A is singular (det = 0) and not invertible!")
elif det_b == 0:
    print("⚠️ Matrix B is singular (det = 0) and not invertible!")
else:
    print("✅ Both matrices are invertible! 🎉")
