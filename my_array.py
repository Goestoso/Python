import numpy as np
from random import randint
from typing import Iterable, Tuple, List

def union(arrays:Tuple['MyArray', ...]):
    if isinstance(arrays, tuple):
        union = MyArray()
        for array in arrays:
            union.extend(array)
        return union

class MyArray:
    
    DEFAULT_CAPACITY = 10
    __lastPos = -1
    __index = 0
    __data = np.empty(shape=DEFAULT_CAPACITY, dtype=int)
    
    def __init__(self,capacity:int|None=None, data:Iterable[int]|None=None) -> None: # constructor Overload
        if capacity: self.__data = np.empty(shape=capacity, dtype=int)
        if isinstance(data, Iterable): 
            iter(data)
            for element in data:
                self.append(element)
        
    @property
    def capacity(self):
        return len(self.__data)
    
    def __str__(self) -> str: # class Object Override
        if self.is_empty(): return "Array is empty"
        else:
            msg = "My Array: "
            for i in range(self.__lastPos+1):
                msg += f"[{self.__data[i]}] "
        return msg
    
    def __repr__(self) -> str: # class Object Override
        if self.is_empty(): return "[]"
        else:
            msg = ""
            for i in range(self.__lastPos+1):
                msg += f"[{self.__data[i]}] "
        return msg
    
    def __iter__(self): # allows an object to be iterable
        for i in range(self.__lastPos + 1):
            yield self.__data[i] # yield is a keyword in Python used in generator functions.
    
    def __next__(self): # to get the next element from an iterator
        if self.__index <= self.__lastPos:
            element = self.__data[self.__index]
            self.__index += 1
            return element
        else:
            raise StopIteration
    
    def __getitem__(self, index:int|slice):
        if isinstance(index, int) and index <= self.__lastPos:
            return self.__data[index]
        elif isinstance(index, slice): return self.__data[index.start:index.stop:index.step]
        
    def __setitem__(self, index, value):
        if index < 0 or index > self.__lastPos:
            raise IndexError(f"IndexError: index {index} is out of bounds of MyArray[0, {self.__lastPos}]")
        self.__data[index] = value
    
    def __delitem__(self, index:int):
        self.pop(index)
        
    def __add__(self, array:Iterable[int]):
        if isinstance(array, Iterable):
            new_array = MyArray(data=self)
            new_array.extend(array)
            return new_array
    
    def __rmul__(self, value:int):
        return self.__mul__(value)
    
    def __mul__(self, value:int) -> Tuple['MyArray', ...] :
        if isinstance(value, int):
            return tuple([MyArray(data=self) for _ in range(value)])
                 
    def __truediv__(self, value):
        if isinstance(value, int):
            if value > 0 and value <= len(self):
                sub_length = len(self) // value
                remainder = len(self) % value
                start = 0
                subarrays: List[MyArray] = []
                for i in range(value):
                    end = start + sub_length
                    if i < remainder:
                        end += 1
                    sub = MyArray(data=self[start:end])
                    subarrays.append(sub)
                    start = end
                return tuple(subarrays)
            else:
                raise ValueError("ValueError: value must be a positive integer less than or equal to the length of the array")
        else:
            raise TypeError("TypeError: value must be an integer")
        
    def __floordiv__(self, value:int):
        return self.__truediv__(value)
    
    """Complexity O(n log n)"""
    
    def __merge_sort_descending(self, array, left, right):
        if left < right:
            middle = (left + right) // 2
            self.__merge_sort_descending(array, left, middle)
            self.__merge_sort_descending(array, middle + 1, right)
            self.__merge_descending(array, left, middle, right)
    
    """Recursion"""
    
    def __merge_descending(self, array, left, middle, right):
        n1 = middle - left + 1
        n2 = right - middle
        array_l = np.empty(shape=n1, dtype=int)
        array_r = np.empty(shape=n2, dtype=int)
        
        for i in range(n1):
            array_l[i] = array[left + i]
        for j in range(n2):
            array_r[j] = array[middle + 1 + j]
        
        i, j, k = 0, 0, left
        
        while i < n1 and j < n2:
            if array_l[i] >= array_r[j]:
                array[k] = array_l[i]
                i += 1
            else:
                array[k] = array_r[j]
                j += 1
            k += 1
        
        while i < n1:
            array[k] = array_l[i]
            i += 1
            k += 1
        
        while j < n2:
            array[k] = array_r[j]
            j += 1
            k += 1
    
    def __reversed__(self):
        temp = MyArray(data=self)
        temp.__merge_sort_descending(temp, left=0, right=self.__lastPos)
        return temp
    
    def __len__(self):
        return self.__lastPos+1
    
    def __eq__(self, object:object):
        if self is object: return True
        if isinstance(object, MyArray):
            if self.__lastPos == object.__lastPos:
                for i in range(object.__lastPos):
                    if self.__data[i] != object.__data[i]: return False
                return True
        return False
    
    def __ne__(self, object: object):
        return not self.__eq__(object)
    
    def __gt__(self, object:object): # greater than
        if isinstance(object, Iterable) and self.__len__() > len(list(object)): return True # To check if an object is iterable, we check if it is an instance of the Iterable class
        elif isinstance(object, Iterable) and self.__len__() <= len(list(object)): return False
        else: raise TypeError(f"TypeError: unorderable types: {type(self.__data)} > {type(object)}") # raising exception to unorderable types
    
            
    def __ge__(self, object:object): # greater than or equal to
        if isinstance(object, Iterable) and self.__len__() >= len(list(object)): return True # To check if an object is iterable, we check if it is an instance of the Iterable class
        elif isinstance(object, Iterable) and self.__len__() < len(list(object)): return False
        else: raise TypeError(f"TypeError: unorderable types: {type(self.__data)} > {type(object)}") # raising exception to unorderable types
    
    def __lt__(self, object:object): # less than 
        if isinstance(object, Iterable) and self.__len__() < len(list(object)): return True # To check if an object is iterable, we check if it is an instance of the Iterable class
        elif isinstance(object, Iterable) and self.__len__() >= len(list(object)): return False
        else: raise TypeError(f"TypeError: unorderable types: {type(self.__data)} > {type(object)}") # raising exception to unorderable types
    
    def __le__(self, object:object): # less than or equal to
        if isinstance(object, Iterable) and self.__len__() <= len(list(object)): return True # To check if an object is iterable, we check if it is an instance of the Iterable class
        elif isinstance(object, Iterable) and self.__len__() > len(list(object)): return False
        else: raise TypeError(f"TypeError: unorderable types: {type(self.__data)} > {type(object)}") # raising exception to unorderable types

    def is_empty(self) -> bool:
        return self.__lastPos == -1
    
    def is_full(self) -> bool:
        return self.__len__() == len(self.__data)
    
    def resize(self, new_capacity:int):
        temp = np.empty(shape=new_capacity, dtype=int)
        for i in range(self.__lastPos+1):
            temp[i] = self.__data[i]
        self.__data = temp
        
    def append(self, e:int):
        if self.is_full(): self.resize(len(self.__data)*2)
        self.__lastPos += 1
        self.__data[self.__lastPos] = e
        
    def insert(self, index:int, e:int):
        if self.is_full(): self.resize(len(self.__data)*2)
        if index == self.__lastPos: self.append(e)
        elif index < self.__lastPos and index >= 0:
            temp = np.empty(shape=len(self.__data), dtype=int)
            i, j, prox = 0, 0, False
            while(j <= self.__lastPos):
                j = i - 1
                if i == index:
                    temp[i] = e
                    prox = True
                elif prox: temp[i] = self.__data[j]
                else: temp[i] = self.__data[i]
                i += 1
            self.__lastPos += 1
            self.__data = temp
        else: raise IndexError(f"IndexError: index {index} is out of bounds of MyArray[0, {self.__lastPos}]")
            
    def pop(self, index:int=-1) -> int:
        aux:int = -1
        if self.is_empty(): return aux
        if index == self.__lastPos: return self.pop() # Recursion
        elif index >= 0 and index < self.__lastPos:
            temp = np.empty(shape=len(self.__data), dtype=int)
            i, prox = 0, False
            aux:int = self.__data[index]
            while(i < self.__lastPos):          
                if i == index: 
                    temp[i] = self.__data[i+1]
                    prox = True
                elif prox and not i+1 == self.__lastPos+1: temp[i] = self.__data[i+1]
                else: temp[i] = self.__data[i]
                i +=1
            self.__data = temp
            self.__lastPos -= 1 
        else: 
            aux:int = self.__data[self.__lastPos]
            self.__lastPos -= 1
        if (len(self.__data) >= 10 and self.__lastPos <= len(self.__data) /4): self.resize(len(self.__data)//2)
        return aux
    
    def remove(self, e:int) -> bool:
        if self.is_empty(): return False
        for i in range(self.__lastPos):
            if self.__data[i] == e: 
                temp = np.empty(shape=len(self.__data), dtype=int)
                if i == self.__lastPos: 
                    self.pop()
                    return True
                index, prox = 0, False
                while(index < self.__lastPos):          
                    if index == i: 
                        temp[index] = self.__data[index+1]
                        prox = True
                    elif prox and not index+1 == self.__lastPos+1: temp[index] = self.__data[index+1]
                    else: temp[index] = self.__data[index]
                    index +=1
   
                self.__data = temp
                self.__lastPos -= 1
                return True
        return False
    
    def extend(self, array:Iterable[int]):
        if isinstance(array, Iterable):
            for element in array:
                self.append(element)
    
    def count(self, e:int) -> int:
        if self.is_empty(): return 0
        count = 0
        for element in self.__data:
            if element == e: count += 1
        return count
    
    def index(self, e:int) -> int:
        if self.is_empty(): return -1
        for i in range(self.__len__()):
            if self.__data[i] == e: return i
        return -1
    
    def fill_array_randomly(self):
        self.__lastPos = -1
        for i in range(len(self.__data)):
            self.__data[i] = randint(0, len(self.__data))
            self.__lastPos += 1
            
    def adjust(self):
        if not self.is_empty() or not self.is_full():
            temp = np.empty(shape=self.__len__(), dtype=int)
            for i in range(self.__len__()):
                temp[i] = self.__data[i]
            self.__data = temp
            
    def empty_array(self):
        self.__lastPos = -1
        self.__index = 0
        
    """Complexity O(n^2)"""
    
    def selection_sort(self): # sort by position selection
        for i in range(len(self.__data)):
            min = i # position
            for j in range(i+1, self.__len__()): # posterior position
                if self.__data[j] < self.__data[min]: min = j # updates the position with the lowest value
            temp = self.__data[min] # takes the value of the position with the lowest value
            self.__data[min] = self.__data[i] # exchanges the values ​​of the posterior position with the current 
            self.__data[i] = temp # updates the current position with the lowest value
        
    def insertion_sort(self): # sort using key value insertion
        for i in range(self.__len__()):
            key = self.__data[i] # represents the key value that we are comparing and inserting in the correct place
            j = i - 1 # previous index
            while(j >= 0 and self.__data[j] > key): # as long as the values ​​in previous positions are greater than the key value
                self.__data[j+1] = self.__data[j] # insert the largest values ​​in front of the smallest
                j -= 1
            self.__data[j+1] = key # updates the lowest value
            
    def bubble_sort(self):  # compares pairs of adjacent elements in the array
        for i in range(self.__len__()): 
            for j in range(i+1, self.__len__()-1): 
                if(self.__data[j] > self.__data[j+1]): #  if they are out of order 
                    temp = self.__data[j] #  swaps their positions .
                    self.__data[j] = self.__data[j+1]
                    self.__data[j+1] = temp
                    
    """Complexity O(n log n)"""
    
    def quick_sort(self, first_index: int = 0, last_index: int = -1):
        if last_index == -1: last_index = self.__lastPos
        if first_index < last_index:  # Stop condition
            q = self.__partition(first_index, last_index)  # Partition the array and get the pivot position
            self.quick_sort(first_index, q - 1)  # Sort the left sublist
            self.quick_sort(q + 1, last_index)  # Sort the right sublist
            
    def merge_sort(self, left:int=0, right:int=-1):
        if right == -1: right = self.__len__() -1
        if left < right:
            middle = (left + right) // 2
            # Sort the first and second half of the array
            self.merge_sort(left, middle)  
            self.merge_sort(middle + 1, right)
            # Combines the two ordered halves
            self.__merge(left, middle, right)
    
    """Recursion"""

    def __partition(self, first: int, last: int):
        pivot = self.__data[last]  # Choose the pivot as the last element of the array
        i = first - 1  # Index of smallest element
        for j in range(first, last):  # Partition loop
            if self.__data[j] <= pivot:  # If the current element is less than or equal to the pivot
                i += 1
                # Exchange __data[i] with __data[j]
                self.__data[i], self.__data[j] = self.__data[j], self.__data[i]
        # Place the pivot in the correct position
        i += 1
        self.__data[i], self.__data[last] = self.__data[last], self.__data[i]
        return i  # Return the pivot position

    def __merge(self, left:int, middle:int, right:int):
        # Sub-array sizes
        n1 = middle - left + 1
        n2 = right - middle
        # Temporary arrays to store the elements
        array_l = np.empty(shape=n1, dtype=int)
        array_r = np.empty(shape=n2, dtype=int)
        # Copy __data to temporary arrays 
        for i in range(n1):
            array_l[i] = self.__data[left + i]
        for j in range(n2):
            array_r[j] = self.__data[middle + 1 + j]
        # Starting indices of the subarrays and the combined array
        i, j, k = 0, 0, left
        # Combine the temporary arrays back into the original array
        while i < n1 and j < n2:
            if array_l[i] <= array_r[j]:
                self.__data[k] = array_l[i]
                i += 1
            else:
                self.__data[k] = array_r[j]
                j += 1
            k += 1
        # // Copy the remaining elements of array_l[], if any
        while i < n1:
            self.__data[k] = array_l[i]
            i += 1
            k += 1
        # Copy the remaining elements of array_r[], if any
        while j < n2:
            self.__data[k] = array_r[j]
            j += 1
            k += 1
        
            
        
            