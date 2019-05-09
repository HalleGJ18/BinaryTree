# BinaryTree
Binary Tree written in Python with search, pre-order traversal, in-order traversal and post-order traversal. Has class for BinaryTree and class for Node.

Currently works with numbers in an array only.

## Creating a tree
    ``nums = []  
    tree = BinaryTree()``  

    ``for i in numbers:  
        tree.add_node(i)``   
  
## Print out a readable table to trace tree
shows structure of tree without drawing  
    ``tree.print_tree()``  
### Output
*value of node; left child node; right child node; parent node*  

## Search tree
searches tree for value and says if present or not  
    ``tree.search(value)``  

## In-order traversal
returns array of the values of the nodes in tree when traversed  
    ``tree.inorder(0)`` where 0 is the first node in the tree.values array, which is the root node  
*or can be output*    ``print(tree.inorder(0))``  
syntax the same for the other 2 traversals  
 
## Pre-order traversal
returns array of the values of the nodes in tree when traversed  
    ``tree.preorder(0)``  

## Post-oder traversal
returns array of the values of the nodes in tree when traversed  
    ``tree.postorder(0)``  
