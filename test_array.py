from my_array import MyArray, union
from time import time

array = MyArray()
array.fill_array_randomly()
print("First array:")
print(array)
array.append(1)
print(repr(array))
array.insert(0,0)
print(repr(array))
print(f"Element 3 appeared {array.count(3)} time(s).")
print(f"The {array.pop()} element has been removed.")
print(f"The index of element 5 is {array.index(5)}.")
other_array = MyArray(20)
other_array.fill_array_randomly()
print("Other array:")
print(repr(other_array))
print("Using del to remove by index...")
del other_array[5]
print(repr(other_array))
array.extend(other_array)
print("Extending the array with other iterables...")
print(array)
print(f"Size of extended array: {array.capacity}")
print("Adjusting...")
array.adjust()
print(f"Size of adjusted array: {array.capacity}")
print("Concatenating array:")
array = array + array
print(array)
print("Multiplying array:")
arrays = array * 2
print(arrays)
print("Using the first copy array:")
array1 = arrays[0]
print(array1)
print("Dividing array:")
print(len(array))
arrays = array / 10
print(arrays)
print("Using the last slice:")
last_array = arrays[len(arrays)-1]
print(last_array)
print("Joining the arrays:")
print(union(arrays))
array1 = MyArray()
array1.extend([1,2,3,4,5,6,7,8,9,10])
array2 = MyArray()
array2.extend([1,2,3,4,5,6,7,8,9,10])
print(f"Checking if array1 is equal to array2: {array1 == array2}")
print(f"Checking if array1 is equal to array1: {array1 == array1}")
array1.insert(0,0)
print("New comparing:")
print(repr(array1))
print(repr(array2))
print(f"Checking if array1 is greater than array2: {array1 > array2}, because {len(array1)} is greater than {len(array2)}.")
print("New comparing:")
print(f"Element {array1.pop()} has been removed from array1.")
print(f"Element {array1.pop(index=0)} has been removed from array1.")
array2.insert(0,0)
print(repr(array1))
print(repr(array2))
print(f"Checking if array1 is less than array2: {array1 < array2}, because {len(array1)} is less than {len(array2)}.")
print(f"Max value of array1 is {max(array1)}")
print(f"Max value of array2 is {max(array2)}")
print(f"Min value of array1 is {min(array1)}")
print(f"Min value of array2 is {min(array2)}")
array = MyArray(5)
array.extend([1,2,3,4,5])
print(array)
print(f"Reversed array: {reversed(array)}")
big_array = MyArray(10000)
print("Big array:")
big_array.fill_array_randomly()
print("Selection sort:")
start = time()
big_array.selection_sort()
end = time()
print(f"Duration: {end - start:.4f} secs.")
big_array.fill_array_randomly()
print("Insertion sort:")
start = time()
big_array.insertion_sort()
end = time()
print(f"Duration: {end - start:.4f} secs.")
big_array.fill_array_randomly()
print("Bubble sort:")
start = time()
big_array.bubble_sort()
end = time()
print(f"Duration: {end - start:.4f} secs.")
big_array.fill_array_randomly()
print("Quick sort:")
start = time()
big_array.quick_sort()
end = time()
print(f"Duration: {end - start:.4f} secs.")
big_array.fill_array_randomly()
print("Merge sort:")
start = time()
big_array.merge_sort()
end = time()
print(f"Duration: {end - start:.4f} secs.")