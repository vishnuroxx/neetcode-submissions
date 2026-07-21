class PrefixTree:
    def __init__(self):
        self.children = [None] * 26
        self.isLast = False

    def insert(self, word: str) -> None:
        curr = self
        i = 0
        
        while i < len(word) and curr.children[ord(word[i]) - 97]:
            curr = curr.children[ord(word[i]) - 97]
            i += 1
        
        if i < len(word):
            #insert 
            for ch in word[i:]:
                curr.children[ord(ch) - 97] = PrefixTree()

                if ch == word[-1]: # last element  
                    curr.children[ord(ch) - 97].isLast = True

                curr = curr.children[ord(ch) - 97] # go to next element
        else:
            curr.isLast = True

    def search(self, word: str) -> bool:
        curr = self
        for ch in word:
            if not curr:
                return False
            else:
                curr = curr.children[ord(ch) - 97]

        if curr and curr.isLast:
            return True
        else:
            return False    


    def startsWith(self, prefix: str) -> bool:
        curr = self
        for ch in prefix:
            if not curr:
                return False
            else:
                curr = curr.children[ord(ch) - 97]

        if curr:
            return True
        else:
            return False    
        
        