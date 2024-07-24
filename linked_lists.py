def max(linked_list:'SinglyLinkedList') -> object:
    if linked_list.empty: return None
    if len(linked_list) == 0: return linked_list.first
    aux = linked_list.first.next  # type: ignore
    greater = linked_list.first.info # type: ignore
    while(aux != None):
        if aux.info > greater: # type: ignore
            greater = aux.info
        aux = aux.next
    return greater


def min(linked_list:'SinglyLinkedList') -> object:
    if linked_list.empty: return None
    if len(linked_list) == 0: return linked_list.first
    aux = linked_list.first.next  # type: ignore
    less = linked_list.first.info # type: ignore
    while(aux != None):
        if aux.info < less: # type: ignore
            less = aux.info
        aux = aux.next
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
    
class SinglyLinkedList:
    
    __first: Node|None = None
    __last: Node|None = None
    
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
    
    def index_value(self, value:object) -> int:
        if self.empty: return -1
        index = 0
        aux = self.first
        while(aux != None):
            if aux.info == value: return index
            aux = aux.next
            index += 1
        return -1
    
    def remove_index(self, index:int):
        if self.empty: raise IndexError(f"IndexError: index {index} does not exist, SinglyLinkedList is empty!")
        if index == 0: return self.remove()
        if index == len(self)-1: return self.pop()
        aux, count = self.first, 0
        while(aux != None):
            if(count + 1 == index):
                info = aux.next.info # type: ignore
                aux.next = aux.next.next # type: ignore
                return info
            count+=1
            aux = aux.next
        raise IndexError(f"IndexError: index {index} is out of bounds of SinglyLinkedList of lenght {len(self)}")
    
    def insert_index(self, index:int, value:object):
        if self.empty: raise IndexError(f"IndexError: index {index} does not exist, SinglyLinkedList is empty!")
        if index == 0: return self.insert(value)
        if index == len(self)-1: return self.append(value)
        if index > len(self)-1: raise IndexError(f"IndexError: index {index} is out of bounds of SinglyLinkedList of length {len(self)}")
        new_node = Node(value)
        current = self.first
        for _ in range(index - 1):
            current = current.next # type: ignore
        new_node.next = current.next # type: ignore
        current.next = new_node # type: ignore
    
    