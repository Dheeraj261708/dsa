class MyQueue(object):

    def __init__(self):
        self.Stack1=[]
        self.Stack2=[]

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        self.Stack1.append(x)
        

    def pop(self):
        """
        :rtype: int
        """
        if not self.Stack2:
            while self.Stack1:
                self.Stack2.append(self.Stack1.pop())
        return self.Stack2.pop()
        

    def peek(self):
        """
        :rtype: int
        """
        if not self.Stack2:
            while self.Stack1:
                self.Stack2.append(self.Stack1.pop())
        return self.Stack2[-1]

    def empty(self):
        """
        :rtype: bool
        """
        return len(self.Stack1)==0 and len(self.Stack2)==0


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()