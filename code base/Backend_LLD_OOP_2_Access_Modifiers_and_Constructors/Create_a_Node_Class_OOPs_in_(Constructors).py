'''
Create a Node class with following requirements

Two data members
i. data : int
ii. next : Node
A constructor which takes an integer parameter. This constructor should set data property and leave the next set to null.
A constructor which takes a Node parameter. This constructor should make a deep copy of the passed node.
'''

# approach1................
class Node:

    def __init__(self, data: int):
        self.data = data
        self.next = None

    @classmethod
    def from_node(cls, node: 'Node')->'Node':
        if node is None:
            return None
        new_node = cls(node.data)
        new_node.next = cls.from_node(node.next)
        return new_node


# approach2................
class Node1:

    def __init__(self, value):

        if isinstance(value, Node1):
            self.data = value.data
            self.next = Node1(value.next) if value.next else None
        elif isinstance(value, int):
            self.data = value
            self.next = None
        else: raise TypeError("Invalid parameter type. Expected int or Node.")



