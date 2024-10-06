from typing import Iterable, Any

def max(linked_list:'SinglyLinkedList|DoublyLinkedList|CircularLinkedList') -> object:
    if linked_list.empty: return None
    if isinstance(linked_list, SinglyLinkedList):
        if len(linked_list) == 0: return linked_list.first
        aux = linked_list.first.next  # type: ignore
        greater = linked_list.first.info # type: ignore
        while(aux != None):
            if aux.info > greater: # type: ignore
                greater = aux.info
            aux = aux.next
        return greater
    elif isinstance(linked_list, DoublyLinkedList):
        if len(linked_list) == 0: return linked_list.head
        aux = linked_list.head.next  # type: ignore
        greater = linked_list.head.info # type: ignore
        while(aux != None):
            if aux.info > greater: # type: ignore
                greater = aux.info
            aux = aux.next
        return greater
    elif isinstance(linked_list, CircularLinkedList):
        if len(linked_list) == 0: return linked_list.head
        aux = linked_list.head.next  # type: ignore
        greater = linked_list.head.info # type: ignore
        while(aux != linked_list.head):
            if aux.info > greater: # type: ignore
                greater = aux.info # type: ignore
            aux = aux.next # type: ignore
        return greater


def min(linked_list:'SinglyLinkedList|DoublyLinkedList|CircularLinkedList') -> object:
    if linked_list.empty: return None
    if isinstance(linked_list, SinglyLinkedList):
        if len(linked_list) == 0: return linked_list.first
        aux = linked_list.first.next  # type: ignore
        less = linked_list.first.info # type: ignore
        while(aux != None):
            if aux.info < less: # type: ignore
                less = aux.info
            aux = aux.next
        return less
    elif isinstance(linked_list, DoublyLinkedList):
        if len(linked_list) == 0: return linked_list.head
        aux = linked_list.head.next  # type: ignore
        less = linked_list.head.info # type: ignore
        while(aux != None):
            if aux.info < less: # type: ignore
                less = aux.info
            aux = aux.next
        return less
    elif isinstance(linked_list, CircularLinkedList):
        if len(linked_list) == 0: return linked_list.head
        aux = linked_list.head.next  # type: ignore
        less = linked_list.head.info # type: ignore
        while(aux != linked_list.head):
            if aux.info < less: # type: ignore
                less = aux.info # type: ignore
            aux = aux.next # type: ignore
        return less

class Node:
    
    def __init__(self, info:object) -> None:
        self.__info = info
        self.next = None 
    
    @property
    def info(self):
        return self.__info
    
    @info.setter
    def info(self, info:object):
        self.__info = info
    
    @property
    def next(self) -> 'Node|None':
        return self.__next
    
    @next.setter
    def next(self, next:'Node|None'):
        self.__next = next
        
    def __str__(self) -> str:
        return f"|{self.info}|->"
    
class DoubleNode:
    
    def __init__(self, info:object) -> None:
        self.__info = info
        self.next = None
        self.previous = None
    
    @property
    def info(self):
        return self.__info
    
    @info.setter
    def info(self, info:object):
        self.__info = info
    
    @property
    def next(self) -> 'DoubleNode|None':
        return self.__next
    
    @next.setter
    def next(self, next:'DoubleNode|None'):
        self.__next = next
    
    @property
    def previous(self) -> 'DoubleNode|None':
        return self.__previous
    
    @previous.setter
    def previous(self, previous:'DoubleNode|None'):
        self.__previous = previous
        
    def __str__(self) -> str:
        return f"<-|Info: {self.info}|->"
    
    def __repr__(self) -> str:
        return f"<-|{self.info}|->"
    
