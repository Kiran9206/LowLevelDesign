'''
Parallel Matrix Painting
Problem Statement
You are tasked with creating a Python program that can divide a matrix into quadrants and paint each quadrant with a different color using parallel
processing. The program should leverage the concurrent.futures module to achieve parallelism and improve performance.

Requirements
The program should include the following components:

paint_quadrant function:
Takes a matrix, start and end row indices, start and end column indices, and a color as input.
Paints the specified quadrant of the matrix with the given color.
divideandpaint function:
Takes a matrix and a list of colors as input.
Divides the matrix into four quadrants (top-left, top-right, bottom-left, bottom-right).
Utilizes the concurrent.futures.ThreadPoolExecutor to create four separate threads.
Each thread calls the paint_quadrant function with the corresponding quadrant and color.
Waits for all threads to complete before returning.
Example usage:
Creates a sample 4x4 matrix.
Calls the divideandpaint function with the matrix and a list of four colors.
Prints the painted matrix.
Instructions
Implement the paint_quadrant function according to the specified requirements.
Implement the divideandpaint function, which creates a thread pool executor and submits tasks to paint each quadrant in parallel.
'''


def paint_quadrant(matrix: list, start_row: int, end_row:int, start_col: int, end_col: int, color:str):
    for row in range(start_row, end_row):
        for col in range(start_col, end_col):
            matrix[row][col] = color


def divide_and_paint(matrix:list, colors:list):

    mid_row = len(matrix) // 2
    mid_col = len(matrix[0]) // 2

    from concurrent.futures import ThreadPoolExecutor
    with ThreadPoolExecutor(max_workers=4) as executor:
        futures = [executor.submit(paint_quadrant, matrix, 0, mid_row, 0, mid_col, colors[0]),
                   executor.submit(paint_quadrant,matrix, 0, mid_row, mid_col, len(matrix[0]), colors[1]),
                   executor.submit(paint_quadrant, matrix, mid_row, len(matrix), 0, mid_col, colors[2]),
                   executor.submit(paint_quadrant, matrix, mid_row, len(matrix), mid_col, len(matrix[0]), colors[3])]

        for future in futures:
            future.result()

if __name__ == '__main__':
    matrix = [[0 for _ in range(4)] for _ in range(4)]
    colors = ['R', 'G', 'B', 'Y']  # Red, Green, Blue, Yellow
    divide_and_paint(matrix, colors)
    # Print the painted matrix
    for row in matrix:
        print(row)

