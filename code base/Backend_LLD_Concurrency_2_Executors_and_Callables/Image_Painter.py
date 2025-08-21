'''
Image Painter
Implement a Java program that simulates image re-painting using 4 threads. The algorithm for painting is described as under but your task is given an
image, divide the image into 4 quadrants and let each thread paint one quadrant of the image. The concurrent execution ensures image is painted
efficiently.

Problem Statement:
You are provided a function paintImage. This function is designed to paint a square image, represented as a 2D integer array, where each integer
represents a color. The goal is to paint the image in such a way that each quadrant of the image has a different color. The painting process for each
 quadrant should be performed concurrently using multiple threads.

Tasks:
Implement the paintImage function
Divide the given image into four quadrants.
Paint each quadrant with a different color.
The base color will be provided as an input to the painting method, and each quadrant should use a variation of this base color.
For first quadrant the color should be same as the given base color.
For second quadrant the color should be equal to 2*base color.
For third quadrant the color should be equal to 3*base color.
For fourth quadrant the color should be equal to 4*base color
Instructions
The image is represented as a 2D integer array.
Use a fixed thread pool size of 4 threads in your ExecutorService.
Handle any potential exceptions that may arise during the execution.
Implement the paintImage function and the constructor in the ImagePainter class.
Use Java's ExecutorService to execute the painting of each quadrant in a separate thread.
Ensure that the program waits for all quadrants to be fully painted before proceeding.
Properly shutdown your ExecutorService after the painting is completed to avoid any resource leaks.
'''

from concurrent.futures import ThreadPoolExecutor
from typing import List

from pandas import interval_range


class ImagePainter:

    def __init__(self, image:List[List[int]], base_color: int):
        self.base_color = base_color
        self.image = image



    def paint_quadrant(self,start_row: int, end_row: int, start_col:int, end_col:int, color:int):
        for row in range(start_row, end_row):
            for col in range(start_col, end_col):
                self.image[row][col] = color

    def paintImage(self):

        # divide the image into four quadrants
        n = len(self.image)
        mid = n // 2
        quadrants = [
            (0, mid, 0, mid),
            (0, mid, mid, n),
            (mid, n, 0, mid),
            (mid, n, mid, n)
        ]

        with ThreadPoolExecutor(max_workers=4) as executor:
            try:
                futures = [
                    executor.submit(self.paint_quadrant, *quadrants[0], self.base_color),
                    executor.submit(self.paint_quadrant, *quadrants[1], 2 * self.base_color),
                    executor.submit(self.paint_quadrant, *quadrants[2], 3 * self.base_color),
                    executor.submit(self.paint_quadrant, *quadrants[3], 4 * self.base_color)
                ]

                try:
                    for future in futures:
                        future.result()
                except Exception as e:
                    print(f"Error occurred while painting quadrant: {e}")

            except Exception as e:
                print("executor error!!!",{e})




if __name__ == '__main__':

    image = [[0 for _ in range(5)] for _ in range(5)]
    base_color = 1  # Base color for the image
    painter = ImagePainter(image, base_color)
    painter.paintImage()
    # Print the painted image
    for row in painter.image:
        print(row)

