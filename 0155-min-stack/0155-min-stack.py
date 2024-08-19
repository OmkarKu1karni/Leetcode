class MinStack:

    def __init__(self):
        self.st = []
        self.mini = float("-inf")

    def push(self, val: int) -> None:
        if len(self.st)==0 :
            self.st.append(val)
            self.mini = val
        else : 
            if val < self.mini : 
                self.st.append(2*val-self.mini)
                self.mini = val
            else : 
                self.st.append(val)

    def pop(self) -> None:
        if len(self.st)==0 :
            return 
        el = self.st[-1]
        self.st.pop()
        if el < self.mini : 
            self.mini = 2*self.mini - el
        
    def top(self) -> int:
        if len(self.st)==0 :
            return -1
        el = self.st[-1]
        if el < self.mini : 
            return self.mini
        return el 

    def getMin(self) -> int:
        return self.mini

# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()