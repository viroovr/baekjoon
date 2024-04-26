from collections import defaultdict


class Node:
    def __init__(self, data=0) -> None:
        self.next = None
        self.data = data


class LinkedList:
    def __init__(self, original=None) -> None:
        if original is None:
            self.head = Node()
            self.total_length = 0
        else:
            self.constructWithList(original)

    def setMemberWithList(self, original):
        self.head = original[0]
        self.total_length = len(original)

    def setLinkedNodeWithList(self, original):
        last_second_node_index = len(original) - 1
        for i in range(last_second_node_index):
            original[i].next = original[i + 1]

    def constructWithList(self, original):
        self.setMemberWithList(original)
        self.setLinkedNodeWithList(original)

    def getTailNode(self):
        head = self.head
        last_node_index = self.total_length - 1
        for _ in range(last_node_index):
            head = head.next
        return head

    def addNodeToTail(self, node):
        tail = self.getTailNode()
        if self.total_length == 0:
            self.head = node
        else:
            tail.next = node
        self.total_length += 1

    def printLinkedList(self):
        head = self.head
        i = 0
        while head:
            print(head.data, end="->")
            head = head.next
            i += 1
        print("N")

    def removeNodeWithPrev(self, prev):
        self.total_length -= 1
        prev.next = prev.next.next

    def removeRedundantNode(self):
        head = self.head
        dic = defaultdict(int)
        dic[head.data] = 1
        while head.next:
            if dic[head.next.data] == 1:
                self.removeNodeWithPrev(head)
            else:
                dic[head.next.data] = 1
                head = head.next

    def checkKNum(self, k):
        return k > self.total_length or k <= 0

    def search_backward_kth_node(self, k: int):
        if self.checkKNum(k):
            return None
        head = self.head
        for _ in range(self.total_length - k):
            head = head.next
        return head.data

    def remove_middle_node(self):
        if self.total_length < 3:
            return
        mid = self.total_length // 2
        head = self.head
        for _ in range(mid - 1):
            head = head.next
        self.removeNodeWithPrev(head)

    def move_node(self, x):
        head = self.head
        small_node, big_node = small_head, big_head = Node(0), Node(0)
        while head:
            if head.data < x.data:
                small_node.next = head
                small_node = head
            else:
                big_node.next = head
                big_node = head
            head = head.next
        self.head = small_head.next
        small_node.next = big_head.next
        big_node.next = None


# li = [Node(11), Node(3), Node(5), Node(8), Node(
#     5), Node(10), Node(2), Node(1), Node(7)]
# ll = LinkedList(li)

# 2.1
# ll.removeRedundantNode()
# ll.printLinkedList()

# 2.2
# k = 0
# print(k, "th backward data is : ", ll.search_backward_kth_node(k))
# ll.printLinkedList()

# 2.3
# ll.remove_middle_node()
# ll.printLinkedList()

# 2.4
# ll.move_node(Node(9))
# ll.printLinkedList()

# 2.5
def addTwoLinkedList(num1: LinkedList, num2: LinkedList):
    num3 = LinkedList()
    large = max(first.total_length, second.total_length)
    num1_node, num2_node = num1.head, num2.head
    temp_zero_node = Node(0)
    upward_count = 0
    for _ in range(large):
        temp_sum = num1_node.data + num2_node.data + upward_count
        calculated_digit = temp_sum % 10
        upward_count = temp_sum // 10
        num3.addNodeToTail(Node(calculated_digit))
        num1_node, num2_node = num1_node.next, num2_node.next
        if num1_node is None:
            num1_node = temp_zero_node
        if num2_node is None:
            num2_node = temp_zero_node
    else:
        if upward_count > 0:
            num3.addNodeToTail(Node(upward_count))

    print("sum num: ")
    num3.printLinkedList()


first = [Node(7), Node(1), Node(6), Node(9), Node(9)]
second = [Node(5), Node(9), Node(3)]
first = LinkedList(original=first)
second = LinkedList(original=second)
print("first num: ")
first.printLinkedList()
print("second num: ")
second.printLinkedList()
addTwoLinkedList(first, second)
