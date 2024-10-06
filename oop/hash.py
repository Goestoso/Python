class Node:
    
    @property
    def key(self):
        return self.__key
    
    @property
    def info(self):
        return self.__info
    
    @info.setter
    def info(self, new_info):
        self.__info = new_info
        
    @property
    def next(self):
        return self.__next
    
    @next.setter
    def next(self, new_node:'Node'):
        self.__next = new_node
    
    def __init__(self, key:str, info:object):
        self.__key: str = key
        self.__info: object = info
        self.__next: Node|None = None
        
class HashTable:
    
    @property
    def size(self):
        return self.__size
    @property
    def empty(self) -> bool:
        return all(bucket is None for bucket in self.__table)
    
    @property
    def full(self) -> bool:
        return all(bucket is not None for bucket in self.__table)
    
    def __init__(self, size:int):
        self.__size = size
        self.__table: list[Node] = [None] * size # type: ignore 
        
    def hash_function(self, key:str) -> int:
        return sum(ord(c) for c in key) % self.size
    
    def resize(self, size: int):
        old_table = self.__table  
        self.__table = [None] * size  # type: ignore
        self.__size = size # type: ignore

        for bucket in old_table:
            current = bucket
            while current is not None:
                self.insert(current.key, current.info)  
                current = current.next
    
    def clear(self):
        self.__table: list[Node] = [None] * self.size # type: ignore 
            
    def insert(self, key:str, value:object):
        if self.full: self.resize(self.size*2)
        
        index = self.hash_function(key)
        aux = Node(key, value)
        
        if self.__table[index] is None: self.__table[index] = aux  # No collision, insert directly  
        else:
            current = self.__table[index]
            while current.next is not None:
                if current.key == key: 
                    current.info = value
                    return  
                current = current.next
            if current.key == key: current.info = value
            else: current.next = aux
 
            
    def search(self, key:str):
        index = self.hash_function(key)
        current = self.__table[index]
        
        while current is not None:
            if current.key == key: return current.info
            current = current.next
        return None
    
    def free_buckets(self) -> int:
        count = 0
        for bucket in self.__table:
            if bucket is None: count += 1
        return count
    
    def busy_buckets(self) -> int:
        count = 0
        for bucket in self.__table:
            if bucket is not None: count += 1
        return count
    
    def remove(self, key:str) -> object|None:
        index = self.hash_function(key)
        current = self.__table[index]
        prev = None
        while current is not None:
            if current.key == key:
                if prev is None: self.__table[index] = current.next # first Node # type: ignore 
                else: prev.next = current.next # type: ignore
                if self.size >= 10 and self.free_buckets() >  self.busy_buckets(): self.resize(self.size//2)
                return current.info
            prev = current
            current = current.next
        return None
    
    def __repr__(self) -> str:
        if self.empty: return "None"
        msg = ""
        for bucket in self.__table:
            current = bucket
            while current is not None:
                msg += f"{current.key}: {current.info}\n"
                current = current.next
        return msg
    
    def __str__(self) -> str:
        if self.empty: return "Empty"
        msg = ""
        for index, bucket in enumerate(self.__table):
            msg += f"Bucket {index}:\n"
            current = bucket
            if current is None: msg += " (empty)\n"
            else:
                while current is not None:
                    msg += f"Key: {current.key}, Info: {current.info}\n"
                    current = current.next
        return msg
    
if __name__ == "__main__":
    hash = HashTable(10)
    hash.insert('One', 1)
    hash.insert('One', 1)
    hash.insert('Two', 2)
    hash.insert('Three', 3)
    hash.insert('Four', 4)
    hash.insert('Five', 5)
    hash.insert('Six', 6)
    hash.insert('Seven', 7)
    hash.insert('Eight', 8)
    hash.insert('Nine', 9)
    hash.insert('Ten', 10)
    hash.insert('Eleven', 11)
    hash.insert('Twelve', 12)
    hash.insert('Thirteen', 13)
    hash.insert('Fourteen', 14)
    hash.insert('Fifteen', 15)
    hash.insert('Sixteen', 16)
    hash.insert('Seventeen', 17)
    hash.insert('Eighteen', 18)
    hash.insert('Nineteen', 19)
    hash.insert('Twenty', 20)
    print(hash)
    hash.remove('One')
    print(repr(hash))
    print(hash.search('Five'))
    hash.clear()
    print(hash)
    hash.insert('One', 1)
    hash.insert('One', 1)
    hash.insert('Two', 2)
    hash.insert('Three', 3)
    hash.insert('Four', 4)
    hash.insert('Five', 5)
    hash.insert('Six', 6)
    hash.insert('Seven', 7)
    hash.insert('Eight', 8)
    hash.insert('Nine', 9)
    hash.insert('Ten', 10)
    print(hash)
    print(hash.free_buckets())
    print(hash.busy_buckets())
    hash.insert('One', -1)
    print(hash)