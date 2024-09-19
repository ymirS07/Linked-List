class Node:
    __slots__ = 'prev','next','key','value'
    def __init__(self, key = 0, value = 0):
        self.key = key
        self.value = value

class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.key_to_node = {}
        self.dummy = Node()
        self.tail = Node()
        self.dummy.prev = None
        self.dummy.next = self.tail
        self.tail.prev = self.dummy
        self.tail.next = None
        
    def get_node(self, key: int):
        if key not in self.key_to_node:
            return None
        node = self.key_to_node[key]
        self.remove(node)
        self.push_front(node)
        return node

    def get(self, key: int) -> int:
        node = self.get_node(key)
        return node.value if node else -1
    
    def put(self, key: int, value: int) -> None:
        node = self.get_node(key)
        if node:
            node.value = value
            return
        self.key_to_node[key] = node = Node(key, value)
        self.push_front(node)
        if len(self.key_to_node) > self.capacity:
            back_node = self.tail.prev
            del self.key_to_node[back_node.key]
            self.remove(back_node)
    
    def remove(self, x: Node) -> None:
        x.prev.next = x.next
        x.next.prev = x.prev
    
    def push_front(self, x: Node) -> None:
        x.prev = self.dummy
        x.next = self.dummy.next
        x.prev.next = x
        x.next.prev = x

    def print_list(self):
        current = self.dummy
        while current:
            print(f'Key: {current.key}, Value: {current.value}')
            current = current.next

if __name__ == '__main__':
    lRUCache = LRUCache(2)
    lRUCache.put(1, 1)  #缓存是 {1=1}
    lRUCache.put(2, 2)  #缓存是 {1=1, 2=2}
    lRUCache.print_list()
    lRUCache.get(1)     #返回 1
    lRUCache.put(3, 3)  #该操作会使得关键字 2 作废，缓存是 {1=1, 3=3}
    lRUCache.print_list()
    lRUCache.get(2)     #返回 -1 (未找到)
    lRUCache.put(4, 4)  #该操作会使得关键字 1 作废，缓存是 {4=4, 3=3}
    lRUCache.print_list()
    lRUCache.get(1)     #返回 -1 (未找到)
    lRUCache.get(3)     #返回 3
    lRUCache.get(4)     #返回 4   
