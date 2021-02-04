class Node:
    def __init__(self, data=None, next_node=None):
        self.value = data
        self.next = next_node


class Circle:
    def __init__(self, head=None):
        self.head = Node(head)
        self.length = (0 if (head is not None) else 1)

    def push(self, node):
        current = self.head
        for i in range(self.length - 1):
            current = current.next
        current.next = Node(node, self.head)
        self.length += 1
        return

    def next_node(self, node):
        if node is None:
            return self.head
        return node.next

    def top(self):
        return self.head
