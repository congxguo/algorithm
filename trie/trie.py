'''
root {'a': nodeA, 'b': nodeB, ...}

nodeA {'x': nodeX, 'y': nodeY, ...}

nodeX {}

example: ax

'''

class TrieTreeNode:
    def __init__(self):
        # the keys of child nodes are stored in the parent node
        self.children = {}
        # used for full match
        self.is_end = False
        
        # for extended use cases
        self.count = 0
        self.key = None
        
        
class TrieTree:
    def __init__(self):
        self.root = TrieTreeNode()
    
    
    # use the structure as index for specific searching
    def search(self, str):
        cur_node = self.root
        # push one node down by each ch in the str if matching, else just return False
        for ch in str:
            if ch not in cur_node.children:
                return False
            cur_node = cur_node.children[ch]
        
        return cur_node.is_end
    
    
    def start_with(self, str):
        cur_node = self.root
        for ch in str:
            if ch not in cur_node.children:
                return False
            cur_node = cur_node.children[ch]
        
        return True
    
    
    # build structure or index gradually
    def insert(self, str):
        cur_node = self.root
        for ch in str:
            if ch not in cur_node.children:
                new_node = TrieTreeNode()
                cur_node.children[ch] = new_node
                cur_node = new_node
                # extended use case
                cur_node.key = ch
            else:
                cur_node = cur_node.children[ch]
                # extended use case

                cur_node.count += 1
        cur_node.is_end = True
            
            
    def print_trie(self):
        self.traverse(self.root, [])
        
    
    def print_nodes(self, path):
        for node in path:
            print(f"{node.key}:{node.count}", end="->")


    def traverse(self, node, path):
        if node.is_end:
            self.print_nodes(path)
            print("")
            
        if node.children:
            for cur_key in node.children:
                path.append(node.children[cur_key])
                self.traverse(node.children[cur_key], path)
                path.pop()
                

trie = TrieTree()
# trie.insert('a')
trie.insert('a')
trie.insert('ab')
trie.insert('bbd')
trie.insert('abc')
# trie.insert('abc')

print('#####################################')
print(f'{trie.start_with('a')}')
print(f'{trie.start_with('c')}')
print('#####################################')
print(f'{trie.search('a')}')
print(f'{trie.search('bb')}')
print('#####################################')
trie.print_trie()