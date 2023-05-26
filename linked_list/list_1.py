class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    def __str__(self):
        return str(self.data)


class LinkedList:
    def __init__(self, *args):
        self.head = None

        for arg in args:
            self.append(arg)

    def __str__(self):
        if self.is_empty():
            return "LinkedList is empty!"
        current = self.head
        result = []
        while current:
            result.append(str(current.data))
            current = current.next
        return " -> ".join(result)

    def is_empty(self):
        return self.head is None

    def append(self, data):
        new_node = Node(data)
        if self.is_empty():
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node

    def prepend(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def delete(self, data):
        if self.head and self.head.data == data:
            self.head = self.head.next

        current = self.head
        while current.next:
            if current.next.data == data:
                current.next = current.next.next
            current = current.next

    def search(self, data):
        current = self.head
        while current:
            if current.data == data:
                return True
            current = current.next
        return False

    def print_list(self):
        current = self.head
        while current:
            print(current.data, end=' ')
            current = current.next
        print()

    def get_length(self):
        count = 0
        current = self.head
        while current:
            count += 1
            current = current.next
        return count

    def reverse(self):
        previous = None
        current = self.head
        while current:
            next_node = current.next
            current.next = previous
            previous = current
            current = next_node
        self.head = previous

    def get_n_from_end(self, n):
        if n <= 0:
            return None

        pos1 = self.head
        pos2 = self.head

        flag3 = False
        counter = 1

        while pos2 is not None:
            if pos2.next is None:
                if n == 1:
                    return pos2
                elif counter == (n - 1) and flag3:
                    return pos1

            if pos2.next is not None and counter == (n - 1) and flag3:
                pos1 = pos1.next
                pos2 = pos2.next
            else:
                pos2 = pos2.next

            if not flag3:
                counter += 1
                if counter == n:
                    counter -= 1
                    flag3 = True

        return None


ll = LinkedList()
ll.append(1)
ll.append(2)
ll.append(33)
ll.append(3)
ll.append(5)
ll.print_list()
print(ll.search(33), "| len = ", ll.get_length())
ll.delete(33)
ll.print_list()
print(ll.search(33), "| len = ", ll.get_length())
ll.prepend(0)
ll.print_list()
ll.reverse()
print(ll)
ll2 = LinkedList(3, 2, 1)
print(ll2)
ll3 = LinkedList()
print(ll3)
print(ll.get_n_from_end(1))
print(ll.get_n_from_end(3))
print(ll.get_n_from_end(6))