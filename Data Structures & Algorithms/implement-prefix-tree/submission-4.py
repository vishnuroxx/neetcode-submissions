class PrefixTree:
    def __init__(self):
        self.children = [None] * 26
        self.isLast = False

    def insert(self, word: str) -> None:
        curr = self

        for ch in word: 
            if not curr.children[ord(ch) - 97]:
                curr.children[ord(ch) - 97] = PrefixTree()
            curr = curr.children[ord(ch) - 97]

        curr.isLast = True 

    def search(self, word: str) -> bool:
        curr = self
        for ch in word:
            if not curr.children[ord(ch) - 97]:
                return False
            curr = curr.children[ord(ch) - 97]

        if curr.isLast:
            return True
        else:
            return False    


    def startsWith(self, prefix: str) -> bool:
        curr = self

        for ch in prefix:
            if not curr.children[ord(ch) - 97]:
                return False
            curr = curr.children[ord(ch) - 97]

        return True
        
        