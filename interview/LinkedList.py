class Node:
    def __init__(self, data, head=None, next=None) -> None:
        self.data = data
        self.head = head
        self.next = next

    def add_node(self, next_node):
        if self.head:
            p = self.next
            while p:
                p = p.next
            p = next_node
        else:
            return -1

    def print_node(self):
        print("head, next, data:", self.head, self.next, self.data)


head = Node(0)
node = Node(1, head)
node2 = Node(2, head)
head.next = node
head.head = head
node.next = node2

head.print_node()
node.print_node()
node2.print_node()

node.add_node(node2)


head.print_node()
node.print_node()
node2.print_node()
