#Stack implementation

class Stack:
    def __init__(self):
        self._size = 0
        self._storage = []
        self.iteration_index=0
        
    def is_empty(self):
        return self._size == 0
    
    def push(self, value):
        self._storage.append(value)
        self._size += 1
    
    def pop(self):
        if self.is_empty():
            return None
        value = self._storage.pop(self._size - 1)
        self._size -= 1
        return value
    
    def __str__(self):
        print_value = 'storage of stack: '
        print_value += self._storage.__str__()
        print_value += 'stack size: '
        print_value += str(self._size)
       
        return print_value
    
    def __iter__(self):
        self._list_iterator = iter(self._storage)
        return self._list_iterator
    def peek(self):
        if self.is_empty():
            return None
        else:
            peek = self.pop()
            self.push(peek)
            return peek 



class Min_O1(object):
    def __init__(self):
        self.main = Stack()
        self.mins = Stack()
        self._size = 0
        self._storage = []
        self.peek = self.main.peek()
     
    def push(self,value):
        self.main.push(value)
        if self.main.is_empty():
            self.mins.push(value)
            self.main.push(value)      
        elif value <= int(self.mins.peek()):
            self.mins.push(value)
        else:
            self.mins.push(self.mins.peek())
    
    def pop(self):
        if self.main.is_empty():
            return None
        else:
            self.main.pop()
            self.mins.pop()
    
    def getMin(self):
        if self.main.is_empty():
            return None
        else:
            return self.mins.peek()

#testing
test1 = Min_O1()
test1.push(5)
test1.push(7)
test1.push(8)
test1.push(9)
test1.push(2)
print (test1.getMin())
test1.pop()
test1.pop()
print (test1.getMin())
