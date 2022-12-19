# 0x00-pascal_triangle

To implement the function pascal_triangle(n), we can follow these steps:

Define the function pascal_triangle(n). Inside it, define a variable result initialized to an empty list.
Implement a loop that iterates n times. In each iteration, create a new row of the triangle as a list of integers, starting with the number 1.
For rows 1 and 2, append the number 1 to the end of the row.
For rows greater than 2, compute the values of the remaining elements in the row using the formula result[i][j] = result[i-1][j-1] + result[i-1][j]. Append this value to the end of the row.
After the loop, return result.