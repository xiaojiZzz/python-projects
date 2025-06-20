"""
LRU 缓存
请你设计并实现一个满足  LRU (最近最少使用) 缓存 约束的数据结构。
实现 LRUCache 类：
LRUCache(int capacity) 以 正整数 作为容量 capacity 初始化 LRU 缓存
int get(int key) 如果关键字 key 存在于缓存中，则返回关键字的值，否则返回 -1 。
void put(int key, int value) 如果关键字 key 已经存在，则变更其数据值 value ；如果不存在，则向缓存中插入该组 key-value 。
如果插入操作导致关键字数量超过 capacity ，则应该 逐出 最久未使用的关键字。
函数 get 和 put 必须以 O(1) 的平均时间复杂度运行。
示例：
输入
["LRUCache", "put", "put", "get", "put", "get", "put", "get", "get", "get"]
[[2], [1, 1], [2, 2], [1], [3, 3], [2], [4, 4], [1], [3], [4]]
输出
[null, null, null, 1, null, -1, null, -1, 3, 4]
解释
LRUCache lRUCache = new LRUCache(2);
lRUCache.put(1, 1); // 缓存是 {1=1}
lRUCache.put(2, 2); // 缓存是 {1=1, 2=2}
lRUCache.get(1);    // 返回 1
lRUCache.put(3, 3); // 该操作会使得关键字 2 作废，缓存是 {1=1, 3=3}
lRUCache.get(2);    // 返回 -1 (未找到)
lRUCache.put(4, 4); // 该操作会使得关键字 1 作废，缓存是 {4=4, 3=3}
lRUCache.get(1);    // 返回 -1 (未找到)
lRUCache.get(3);    // 返回 3
lRUCache.get(4);    // 返回 4
提示：
1 <= capacity <= 3000
0 <= key <= 10000
0 <= value <= 105
最多调用 2 * 105 次 get 和 put
"""
from typing import Optional


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
