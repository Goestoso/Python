import numpy as np
from random import randint
from typing import Iterable
class MyArray:
    
    CAPACITY = 10
    
    def __init__(self,capacity:int|None=None) -> None: # constructor Overload
        self.__lastPos:int = -1
        if capacity: self.__data = np.empty(shape=capacity, dtype=int)
        else: self.__data = np.empty(shape=self.CAPACITY, dtype=int)
        
    @property
    def lastPos(self):
        return self.__lastPos
    
    @property
    def data(self):
        return self.__data
    
    def __str__(self) -> str: # class Object Override
        if self.is_empty(): return "Array is empty"
        else:
            msg = "My Array: "
            for i in range(self.lastPos+1):
                msg += f"[{self.data[i]}] "
        return msg
    
    def __repr__(self) -> str: # class Object Override
        if self.is_empty(): return "[]"
        else:
            msg = ""
            for i in range(self.lastPos+1):
                msg += f"[{self.data[i]}] "
        return msg
    
    def __eq__(self, object:object):
        if self is object: return True
        if isinstance(object, MyArray):
            if self.lastPos == object.lastPos:
                for i in range(object.lastPos):
                    if self.data[i] != object.data[i]: return False
                return True
        return False

    def is_empty(self) -> bool:
        return self.lastPos == -1
    
    def is_full(self) -> bool:
        return self.lastPos == len(self.data) - 1
    
    def resize(self, new_capacity:int):
        temp = np.empty(shape=new_capacity, dtype=int)
        for i in range(self.lastPos+1):
            temp[i] = self.data[i]
        self.__data = temp
        
    def append(self, e:int):
        if self.is_full(): self.resize(len(self.data)*2)
        self.__lastPos += 1
        self.data[self.lastPos] = e
        
    def insert(self, index:int, e:int):
        if self.is_full(): self.resize(len(self.data)*2)
        if index == self.lastPos: self.append(e)
        elif index < self.lastPos:
            temp = np.empty(shape=len(self.data), dtype=int)
            i, j, prox = 0, 0, False
            while(j <= self.lastPos):
                j = i - 1
                if i == index:
                    temp[i] = e
                    prox = True
                elif prox: temp[i] = self.data[j]
                else: temp[i] = self.data[i]
                i += 1
            self.__lastPos += 1
            self.__data = temp
            
    def pop(self) -> int:
        if self.is_empty(): return -1
        aux:int = self.data[self.lastPos]
        self.__lastPos -= 1
        if (len(self.data) >= 10 and self.lastPos <= len(self.data) /4): self.resize(len(self.data)//2)
        return aux
    
    def remove(self, e:int) -> bool:
        if self.is_empty(): return False
        for i in range(self.lastPos):
            if self.data[i] == e: 
                temp = np.empty(shape=len(self.data), dtype=int)
                if i == self.lastPos: 
                    self.pop()
                    return True
                index, prox = 0, False
                while(index < self.lastPos):          
                    if index == i: 
                        temp[index] = self.data[index+1]
                        prox = True
                    elif prox and not index+1 == self.lastPos+1: temp[index] = self.data[index+1]
                    else: temp[index] = self.data[index]
                    index +=1
   
                self.__data = temp
                self.__lastPos -= 1
                return True
        return False
    
    def extend(self, array:Iterable[int]|'MyArray'):
        if isinstance(array, MyArray):
            for element in array.data:
                self.append(element)
        else:
            for element in array:
                self.append(element)
    
    def count(self, e:int) -> int:
        if self.is_empty(): return 0
        count = 0
        for element in self.data:
            if element == e: count += 1
        return count
    
    def index(self, e:int) -> int:
        if self.is_empty(): return -1
        for i in range(self.lastPos+1):
            if self.data[i] == e: return i
        return -1
    
    def fill_array_randomly(self):
        self.__lastPos = -1
        for i in range(len(self.data)):
            self.data[i] = randint(0, len(self.data))
            self.__lastPos += 1
            
    def adjust(self):
        if not self.is_empty() or not self.is_full():
            temp = np.empty(shape=self.lastPos+1, dtype=int)
            for i in range(self.lastPos+1):
                temp[i] = self.data[i]
            self.__data = temp
            
    def empty_array(self):
        self.__lastPos = -1
        
    """Complexity O(n^2)"""
    
    def selection_sort(self): # sort by position selection
        for i in range(len(self.data)):
            min = i # position
            for j in range(i+1, len(self.data)): # posterior position
                if self.data[j] < self.data[min]: min = j # updates the position with the lowest value
            temp = self.data[min] # takes the value of the position with the lowest value
            self.data[min] = self.data[i] # exchanges the values ​​of the posterior position with the current 
            self.data[i] = temp # updates the current position with the lowest value
        
    def insertion_sort(self): # sort using key value insertion
        for i in range(len(self.data)):
            key = self.data[i] # represents the key value that we are comparing and inserting in the correct place
            j = i - 1 # previous index
            while(j >= 0 and self.data[j] > key): # as long as the values ​​in previous positions are greater than the key value
                self.data[j+1] = self.data[j] # insert the largest values ​​in front of the smallest
                j -= 1
            self.data[j+1] = key # updates the lowest value
            
    def bubble_sort(self):  # compares pairs of adjacent elements in the array
        for i in range(len(self.data)): 
            for j in range(i+1, len(self.data)-1): 
                if(self.data[j] > self.data[j+1]): #  if they are out of order 
                    temp = self.data[j] #  swaps their positions .
                    self.data[j] = self.data[j+1]
                    self.data[j+1] = temp
                    
    """Complexity O(n log n)"""
    
    def __partition(self, first:int, last:int):
        pivot = self.data[last] # Choose the pivot as the last element of the array
        i = first -1 # Index of smallest element
        j = first
        while(j < last): # partition loop
            if self.data[j] <= pivot: # If the current element is less than or equal to the pivot
                i +=1
                # Exchange data[i] with data[j]
                temp = self.data[i]
                self.data[i] = self.data[j]
                self.data[j] = temp
            j+=1
        # Place the pivot in the correct position
        i+=1
        temp = self.data[i]
        self.data[i] = pivot
        self.data[last] = temp
        return i # Return the pivot position
    
    """Recursion"""
                    
    def quick_sort(self, first_index:int=0, last_index:int=-1): 
        if last_index == -1: last_index = len(self.data) -1
        if first_index < last_index:  # stop condition
            q = self.__partition(first_index, last_index) # Partition the array and get the pivot position
            self.quick_sort(first_index, q-1) # Sort the left sublist
            self.quick_sort(q+1, last_index) # // Sort the right sublist
            
    def merge_sort(self, left:int=0, right:int=-1):
        if right == -1: right = len(self.data) -1
        if left < right:
            middle = (left + right) // 2
            # Sort the first and second half of the array
            self.merge_sort(left, middle)  
            self.merge_sort(middle + 1, right)
            # Combines the two ordered halves
            self.__merge(left, middle, right)

    def __merge(self, left:int, middle:int, right:int):
        # Sub-array sizes
        n1 = middle - left + 1
        n2 = right - middle
        # Temporary arrays to store the elements
        array_l = np.empty(shape=n1, dtype=int)
        array_r = np.empty(shape=n2, dtype=int)
        # Copy data to temporary arrays 
        for i in range(n1):
            array_l[i] = self.data[left + i]
        for j in range(n2):
            array_r[j] = self.data[middle + 1 + j]
        # Starting indices of the subarrays and the combined array
        i, j, k = 0, 0, left
        # Combine the temporary arrays back into the original array
        while i < n1 and j < n2:
            if array_l[i] <= array_r[j]:
                self.data[k] = array_l[i]
                i += 1
            else:
                self.data[k] = array_r[j]
                j += 1
            k += 1
        # // Copy the remaining elements of array_l[], if any
        while i < n1:
            self.data[k] = array_l[i]
            i += 1
            k += 1
        # Copy the remaining elements of array_r[], if any
        while j < n2:
            self.data[k] = array_r[j]
            j += 1
            k += 1
        
            
        
            