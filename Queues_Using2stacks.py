class queueUsingTwoStacks:
    def __init__(self):
        self.orderedStack = []
        self.reversedStack = []

    def reverseAndPop(self):
        if (not self.reversedStack):
            while(self.orderedStack):
                self.reversedStack.append(self.orderedStack.pop())
        if (self.reversedStack):
            return self.reversedStack.pop()
        return None
    
    def enqueue(self, data):
        self.orderedStack.append(data)

    def dequeue(self):
        return self.reverseAndPop()
        
    def frontOfQueue(self):
        front = self.reverseAndPop()
        print(front)
        self.reversedStack.append(front)

q = queueUsingTwoStacks()

for _ in range(int(input())):
    cmd = input()
    if cmd[0] is "1":
        q.enqueue(int(cmd[2:]))
    elif cmd[0] is "2":
        q.dequeue()
    elif cmd[0] is "3":
        q.frontOfQueue()