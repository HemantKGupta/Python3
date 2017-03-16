class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def is_empty(self):
        return (self.items == [])

    def print_stack(self):
        while not self.is_empty():
            print(self.pop(), end=" ")

stack = Stack()
stack.push(54)
stack.push(10)
stack.print_stack()




