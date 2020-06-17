class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[-1]

    def size(self):
        return len(self.items)

    def isEmpty(self):
        return self.items == []

    def show(self):
        print('\ntop=>', end='')
        for i in reversed(self.items):
            print('\t\t', end='')
            print(i)
        print('bottom\n')


if __name__ == '__main__':
    s = Stack()
    print(s.isEmpty())
    s.push('Bob')
    s.push(5)
    s.push('Alice')
    s.show()
    print(s.peek())
    print(s.pop())
    s.show()
