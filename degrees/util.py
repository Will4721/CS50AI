class Node():
    def __init__(self, state, parent, action):
        self.state = state
        self.parent = parent
        self.action = action


class StackFrontier():
    def __init__(self):
        self.frontier = []

    def add(self, node):
        self.frontier.append(node)

    def contains_state(self, state):
        return any(node.state == state for node in self.frontier)

    def empty(self):
        return len(self.frontier) == 0

    def remove(self):
        if self.empty():
            raise Exception("empty frontier")
        else:
            node = self.frontier[-1]
            self.frontier = self.frontier[:-1]
            return node


class QueueFrontier(StackFrontier):

    def remove(self):
        if self.empty():
            raise Exception("empty frontier")
        else:
            node = self.frontier[0]
            self.frontier = self.frontier[1:]
            return node


class HashTable:
    def __init__(self, size):
        self.size = size
        self.hash_table = [[] for _ in range(size)]

    def set_val(self, key, val):
        hashed_key = hash(key) % self.size
        bucket = self.hash_table[hashed_key]

        for index, (record_key, _) in enumerate(bucket):
            if record_key == key:
                bucket[index] = (key, val)
                return
        bucket.append((key, val))

    def get_val(self, key):
        hashed_key = hash(key) % self.size
        bucket = self.hash_table[hashed_key]

        for record_key, record_val in bucket:
            if record_key == key:
                return record_val
        return "No record found"

    def delete_val(self, key):
        hashed_key = hash(key) % self.size
        bucket = self.hash_table[hashed_key]

        for index, (record_key, _) in enumerate(bucket):
            if record_key == key:
                bucket.pop(index)
                return

    def __str__(self):
        return "".join(str(bucket) for bucket in self.hash_table)
