'''
A class of how to implement your own hashmap in python
@author Carolyn Ryan

https://www.youtube.com/watch?v=9HFbhPscPU0
'''
class HashMap:
    def __init__(self, n):
        self.size = n
        self.map = [None] * self.size

    def _get_hash_index(self, key):
        hash = 0
        for char in str(key):
            hash += ord(char)
        return hash % self.size

    def add(self, key, value):
        key_index = self._get_hash_index(key)
        key_val = [key, value]

        if self.map[key_index] is None:
            self.map[key_index] = [key_val]
            return True
        else:
            for kv_pair in self.map[key_index]:
                if kv_pair[0] == key and kv_pair[1] == value:
                    return True
                self.map[key_index].append(key_val)
                return True

    def get(self, key):
        key_index = self._get_hash_index(key)
        possible_vals = self.map[key_index]
        if possible_vals:
            for kv_pair in possible_vals:
                if kv_pair[0] == key:
                    return kv_pair[1]

        return None

    def delete(self, key):
        key_index = self._get_hash_index(key)
        possible_vals = self.map[key_index]
        if not possible_vals:
            return False
        else:
            new_pairs = []
            for kv_pair in possible_vals:
                if kv_pair[0] != key:
                    new_pairs.append(kv_pair)
            self.map[key_index] = new_pairs

    def is_empty(self):
        for pairs in self.map:
            if pairs:
                return False
        else:
            return True

    def __str__(self):
        if self.is_empty():
            return '{}'

        s = '{'
        for pairs in self.map:
            if pairs:
                for pair in pairs:
                    s += '{}:{}, '.format(pair[0], pair[1])
        return s[:-2] + "}"


def main():
    h = HashMap(100)
    print(h)
    h.add('Bob', 12.3)
    h.add('Carolyn', 4.894)
    print(h)
    print(h.get("Bob"))
    print(h.get("Bob11"))
    h.delete('Bob')
    print(h)

main()