class SinglyLinkedList: # whithout tail or last node, just first/head node
    
    @property
    def first(self) -> Node|None:
        return self.__first
    
    @property
    def last(self) -> Node|None:
        return self.__last
    
    @property
    def empty(self) -> bool:
        return self.__first == None
    
    @staticmethod # @staticmethod is a class method to the current class instance # @classmethod is a class method to all instances of class SinglyLinkedList
    def join(linked_list:'SinglyLinkedList', other_linked_list:'SinglyLinkedList'):
        union = SinglyLinkedList()
        current = linked_list.first
        while current:
            union.append(current.info)
            current = current.next
        current = other_linked_list.first
        while current:
            union.append(current.info)
            current = current.next
        return union
    
    def __init__(self, linked_list:'SinglyLinkedList|None'=None) -> None: # Overload constructor
        if linked_list:
            current = linked_list.first # type: ignore 
            self.__last = Node(current.info) # type: ignore 
            self.__first = self.__last
            while(current != None):
                node = Node(current.info)
                self.__last.next = node  # type: ignore
                self.__last = node
                current = current.next
        else:
            self.__first: Node|None = None # instance attributes
            self.__last: Node|None = None

    def __len__(self):
        if self.empty: return 0
        aux, count = self.first, 0
        while(aux != None):
            aux = aux.next
            count +=1
        return count
    
    def __str__(self) -> str:
        temp:str = "Linked List: "
        if self.empty: return temp + 'empty'
        else:
            aux = self.first
            while(aux != None):
                temp += str(aux)
                aux = aux.next
            temp += "\\\\"
        return temp
    
    def __repr__(self) -> str:
        temp:str = ""
        if self.empty: return temp + 'None'
        else:
            aux = self.first
            while(aux != None):
                temp += str(aux)
                aux = aux.next
            temp += " None"
        return temp
    
    def clear(self):
        self.__first = None
        self.__last = None
            
    def insert(self, value:object):
        new = Node(value)
        if self.empty:
            self.__first = new 
            self.__last = self.first
        else:
            new.next = self.first # type: ignore
            self.__first = new
        
    def append(self, value:object):
        new = Node(value)
        if self.empty: 
            self.__last = new 
            self.__first = self.last
        else:
            self.__last.next = new  # type: ignore
            self.__last = new
        
    def pop(self):
        if self.empty: raise TypeError("TypeError: cannot pop None, the SinglyLinkedList is empty!")
        temp = None
        if self.first.next == None: # type: ignore
            temp = self.first.info # type: ignore
            self.__first = None
            self.__last = None
        else:
            aux = self.first
            while(aux.next.next != None): # type: ignore
                aux = aux.next # type: ignore
            temp = aux.next.info # type: ignore
            aux.next = None # type: ignore
            self.__last = aux
        return temp
    
    def remove(self):
        if self.empty: raise TypeError("TypeError: cannot remove None, the SinglyLinkedList is empty!")
        temp = self.first.info # type: ignore
        self.__first = self.first.next # type: ignore
        if self.empty: self.__last = None
        return temp
    
    def count(self, value:object) -> int:
        if self.empty: return 0
        count = 0
        aux = self.first
        while(aux != None):
            if aux.info == value: count += 1
            aux = aux.next
        return count
    
    def index(self, value:object) -> int:
        if self.empty: return -1
        index = 0
        aux = self.first
        while(aux != None):
            if aux.info == value: return index
            aux = aux.next
            index += 1
        return -1
    
    def value(self, index:int) -> object:
        if self.empty: raise IndexError(f"IndexError: index {index} does not exist, SinglyLinkedList is empty!")
        elif index < 0: raise IndexError(f"IndexError: index {index} is negative, there aren't negative indexes!")
        elif index == 0: return self.first.info # type: ignore
        elif index == len(self)-1: return self.last.info # type: ignore
        elif index >= len(self): raise IndexError(f"IndexError: index {index} is out of bounds of SinglyLinkedList of lenght {len(self)}")
        else:
            aux = self.first
            for i in range(len(self)-1):
                if i == index: return aux.info # type: ignore
                aux = aux.next # type: ignore
    
    def remove_index(self, index:int) -> object:
        if self.empty: raise IndexError(f"IndexError: index {index} does not exist, SinglyLinkedList is empty!")
        elif index < 0: raise IndexError(f"IndexError: index {index} is negative, there aren't negative indexes!")
        elif index == 0: return self.remove()
        elif index == len(self)-1: return self.pop()
        elif index >= len(self): raise IndexError(f"IndexError: index {index} is out of bounds of SinglyLinkedList of lenght {len(self)}")
        else:
            aux, count = self.first, 0
            while(aux != None):
                if(count + 1 == index):
                    info = aux.next.info # type: ignore
                    aux.next = aux.next.next # type: ignore
                    return info
                count+=1
                aux = aux.next
        
    def insert_index(self, index:int, value:object):
        if self.empty: raise IndexError(f"IndexError: index {index} does not exist, SinglyLinkedList is empty!")
        elif index < 0: raise IndexError(f"IndexError: index {index} is negative, there aren't negative indexes!")
        elif index == 0: return self.insert(value)
        elif index == len(self): return self.append(value)
        elif index > len(self): raise IndexError(f"IndexError: index {index} is out of bounds of SinglyLinkedList of length {len(self)}")
        else:
            new_node = Node(value)
            current = self.first
            for _ in range(index - 1):
                current = current.next # type: ignore
            new_node.next = current.next # type: ignore
            current.next = new_node # type: ignore
        
