class MyStack:

    def __init__(self):
        self.q = deque()
        self.t = None

    def push(self, x: int) -> None:
        if self.t:
            self.q.append(self.t)
            
        self.t = x

    def pop(self) -> int:
        result = self.t

        newq = deque()
        while len(self.q) > 1:
            newq.append(self.q.popleft())

        self.t = self.q.popleft() if self.q else None
        self.q = newq
            
        return result

    def top(self) -> int:
        return self.t            
        
    def empty(self) -> bool:
        return self.t is None
