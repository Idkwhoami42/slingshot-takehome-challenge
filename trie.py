class Node:
    def __init__(self):
        self.children = [None]*26
        self.leaf = False
class Trie:
    def __init__(self):
        self.root = Node()
    
    def insert(self, keyword):
        node = self.root
        for i in range(len(keyword)):
            if(node.children[ord(keyword[i])-ord('a')] == None):
                node.children[ord(keyword[i])-ord('a')] = Node()
            node = node.children[ord(keyword[i])-ord('a')]
        node.leaf = True

    def search(self, keyword):
        node = self.root
        for i in range(len(keyword)):
            if(node.children[ord(keyword[i])-ord('a')] == None):
                return False
            node = node.children[ord(keyword[i])-ord('a')]
        return node != None and node.leaf   
    
    def eraseall(self):
        node = self.root
        node.children = [None]*26
        node.leaf = False
    
    def erase(self, keyword):
        if (not self.search(keyword)):
            return
        node = self.root
        path = [node]
        for i in keyword:
            node = node.children[ord(i)-ord('a')]
            path.append(node)
        last = path[-1]
        has_no_child = True
        for i in range(26):
            if(last.children[i] == None):
                has_no_child = False
                break
        if(has_no_child):
            last.leaf = False
            for i in range(len(path) - 2, -1, -1):
                node = path[i]
                count = 0
                for j in range(26):
                    if(node.children[j] != None): count += 1
                if count == 1 and node.children[ord(keyword[i] - ord('a'))].leaf == False:
                    node.children[ord(keyword[i] - ord('a'))] = None
                else: break
        else: 
            last.leaf = False

    def get_keywords(self, curr, node = None):
        keywords = []
        if node == None: node = self.root           
        if node.leaf: keywords.append(curr)     
        for i in range(26):
            if node.children[i] != None:
                keywords.extend(self.get_keywords(curr + chr(i + ord('a')), node.children[i]))
        return keywords
    
    def get_keywords_with_prefix(self, prefix):
        node = self.root
        for i in range(len(prefix)):
            if node.children[ord(prefix[i]) - ord('a')] == None:
                return
            node = node.children[ord(prefix[i]) - ord('a')]
        return self.get_keywords(prefix, node)
