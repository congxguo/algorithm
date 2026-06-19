'''
root {'a': nodeA, 'b': nodeB, ...}

nodeA {'x': nodeX, 'y': nodeY, ...}

nodeX {}

example: ax

'''

class TrieTreeNode:
    def __init__(self):
        self.children = {}
        self.is_end = False
        

class TrieTree:
    def __init__(self):
        self.root = TrieTreeNode()
    
    
    def search(self, str):
        cur_node = self.root
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
    
    
    def insert(self, str):
        cur_node = self.root
        for ch in str:
            # print(f'ch={ch}')
            if ch not in cur_node.children:
                new_node = TrieTreeNode()
                cur_node.children[ch] = new_node
                cur_node = new_node
            else:
                cur_node = cur_node.children[ch]
        cur_node.is_end = True
            
    def print_trie(self):
        self.traverse(self.root, [])
        

    def traverse(self, node, path):
        if node.is_end:
            print(f'path={path}')
            
        if node.children:
            for cur_key in node.children:
                path.append(cur_key)
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