class Queue:
    def __init__(self):
        self.stack_new = []
        self.stack_old = []

    def enq(self, x):
        self.stack_new.append(x)

    def shift(self):
        if not self.stack_old:
            while self.stack_new:
                self.stack_old.append(self.stack_new.pop())

    def deq(self):
        self.shift()
        if self.stack_old:
            self.stack_old.pop()

    def peek(self):
        self.shift()
        if self.stack_old:
            print(self.stack_old[-1])


if __name__ == '__main__':
    q = int(input())
    queue = Queue()
    
    for _ in range(q):
        query = input().strip().split()
        if query[0] == '1':
            queue.enq(int(query[1]))
        elif query[0] == '2':
            queue.deq()
        elif query[0] == '3':
            queue.peek()
