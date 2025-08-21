'''
Parallel Binary Tree Size Calculation
Problem Statement
You are tasked with creating a Python program that can calculate the size (number of nodes) of a binary tree using parallel processing.
The program should leverage the concurrent.futures module and threading to achieve parallelism and improve performance.

Requirements
The program should include the following components:

Node class:
Represents a node in the binary tree.
Has attributes: data (integer value), left (reference to the left child), and right (reference to the right child).
TreeSizeCalculator class:
Takes the root node of the binary tree and an instance of concurrent.futures.Executor as input.
Provides a method calculate_size to calculate the size (number of nodes) of the binary tree.
Utilizes parallel processing by submitting tasks to the executor to calculate the size of the left and right subtrees concurrently.
Waits for all tasks to complete before returning the total size.
Instructions
Implement the _calculate_size_recursive method in the TreeSizeCalculator class, which recursively calculates the size of the binary tree using
parallel processing.
Ensure that the calculate_size method properly invokes the _calculate_size_recursive method and handles the case when the root node is None.
_calculate_size_recursive function doesn't return any value but should update the size property given in the constructor.
'''


class Node:

    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class TreeSizeCalculator:
    pass