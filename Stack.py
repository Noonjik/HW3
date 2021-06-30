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
stack=Stack()
stack.pop()