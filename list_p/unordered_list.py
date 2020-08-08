from list_p.node import Node


class UnorderedList:
    def __init__(self):
        self.head = None

    def isEmpty(self):
        return self.head is None

    def add(self, item):
        temp = Node(item)
        temp.setNext(self.head)
        self.head = temp

    def exits(self, item):
        n = self.head
        flag = False
        while n:
            if n.getData() == item:
                flag = True
                break
            n = n.getNext()
        return flag

    def size(self):
        counter = 0
        n = self.head
        while n:
            counter += 1
            n = n.getNext()
        return counter

    def remove(self, item):
        dummy = p = Node(0)
        p.setNext(self.head)
        n = self.head
        while n:
            if n.getData() == item:
                p.setNext(n.getNext())
                self.head = dummy.getNext()
            n = n.getNext()
            p = p.getNext()


if __name__ == '__main__':
    ul = UnorderedList()
    ul.add(1)
    ul.add(2)
    ul.add(3)
    print(ul.size())
    print(ul)
    print(ul.exits(2))
    print(ul.isEmpty())
    ul.remove(2)
    print(ul.size())
    print(ul.exits(2))
