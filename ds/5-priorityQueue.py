class PriorityQueue:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return not self.items

    def insert(self, item):
        self.items.append(item)

    def remove(self):
        maxi = 0
        for i in range(1, len(self.items)):
            if self.items[i] > self.items[maxi]:
                maxi = i
        item = self.items[maxi]
        del self.items[maxi]
        return item
    def print_queue(self):
        print(self.items)

q = PriorityQueue()
q.insert(30)
q.insert(50)
q.insert(20)
q.print_queue()
q.remove()
q.print_queue()
