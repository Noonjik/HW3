#balanced brackets
class Stack:
    def __init__(self):
        self._storage = []
        self._size = 0
    
    def is_empty(self):
        if self._size == 0:
            return True
    
    def push(self, value):
        self._storage.append(value)
        self._size += 1
    
    def pop (self):
        if self.is_empty():
            return None
        else:
            value = self._storage.pop(self._size - 1)
            self._size -= 1
            return value 
    
    def __str__ (self):
        print('Stack objects are:', end ='')
        print(self._storage.__str__())
        print ('Stack size:', end = '')
        print (str(self._size))

stack = Stack()

def is_balanced(str):
    opening_par = ['(', '{', '[']
    closing_par = [')', '}',']']
    result = False
    for i in str:
        if i in opening_par:
            stack.push(i)
        else:
            if stack.is_empty():
                result = False
            else:               
                if i in closing_par:
                    current_char = stack.pop()
                    if current_char == '{' and i =='}':
                        result = True
                    if current_char == '(' and i == ')':
                        result  = True
                    if current_char == '[' and i == ']':
                        result = True
                else:
                    result = False
    return result

char = input('input the expression:  ')
if is_balanced(char):
    print ('brackets are balanced')
else:
    print ('brackets are not balanced')
