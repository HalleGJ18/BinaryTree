class BinaryTree:
    name = "" #can name tree
    nodes = [] #stores nodes
    root = None #root node object
    values = [] #stores values of nodes

    def name_tree(self, name):
        self.name = str(name)

    def print_tree(self):
        print("TREE")
        print("value left right parent")
        for i in self.nodes:
            i.print_node()

    def add_node(self, value):
        def compare(node, thing, nodes):
            #print("comparing with... ", node.value)
            if thing < node.value:
                #print("left")
                if node.left == False:
                    node.left = len(nodes)-1
                    nodes[node.left].parent = self.values.index(node.value)
                    #print("node goes here")
                else:
                    #print("compare next node")
                    return compare(nodes[node.left], thing, nodes)
            elif thing > node.value:
                #print("right")
                if node.right == False:
                    node.right = len(nodes)-1
                    nodes[node.right].parent = self.values.index(node.value)
                    #print("node goes here")
                else:
                    #print("compare next node")
                    return compare(nodes[node.right], thing, nodes)

        if value not in self.values:
            self.nodes.append(Node(value))
            self.values.append(value)
            if len(self.nodes) == 1:
                #print("value: ", value)
                #print("this is the root node")
                self.root = self.nodes[0]
                self.nodes[0].parent = False
            else:
                #print("value: ", value)
                compare(self.root, value, self.nodes)

    def search(self, target):
        def check(target, node):
            if target == node.value:
                return True
            elif target > node.value:
                if node.right == False:
                    return False
                else:
                    return check(target, self.nodes[node.right])
            elif target < node.value:
                if node.left == False:
                    return False
                else:
                    return check(target, self.nodes[node.left])

        found = False
        found = check(target, self.root)
        if found == True:
            print("{} is in the tree".format(target))
        else:
            print("{} is not in the tree".format(target))

    def inorder(self, root):
        #LVR
        visited = []
        if self.nodes[root].left != False:
            visited = self.inorder(self.nodes[root].left)
        visited.append(self.values[root])
        if self.nodes[root].right != False:
            visited = visited + self.inorder(self.nodes[root].right)
        return visited

    def preorder(self, root):
        #VLR
        visited = []
        visited.append(self.values[root])
        if self.nodes[root].left != False:
            visited = visited + self.preorder(self.nodes[root].left)
        if self.nodes[root].right != False:
            visited = visited + self.preorder(self.nodes[root].right)
        return visited

    def postorder(self, root):
        #LRV
        visited = []
        if self.nodes[root].left != False:
            visited = visited + self.postorder(self.nodes[root].left)
        if self.nodes[root].right != False:
            visited = visited + self.postorder(self.nodes[root].right)
        visited.append(self.values[root])
        return visited


class Node:
    def __init__(self, value):
        self.left = False #index of left child node in BinaryTree.nodes
        self.right = False #index of right child node in BinaryTree.nodes
        self.value = value
        self.parent = False

    def print_node(self):
        print(self.value, self.left, self.right, self.parent)
