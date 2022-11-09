class Node:
    def __init__(self, data, reference=None):
        self.data = data
        self.reference = reference


class LinkedList:
    def __init__(self):
        self.head = None

    def print_linked_list(self):
        if self.head == None:
            print("The linked list is empty")
        else:
            c_node = self.head
            while c_node is not None:
                print(c_node.data)
                c_node = c_node.reference

    def add_to_start(self, data):
        n_node = Node(data, self.head)
        self.head = n_node


def main():
    node1 = Node(10)
    print(node1.data)
    node2 = Node(25, node1)
    print(node2.reference)

    linked_list_1 = LinkedList()
    linked_list_1.print_linked_list()

    linked_list_2 = LinkedList()
    linked_list_2.add_to_start(50)
    linked_list_2.add_to_start(25)
    linked_list_2.add_to_start("pickles")
    linked_list_2.add_to_start(True)

    linked_list_2.print_linked_list()


if __name__ == "__main__":
    main()
