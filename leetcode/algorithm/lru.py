from typing import Optional


# 力扣 146
class Node:
    def __init__(self, key: int, val: int):
        self.key = key
        self.value = val
        self.prev = None
        self.next = None


class DoubleList:
    def __init__(self):
        self.head = Node(0, 0)
        self.tail = Node(0, 0)
        self.head.next = self.tail
        self.tail.prev = self.head
        self.size = 0

    def add_last(self, x: Node) -> None:
        x.prev = self.tail.prev
        x.next = self.tail
        self.tail.prev.next = x
        self.tail.prev = x
        self.size += 1

    def remove_first(self) -> Optional[Node]:
        if self.head.next is self.tail:
            return None
        first_node = self.head.next
        self.remove(first_node)
        return first_node

    def remove(self, x: Node) -> None:
        x.prev.next = x.next
        x.next.prev = x.prev
        self.size -= 1

    def get_size(self) -> int:
        return self.size


class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.map = {}
        self.double_list = DoubleList()

    def get(self, key: int) -> int:
        if key not in self.map:
            return -1
        self.make_recently(key)
        return self.map[key].value

    def put(self, key: int, value: int) -> None:
        if key in self.map:
            x = self.map[key]
            self.double_list.remove(x)
            self.add_recently(key, value)
            return
        if self.capacity == self.double_list.get_size():
            self.remove_least_recently()
        self.add_recently(key, value)

    def make_recently(self, key: int) -> None:
        x = self.map[key]
        self.double_list.remove(x)
        self.double_list.add_last(x)

    def add_recently(self, key: int, value: int) -> None:
        x = Node(key, value)
        self.double_list.add_last(x)
        self.map[key] = x

    def remove_least_recently(self) -> None:
        x = self.double_list.remove_first()
        self.map.pop(x.key)


"""
调用 API
from collections import OrderedDict

class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = OrderedDict()

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        # 访问后将元素移到末尾，表示最近使用
        self.cache.move_to_end(key)
        return self.cache[key]

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            # 若键已存在，先删除，再插入以更新顺序
            del self.cache[key]
        elif len(self.cache) >= self.capacity:
            # 超出容量时删除最早的元素
            self.cache.popitem(last=False)
        self.cache[key] = value
"""
