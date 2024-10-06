from linked_lists import Iterable
import numpy as np

class Stack:
    
    def __init__(self, iterable:Iterable|None=None) -> None:
        self.__top = -1
        self.__bottom = -1
        self.DEFAULT_CAPACITY = 10
        self.__data = np.empty(shape=self.DEFAULT_CAPACITY, dtype=object)
        if iterable:
            for e in iterable:
                self.push(e)
        
    @property
    def top(self):
        return self.__data[self.__top] if self.__top != -1 else None
    
    @property
    def bottom(self):
        return self.__data[self.__bottom] if self.__bottom != -1 else None
    
    @property
    def empty(self):
        return self.__top == -1
    
    @property
    def full(self):
        return self.__top == len(self.__data)-1
    
    @staticmethod
    def copy(stack:'Stack'):
        if stack.empty: return stack
        lifo, aux = Stack(), Stack()
        while(not stack.empty):
            aux.push(stack.pop())
            
        while(not aux.empty):
            item = aux.pop()
            lifo.push(item)
            stack.push(item)
        return lifo
       
    def __len__(self):
        return self.__top+1
    
    def __str__(self) -> str:
        msg = "Stack: \n\\\\\\\n"
        if self.empty: return "Stack is empty"
        index = self.__top
        while(index>-1):
            msg += f"↑\n{str(self.__data[index])}\n"
            index -= 1
        return msg
    
    def __repr__(self) -> str:
        msg = "\nNone\n"
        if self.empty: return "None"
        index = index = self.__top
        while(index>-1):
            msg += f"↑\n{str(self.__data[index])}\n"
            index -= 1
        return msg
    
    def resize(self, new_capacity:int):
        temp = np.empty(shape=new_capacity, dtype=int)
        index = self.__top
        while(index > -1):
            temp[index] = self.__data[index]
            index-=1
        self.__data = temp
    
    def push(self, value:object):
        if self.empty:
            self.__top += 1
            self.__data[self.__top] = value
            self.__bottom = self.__top
        else:
            self.__top += 1
            self.__data[self.__top] = value
            if self.full: self.resize(len(self.__data)*2)
            
    def pop(self):
        if self.empty: raise TypeError("TypeError: cannot pop None, the Stack is empty!")
        else:
            temp = self.__data[self.__top]
            self.__top-=1
            if (len(self.__data) >= 10 and self.__top <= len(self.__data) /4): self.resize(len(self.__data)//2)
            return temp
        
    def clear(self):
        self.__top = -1
        self.__bottom = -1
        
    def push_stack(self, other_stack:'Stack'):
        if not other_stack.empty:
            aux = self.copy(other_stack)
            while(not aux.empty):
                self.push(aux.pop())

if __name__ == '__main__':
    stack = Stack()
    stack.push(1)
    stack.push(2)
    stack.push(3)
    print(stack)
    print(stack.pop())
    print(stack.pop())
    print(stack.pop())
    print(stack)
    iterable = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
    print(iterable)
    other_stack = Stack(iterable)
    print(f'Iterable Stack: {repr(other_stack)}')
    print(f'Top: {other_stack.top}')
    print(f'Bottom: {other_stack.bottom}')
    copy = Stack.copy(other_stack)
    print(f'Copy Stack: {repr(copy)}')
    stack.push_stack(copy) 
    stack.push_stack(stack)  
    print(stack)