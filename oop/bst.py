class Node:
    
    @property
    def info(self):
        return self.__info
    
    @info.setter
    def info(self, new_info:int):
        self.__info = new_info
        
    @property
    def left(self) -> 'Node|None':
        return self.__left
    
    @left.setter
    def left(self, new_left:'Node'):
        self.__left = new_left
        
    @property
    def right(self) -> 'Node|None':
        return self.__right
    
    @right.setter
    def right(self, new_right:'Node'):
        self.__right = new_right
    
    def __init__(self, info:int):
        self.__info: int = info
        self.__left: Node|None = None
        self.__right: Node|None = None
        
    def __str__(self) -> str:
        return f"[{self.info}]"
    
class BST:
    
    @property
    def empty(self) -> bool:
        try:
            self.root
        except AttributeError:
            return True
        else:
            return False
    
    @property
    def root(self) -> Node:
        return self.__root
    
    def search(self, x:int) -> bool:
        if self.empty: return False
        elif x == self.root.info: return True
        else: return self.__search(x, self.root)
        
    def __search(self, target:int, current:Node) -> bool:
        if current is None: return False
        elif current.info == target: return True
        elif target < current.info: return self.__search(target, current.left) # type: ignore
        else: return self.__search(target, current.right) # type: ignore
        
    def insert(self, x:int):
        new = Node(x)
        if self.empty: self.__root = new
        else: self.__insert(new,self.root)
        
    def __insert(self, new:Node, current:Node):
        if new.info <= current.info: # goes to the left
            if current.left is None: current.left = new
            else: self.__insert(new, current.left)
        else: # goes to the right
            if current.right is None: current.right = new
            else: self.__insert(new, current.right)
            
    def remove(self, x:int) -> int:
        if self.empty or not self.search(x): return -1
        self.__remove(x, self.root)
        return x
    
    def __remove(self, target:int, current:Node):
        if target < current.info: current.left = self.__remove(target, current.left) # type: ignore
        elif target > current.info: current.right = self.__remove(target, current.right) # type: ignore
        else:
            if current.left is None and current.right is None: return None
            elif current.left is None: return current.right
            elif current.right is None: return current.left
            else:
                sucessor = self.__find_min(current.right)
                current.info = sucessor.info
                current.right = self.__remove(sucessor.info, current.right) # type: ignore
        return current
    
    def __find_min(self, node:Node) -> Node:
        while node.left is not None:
            node = node.left
        return node
            
    def nodes(self) -> int:
        if self.empty: return 0
        else: return self.__nodes(self.root)
            
    def __nodes(self, current:Node|None) -> int:
        if current == None: return 0
        return self.__nodes(current.left) + 1 + self.__nodes(current.right)
    
    def min(self) -> int:
        if self.empty: return -1
        aux = self.root
        while(aux.left is not None): # type: ignore
            aux = aux.left
        return aux.info # type: ignore
        
    def max(self) -> int:
        if self.empty: return -1
        aux = self.root
        while(aux.right is not None): # type: ignore
            aux = aux.right
        return aux.info # type: ignore
    
    def __repr__(self) -> str:
        if self.empty: return ""
        else: return self.__repr_in_order(self.root)
        
    def __repr_in_order(self, current:Node|None) -> str:
        if current is None: return ""
        return self.__repr_in_order(current.left) + str(current) + " " + self.__repr_in_order(current.right)
    
    def __str__(self) -> str:
        if self.empty:
            return "Empty"
        return self.__display_str(self.root, 0)

    def __display_str(self, node, level):
        if node is None: return ""
        right_str = self.__display_str(node.right, level + 1)
        current_str = str(' ' * 4 * level + '-> ' + str(node.info))
        left_str = self.__display_str(node.left, level + 1)
        return right_str + "\n" + current_str + "\n" + left_str

        
if __name__ == "__main__":
    tree = BST()
    tree.insert(100)
    tree.insert(75)
    tree.insert(120)
    tree.insert(25)
    tree.insert(115)
    tree.insert(15)
    tree.insert(45)
    tree.insert(90)
    tree.insert(99)
    tree.insert(110)
    tree.insert(150)
    tree.insert(10)
    tree.insert(20)
    tree.insert(175)
    print(tree)
    print(tree.min())
    print(tree.max())
    print(tree.nodes())
    print(tree.search(120))
    print(tree.remove(75))
    print(tree)