class Node:
    def init(self, data):
        self.data = data
        self.kiri = None
        self.kanan = None

class Tree():
    def init(self, data):
        self.root = Node(data)
    def print_tree(self):
        return self.preorder_print(self.root, "")
    def preorder_print(self, start, tranversal):
        if start:
            tranversal += (str(start.data)+" >> ")
            tranversal = self.preorder_print(start.kiri, tranversal)
            tranversal = self.preorder_print(start.kanan, tranversal)
        return tranversal
        
if __name__ == 'main':
    tree = Tree()
    menu = int(input("""
    ___

       ^^^^^^^^^^^^ Tree  MENU ^^^^^^^^^^^^^
     1. Input Root                              
     2. Input Child                            
     3. Dis Tree dengan Pre-Order Tranversal|

    ___
    0. Keluar.
    Pilih menu : """))