# -*- codeing: uft-8 -*-
""""Trie Algorithm Implementation."""


class Trie(object):
    """Trie class."""

    def __init__(self):
        """Initialize the trie."""
        self.root = {}

    def insert(self, token):
        """Insert a token into the Trie."""
        if not token:
            return None
        else:
            current = self.root
            for char in token.lower():
                current = current.setdefault(char, {})
            current["$"] = "$"

    def contains(self, token):
        """"Check to see if a token is contain in the Trie."""
        current = self.root
        for char in token:
            if char in current:
                current = current[char]
            else:
                return False
        return "$" in current

    def traversal(self, start=None, word=''):
        """Traverse a Trie from a designated start place."""
        if start is None:
            start = self.root
        elif self.contains(start):
            pass  # this would be where autocomplete would go
        for key in start:
            if key == '$':
                yield word
            else:
                for more_letters in self.traversal(start[key], word + key):
                    yield more_letters
        # print(start)
        # lst = []
        # for key in start:
        #     lst.append(key)
        #     if key != '$':
        #         lst += self.traversal(start[key])
        # yield lst



if __name__ == '__main__':
    t = Trie()
    t.insert("cat")
    t.insert("cats")
    t.insert("dog")
    # t.insert("at")
    # print(t.contains("at"))
    for i in t.traversal():
        print(i)
    print(t.traversal(t.root))