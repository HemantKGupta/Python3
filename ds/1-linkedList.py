class Node:
    def __init__(self, cargo=None, next=None):
        self.cargo = cargo
        self.next = next

    def __str__(self):
        return str(self.cargo)


def print_list(node):
    while node is not None:
        print(node, end=" ")
        node = node.next
    print()

def print_list_backwards(list):
    if list.next is None:
        print(list, end=" ")
    else:
        print_list_backwards(list.next)
        print(list, end=" ")


def print_list_backwards2(list):
    if list is None: return
    print_list_backwards2(list.next)
    print(list, end=" ")

node = Node("test")
print(node)

node1 = Node(1)
node2 = Node(2)
node3 = Node(3)

node1.next = node2
node2.next = node3

print_list(node1)
print_list_backwards(node1)
print("\nagain")
print_list_backwards2(node1)