# Matrix Determinant Calculator

## Overview
This Python script calculates the determinant of two 3x3 matrices using a manual formula (without NumPy). It also prints the matrices in a structured format and provides insights into whether they are singular (non-invertible) or not.

## Features
- ✅ Prints matrices in a visually appealing format.
- ✨ Calculates the determinant of two 3x3 matrices.
- ⚠️ Checks if a matrix is singular (det = 0) and warns the user.
- 🎉 Displays a fun message about the invertibility of the matrices.

## Usage
1. Define two 3x3 matrices (`matrix_a` and `matrix_b`).
2. Run the script to print the matrices and their determinants.
3. Get insights into their invertibility status.

## Example Output
```
🟢 Matrix A:
    [1, 2, 3]
    [4, 5, 6]
    [7, 8, 9]

✨ The determinant of matrix A is: 0
⚠️ Matrix A is singular (det = 0) and not invertible!
```

## How It Works
The determinant of a 3x3 matrix is calculated using the standard formula:
```
det(A) = a(ei − fh) − b(di − fg) + c(dh − eg)
```
Where the matrix is:
```
| a  b  c |
| d  e  f |
| g  h  i |
```

## Dependencies
- No external libraries required (pure Python implementation).

## Future Enhancements
- Add support for larger matrices.
- Implement an option for user input matrices.
- Optimize the determinant calculation for efficiency.

Enjoy coding! 🚀