class DoublyLinkedList:
    
    @property
    def head(self):
        return self.__head
    
    @property
    def tail(self):
        return self.__tail
    
    @property
    def empty(self) -> bool:
        return self.head == None
    
    @staticmethod # @staticmethod is a class method to the current class instance # @classmethod is a class method to all instances of class SinglyLinkedList
    def join(linked_list:'DoublyLinkedList', other_linked_list:'DoublyLinkedList'):
        union = DoublyLinkedList()
        current = linked_list.head
        while current:
            union.append(current.info)
            current = current.next
        current = other_linked_list.head
        while current:
            union.append(current.info)
            current = current.next
        return union
    
    @staticmethod
    def middle_value(linked_list:'DoublyLinkedList'):
        if linked_list.empty: raise TypeError("TypeError: Nonetype does not have middle node, the DoublyLinkedList is empty!")
        elif len(linked_list) == 1: return linked_list.head.info # type: ignore
        else: 
            n, p = linked_list.head, linked_list.tail # type: ignore
            if len(linked_list)%2==0:
                for _ in range(len(linked_list)//2):
                    n = n.next # type: ignore
                    p = p.previous # type: ignore
                return p.info, n.info # type: ignore
            else: 
                for _ in range(len(linked_list)):
                    n = n.next # type: ignore
                    p = p.previous # type: ignore
                    if n == p: # type: ignore
                        return n.info # type: ignore
                    
    @staticmethod
    def middle_index(linked_list:'DoublyLinkedList'):
        if linked_list.empty: raise TypeError("TypeError: Nonetype does not have middle node, the DoublyLinkedList is empty!")
        elif len(linked_list) == 1: return 0 # type: ignore
        else: 
            n, p = linked_list.head, linked_list.tail # type: ignore
            if len(linked_list)%2==0:
                for i in range(len(linked_list)//2):
                    n = n.next # type: ignore
                    p = p.previous # type: ignore
                return i, i+1 # type: ignore
            else: 
                for i in range(len(linked_list)):
                    n = n.next # type: ignore
                    p = p.previous # type: ignore
                    if n == p: # type: ignore
                        return i+1 # type: ignore
    
    @staticmethod
    def copy(linked_list:'DoublyLinkedList'):
        if linked_list:
            copy, aux = DoublyLinkedList(), linked_list.head
            while(aux!=None):
                copy.append(aux.info)
                aux = aux.next
            return copy
            
    def __init__(self, iterable:Iterable[Any]|None=None) -> None:
        self.__head: DoubleNode|None = None
        self.__tail: DoubleNode|None = None
        if iterable:
            for value in iterable:
                self.append(value)
         
    
    def __len__(self):
        if self.empty: return 0
        aux, count = self.head, 0
        while(aux != None):
            aux = aux.next
            count +=1
        return count
    
    def __str__(self) -> str:
        temp:str = "Doubly Linked List: "
        if self.empty: return temp + 'empty'
        else:
            aux = self.head
            while(aux != None):
                temp += str(aux)
                aux = aux.next
            temp += "\\\\"
        return temp
    
    def __repr__(self) -> str:
        temp:str = ""
        if self.empty: return temp + 'None'
        else:
            aux = self.head
            while(aux != None):
                temp += str(aux)
                aux = aux.next
            temp += " None"
        return temp
    
    def clear(self):
        self.__head = None
        self.__tail = None
        
    def insert(self, value:object):
        aux = DoubleNode(value)
        if self.empty:
            self.__head = aux
            self.__tail = aux
        else:
            aux.next = self.head
            self.head.previous = aux # type: ignore
            self.__head = aux
    
    def append(self, value:object):
        aux = DoubleNode(value)
        if self.empty:
            self.__head = aux
            self.__tail = aux
        else:
            self.tail.next = aux # type: ignore
            aux.previous = self.tail
            self.__tail = aux
    
    def remove(self):
        if self.empty: raise TypeError("TypeError: cannot remove None, the DoublyLinkedList is empty!")
        if not self.head.next: # type: ignore 
            temp = self.head.info # type: ignore 
            self.__head = None
            self.__tail = None
            return temp
        temp = self.head.info # type: ignore
        self.__head = self.head.next # type: ignore
        if self.empty: self.__tail = None
        return temp
    
    def pop(self):
        if self.empty: raise TypeError("TypeError: cannot pop None, the DoublyLinkedList is empty!")
        if not self.tail.previous: # type: ignore 
            temp = self.tail.info # type: ignore 
            self.__head = None
            self.__tail = None
            return temp
        temp = self.tail.info # type: ignore
        self.__tail = self.tail.previous # type: ignore
        self.__tail.next = None # type: ignore
        if self.empty: self.__head = None
        return temp
    
    def count(self, value:object) -> int:
        if self.empty: return 0
        count = 0
        aux = self.head
        while(aux != None):
            if aux.info == value: count += 1
            aux = aux.next
        return count
    
    def index(self, value:object) -> int:
        if self.empty: return -1
        index = 0
        aux = self.head
        while(aux != None):
            if aux.info == value: return index
            aux = aux.next
            index += 1
        return -1
    
    def last_index(self, value:object) -> int:
        if self.empty: return -1
        index = len(self)-1
        aux = self.tail
        while(aux != None):
            if aux.info == value: return index
            aux = aux.previous
            index -= 1
        return -1
    
    def value(self, index:int) -> object:
        if self.empty: raise IndexError(f"IndexError: index {index} is out of bounds of DoublyLinkedList of length {len(self)}")
        elif index < 0: raise IndexError(f"IndexError: index {index} is negative, there aren't negative indexes!")
        elif index >= len(self): raise IndexError(f"IndexError: index {index} is out of bounds of DoublyLinkedList of lenght {len(self)}")
        elif index == 0: return self.head.info # type: ignore
        elif index == len(self)-1: return self.tail.info # type: ignore
        elif index >= len(self) // 2: # using an algorithm that doesn't need to scan the list much
            aux, i = self.tail.previous, len(self)-2 # type: ignore
            while(i>=0):
                if i == index: return aux.info # type: ignore
                aux = aux.previous # type: ignore
                i -= 1
        else:
            aux = self.head.next # type: ignore
            for i in range(1, index):
                if i == index: return aux.info # type: ignore
                aux = aux.next # type: ignore
    
    def replace_value(self, index:int, new_value:object):
        if self.empty: raise TypeError("TypeError: cannot replace Nonetype value, the DoublyLinkedList is empty!")
        elif index < 0: raise IndexError(f"IndexError: index {index} is negative, there aren't negative indexes!")
        elif index >= len(self): raise IndexError(f"IndexError: index {index} is out of bounds of DoublyLinkedList of lenght {len(self)}")
        aux, i = self.tail, len(self)-1
        if index >= len(self) // 2: 
            while(i>=0):
                if i == index: 
                    aux.info = new_value # type: ignore
                    return
                aux = aux.previous # type: ignore
                i -= 1 
        else:
            for i in range(index):
                if i == index:
                    aux.info = new_value # type: ignore
                    return
                aux = aux.next # type: ignore
    
    def replace_all(self, old_value:object, new_value:object):
        if self.empty: raise TypeError("TypeError: cannot replace Nonetype value, the DoublyLinkedList is empty!")
        aux = self.head
        while(aux!=None):
            if aux.info == old_value: aux.info = new_value
            aux = aux.next
    
    def remove_index(self, index:int) -> object:
        if self.empty: raise IndexError(f"IndexError: index {index} does not exist, SinglyLinkedList is empty!")
        elif index < 0: raise IndexError(f"IndexError: index {index} is negative, there aren't negative indexes!")
        elif index == 0: return self.remove()
        elif index == len(self)-1: return self.pop()
        elif index >= len(self): raise IndexError(f"IndexError: index {index} is out of bounds of SinglyLinkedList of lenght {len(self)}")
        elif index >= len(self) // 2:
            aux, i = self.tail, len(self)-1 # type: ignore
            while(aux != None):
                if i == index:
                    temp = aux.info 
                    aux.previous.next = aux.next # type: ignore
                    aux.next.previous = aux.previous # type: ignore
                    return temp
                aux = aux.previous
                i -= 1
        else: 
            aux = self.head.next # type: ignore
            for i in range(1,index):
                if i == index:
                    temp = aux.info # type: ignore
                    aux.previous.next = aux.next# type: ignore
                    aux.next.previous = aux.previous # type: ignore
                    return temp
                aux = aux.next # type: ignore
    
    def insert_index(self, index:int, value:object):
        if self.empty: raise IndexError(f"IndexError: index {index} does not exist, SinglyLinkedList is empty!")
        elif index < 0: raise IndexError(f"IndexError: index {index} is negative, there aren't negative indexes!")
        elif index > len(self): raise IndexError(f"IndexError: index {index} is out of bounds of SinglyLinkedList of length {len(self)}")
        elif index == 0: return self.insert(value)
        elif index == len(self): return self.append(value)
        elif index >= len(self) // 2:
            new, aux, i = DoubleNode(value), self.tail, len(self)-1 # type: ignore
            if len(self)==2: 
                self.head.next = new  # type: ignore
                self.tail.previous = new # type: ignore
                new.next = self.tail
                new.previous = self.head 
                return
            if index == len(self)-1: 
                self.tail.previous.next = new # type: ignore
                new.next = self.tail
                new.previous = self.tail.previous # type: ignore
                self.tail.previous = new # type: ignore
                return
            while(i>=0):
                if i == index:
                    aux.previous.next = new # type: ignore
                    new.next = aux # type: ignore
                    new.previous = aux.previous # type: ignore
                    return
                i -= 1
        else: 
            new, aux = DoubleNode(value), self.head # type: ignore
            for i in range(index):
                if i == index:
                    new.next = aux.next # type: ignore
                    new.previous = aux.previous # type: ignore
                    aux = new
                    return
                
class CircularLinkedList:
    
    __instances = 0
    
    @property
    def instances(self):
        return self.__instances
    
    @property
    def head(self):
        return self.__head
    
    @property
    def tail(self):
        return self.__tail
    
    @property
    def empty(self) -> bool:
        return self.head == None
    
    @staticmethod # @staticmethod is a class method to the current class instance # @classmethod is a class method to all instances of class SinglyLinkedList
    def join(linked_list:'CircularLinkedList', other_linked_list:'CircularLinkedList'):
        union = CircularLinkedList()
        current = linked_list.head
        union.append(current.info) # type: ignore
        current = current.next # type: ignore
        while current != linked_list.head:
            union.append(current.info) # type: ignore
            current = current.next # type: ignore
        current = other_linked_list.head
        union.append(current.info) # type: ignore
        current = current.next # type: ignore
        while current != other_linked_list.head:
            union.append(current.info) # type: ignore
            current = current.next # type: ignore
        return union
    
    @staticmethod
    def middle_value(linked_list:'CircularLinkedList'):
        if linked_list.empty: raise TypeError("TypeError: Nonetype does not have middle node, the DoublyLinkedList is empty!")
        elif len(linked_list) == 1: return linked_list.head.info # type: ignore
        else: 
            n, p = linked_list.head, linked_list.tail # type: ignore
            if len(linked_list)%2==0:
                for _ in range(len(linked_list)//2):
                    n = n.next # type: ignore
                    p = p.previous # type: ignore
                return p.info, n.info # type: ignore
            else: 
                for _ in range(len(linked_list)):
                    n = n.next # type: ignore
                    p = p.previous # type: ignore
                    if n == p: # type: ignore
                        return n.info # type: ignore
                    
    @staticmethod
    def middle_index(linked_list:'CircularLinkedList'):
        if linked_list.empty: raise TypeError("TypeError: Nonetype does not have middle node, the DoublyLinkedList is empty!")
        elif len(linked_list) == 1: return 0 # type: ignore
        else: 
            n, p = linked_list.head, linked_list.tail # type: ignore
            if len(linked_list)%2==0:
                for i in range(len(linked_list)//2):
                    n = n.next # type: ignore
                    p = p.previous # type: ignore
                return i, i+1 # type: ignore
            else: 
                for i in range(len(linked_list)):
                    n = n.next # type: ignore
                    p = p.previous # type: ignore
                    if n == p: # type: ignore
                        return i+1 # type: ignore
    
    @staticmethod
    def copy(linked_list:'CircularLinkedList'):
        if linked_list:
            copy, aux = CircularLinkedList(), linked_list.head
            copy.append(aux.info) # type: ignore
            aux = aux.next # type: ignore
            while(aux!=linked_list.head):
                copy.append(aux.info) # type: ignore
                aux = aux.next # type: ignore
            return copy
        
    @staticmethod
    def to_list(linked_list:'CircularLinkedList') -> list[object]:
        array = list()
        if linked_list:
            aux = linked_list.head
            array.append(aux.info) # type: ignore
            aux = aux.next # type: ignore
            while(aux != linked_list.head):
                array.append(aux.info) # type: ignore
                aux = aux.next # type: ignore
        return array
    
    @classmethod
    def __increment_instances_count(cls): # this increments the value for each new instance created
        cls.__instances += 1
        
    def __init__(self, iterable:Iterable[Any]|None=None) -> None:
        self.__head: DoubleNode|None = None
        self.__tail: DoubleNode|None = None
        self.__increment_instances_count()
        if iterable:
            for value in iterable:
                self.append(value)
    
    def __len__(self):
        if self.empty: return 0
        aux, count = self.head, 1
        aux = aux.next  # type: ignore
        while(aux != self.head):  # type: ignore
            aux = aux.next  # type: ignore
            count +=1
        return count
    
    def __str__(self) -> str:
        temp:str = "Circular Linked List: "
        if self.empty: return temp + 'empty'
        temp += "○ "
        aux = self.head
        temp += str(aux)
        aux = aux.next  # type: ignore
        while(aux != self.head):
            temp += str(aux)
            aux = aux.next  # type: ignore
        temp += " ○"
        temp += "\n                      |"
        for _ in range(22,len(temp)-26):
            temp += "_"
        temp += "|"
        return temp
    
    def __repr__(self) -> str:
        temp:str = "(tail) "
        if self.empty: return temp + 'None'
        aux = self.head
        temp += str(aux)
        aux = aux.next  # type: ignore
        while(aux != self.head):
            temp += str(aux)
            aux = aux.next  # type: ignore
        temp += " (head)"
        return temp
    
    def clear(self):
        self.__head = None
        self.__tail = None
        
    def insert(self, value:object):
        aux = DoubleNode(value)
        if self.empty:
            self.__head = aux
            self.__tail = aux
        else:
            aux.next = self.head
            aux.previous = self.tail
            self.head.previous = aux # type: ignore
            self.__head = aux
            self.tail.next = self.head  # type: ignore
    
    def append(self, value:object):
        aux = DoubleNode(value)
        if self.empty:
            self.__head = aux
            self.__tail = aux
        else:
            aux.previous = self.tail
            aux.next = self.head
            self.tail.next = aux # type: ignore
            self.__tail = aux
            self.head.previous = self.tail # type: ignore
    
    def remove(self) -> object:
        if self.empty: raise TypeError("TypeError: cannot remove None, the CircularLinkedList is empty!")
        if self.head == self.tail: # type: ignore 
            temp = self.head.info # type: ignore 
            self.__head = None
            self.__tail = None
            return temp
        temp = self.head.info # type: ignore
        self.__head = self.head.next # type: ignore
        self.head.previous = self.tail # type: ignore
        self.tail.next = self.head # type: ignore
        return temp
    
    def pop(self) -> object:
        if self.empty: raise TypeError("TypeError: cannot remove None, the CircularLinkedList is empty!")
        if self.tail == self.head: # type: ignore 
            temp = self.tail.info # type: ignore 
            self.__head = None
            self.__tail = None
            return temp
        temp = self.tail.info # type: ignore
        self.__tail = self.tail.previous # type: ignore
        self.tail.next = self.head # type: ignore
        self.head.previous = self.tail # type: ignore
        return temp
    
    def count(self, value:object) -> int:
        if self.empty: return 0
        count = 1
        aux = self.head
        aux = aux.next # type: ignore
        while(aux != self.head):
            if aux.info == value: count += 1 # type: ignore
            aux = aux.next # type: ignore
        return count     
    
    def index(self, value:object) -> int:
        if self.empty: return -1
        if value == self.head.info: return 0 # type: ignore
        index = 1
        aux = self.head
        aux = aux.next  # type: ignore
        while(aux != self.head):
            if aux.info == value: return index  # type: ignore
            aux = aux.next  # type: ignore
            index += 1
        return -1
    
    def last_index(self, value:object) -> int:
        if self.empty: return -1
        if self.tail.info == value: return len(self)-1 # type: ignore
        index = len(self)-2
        aux = self.tail
        aux = aux.previous # type: ignore
        while(aux != self.tail): 
            if aux.info == value: return index # type: ignore
            aux = aux.previous # type: ignore
            index -= 1
        return -1
    
    def value(self, index:int) -> object:
        if self.empty: raise IndexError(f"IndexError: index {index} is out of bounds of DoublyLinkedList of length {len(self)}")
        elif index < 0: raise IndexError(f"IndexError: index {index} is negative, there aren't negative indexes!")
        elif index >= len(self): raise IndexError(f"IndexError: index {index} is out of bounds of DoublyLinkedList of lenght {len(self)}")
        elif index == 0: return self.head.info # type: ignore
        elif index == len(self)-1: return self.tail.info # type: ignore
        elif index >= len(self) // 2: # using an algorithm that doesn't need to scan the list much
            aux, i = self.tail.previous, len(self)-2 # type: ignore
            while(i>=0):
                if i == index: return aux.info # type: ignore
                aux = aux.previous # type: ignore
                i -= 1
        else:
            aux = self.head.next # type: ignore
            for i in range(1, index):
                if i == index: return aux.info # type: ignore
                aux = aux.next # type: ignore

    def replace_value(self, index:int, new_value:object):
        if self.empty: raise TypeError("TypeError: cannot replace Nonetype value, the DoublyLinkedList is empty!")
        elif index < 0: raise IndexError(f"IndexError: index {index} is negative, there aren't negative indexes!")
        elif index >= len(self): raise IndexError(f"IndexError: index {index} is out of bounds of DoublyLinkedList of lenght {len(self)}")
        aux, i = self.tail, len(self)-1
        if index >= len(self) // 2: 
            while(i>=0):
                if i == index: 
                    aux.info = new_value # type: ignore
                    return
                aux = aux.previous # type: ignore
                i -= 1 
        else:
            for i in range(index):
                if i == index:
                    aux.info = new_value # type: ignore
                    return
                aux = aux.next # type: ignore
    
    def replace_all(self, old_value:object, new_value:object):
        if self.empty: raise TypeError("TypeError: cannot replace Nonetype value, the DoublyLinkedList is empty!")
        if self.head.info == old_value: self.head.info = new_value # type: ignore
        aux = self.head
        aux = aux.next # type: ignore
        while(aux!=self.head):
            if aux.info == old_value: aux.info = new_value # type: ignore
            aux = aux.next # type: ignore
    
    def remove_index(self, index:int) -> object:
        if self.empty: raise IndexError(f"IndexError: index {index} does not exist, SinglyLinkedList is empty!")
        elif index < 0: raise IndexError(f"IndexError: index {index} is negative, there aren't negative indexes!")
        elif index == 0: return self.remove()
        elif index == len(self)-1: return self.pop()
        elif index >= len(self): raise IndexError(f"IndexError: index {index} is out of bounds of SinglyLinkedList of lenght {len(self)}")
        elif index >= len(self) // 2:
            aux, i = self.tail.previous, len(self)-2 # type: ignore
            while(i>=0):
                if i == index:
                    temp = aux.info # type: ignore 
                    aux.previous.next = aux.next # type: ignore
                    aux.next.previous = aux.previous # type: ignore
                    return temp
                aux = aux.previous # type: ignore
                i -= 1
        else: 
            aux = self.head.next # type: ignore
            for i in range(1,index):
                if i == index:
                    temp = aux.info # type: ignore
                    aux.previous.next = aux.next# type: ignore
                    aux.next.previous = aux.previous # type: ignore
                    return temp
                aux = aux.next # type: ignore
    
    def insert_index(self, index:int, value:object):
        if self.empty: raise IndexError(f"IndexError: index {index} does not exist, SinglyLinkedList is empty!")
        elif index < 0: raise IndexError(f"IndexError: index {index} is negative, there aren't negative indexes!")
        elif index > len(self): raise IndexError(f"IndexError: index {index} is out of bounds of SinglyLinkedList of length {len(self)}")
        elif index == 0: return self.insert(value)
        elif index == len(self): return self.append(value)
        elif index >= len(self) // 2:
            new, aux, i = DoubleNode(value), self.tail, len(self)-1 # type: ignore
            if len(self)==2: 
                self.head.next = new  # type: ignore
                self.tail.previous = new # type: ignore
                new.next = self.tail
                new.previous = self.head 
                return
            if index == len(self)-1: 
                self.tail.previous.next = new # type: ignore
                new.next = self.tail
                new.previous = self.tail.previous # type: ignore
                self.tail.previous = new # type: ignore
                return
            while(i>=0):
                if i == index:
                    aux.previous.next = new # type: ignore
                    new.next = aux # type: ignore
                    new.previous = aux.previous # type: ignore
                    return
                i -= 1
        else: 
            new, aux = DoubleNode(value), self.head # type: ignore
            for i in range(index):
                if i == index:
                    new.next = aux.next # type: ignore
                    new.previous = aux.previous # type: ignore
                    aux = new
                    return
    
    