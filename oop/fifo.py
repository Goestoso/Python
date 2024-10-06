from linked_lists import DoubleNode, Iterable

class Queue:
    
    @property
    def front(self):
        return self.__front
    
    @property
    def rear(self):
        return self.__rear
    
    @property
    def empty(self):
        return self.front == None
    
    @staticmethod
    def copy(queue:'Queue'):
        if queue.empty: return None
        fifo, aux = Queue(), queue.rear
        while(aux != None):
            fifo.enqueue(aux.info)
            aux = aux.previous
        return fifo
    
    @staticmethod
    def enqueue_queues(queue:'Queue', other_queue:'Queue'):
        if queue.empty and other_queue.empty: return None
        fifo = Queue()
        while(queue or other_queue):
            if not queue.empty: fifo.enqueue(queue.dequeue())
            if not other_queue.empty: fifo.enqueue(other_queue.dequeue())
        return fifo

    
    def __init__(self, iterable:Iterable[object]|None = None) -> None:
        self.__front = None
        self.__rear = None
        if iterable:
            for value in iterable:
                self.enqueue(value)
        
    def __len__(self):
        if self.empty: return 0
        aux, count = self.front, 0
        while(aux != None):
            aux = aux.next
            count +=1
        return count
    
    def __str__(self) -> str:
        temp = "Queue: "
        if self.empty: return temp + "is empty"
        aux = self.front
        while(aux != None):
            temp += str(aux)
            aux = aux.next
        temp += "\\\\"
        return temp
    
    def __repr__(self) -> str:
        temp = ""
        if self.empty: return "None"
        aux = self.front
        while(aux != None):
            temp += str(aux)
            aux = aux.next
        temp += " None"
        return temp    
    
    def clear(self):
        self.__front = None
        self.__rear = None
        
    def enqueue(self, value:object):
        aux = DoubleNode(value)
        if self.empty:
            self.__front = aux
            self.__rear = aux
        else:
            aux.next = self.front
            self.front.previous = aux # type: ignore
            self.__front = aux
            
    def dequeue(self) -> object:
        if self.empty: raise TypeError("TypeError: cannot dequeue None, the Queue is empty!")
        if not self.rear.previous: # type: ignore 
            temp = self.rear.info # type: ignore 
            self.__front = None
            self.__rear = None
            return temp
        temp = self.rear.info # type: ignore
        self.__rear = self.rear.previous # type: ignore
        self.rear.next = None # type: ignore 
        return temp
        
if __name__ == '__main__':
    queue = Queue()
    queue.enqueue(0)
    queue.enqueue(1)
    queue.enqueue(2)
    queue.enqueue(3)
    queue.enqueue(4)
    queue.enqueue(5)
    print(queue)
    print(queue.dequeue())
    print(queue)
    print(len(queue))
    fifo = Queue([5,4,3,2,1])
    print([5,4,3,2,1])
    print(f"Queued Iterable: {repr(fifo)}")
    copy = Queue.copy(queue)
    print(f"Copy Queue: {repr(queue)}")
    other_copy = Queue.copy(fifo)
    print(f"Other Copy Queue: {repr(fifo)}")
    enqueue_queues = Queue.enqueue_queues(copy, other_copy) # type: ignore
    print(f"Enqueued Queues: {repr(enqueue_queues)}")
    