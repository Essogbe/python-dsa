########################
#  LINKED LIST
########################


class Node:
    def __init__(self,dataval):
        self.dataval = dataval
        self.nextval = None
        
        
class SLinkList():
    def __init__(self):
        self.headval=None
        
    def afficher_chaine(self):
        node = self.headval
        while node is not None:
            print(node.dataval)
            node = node.nextval
            
    def add_to_head(self,node):
        """
        Adds a new node to the head of the linked list.

        Parameters:
            node (Node): The node to be added to the head of the linked list.

        Returns:
            None
        """
        if self.headval !=None :
            node.nextval = self.headval
        self.headval= node
        
    def add_to_end(self,endnode):
        """
        Adds a node to the end of the linked list.

        Parameters:
            endnode (Node): The node to be added to the end of the linked list.

        Returns:
            None
        """
        if self.headval == None:
            return False
        
        end= self.headval
        while (end.nextval):
            end = end.nextval
        
        end.nextval = endnode
        
    def add_to_middle(self,middle_leftNode,newNode):
        """
        Add a new node to the middle of the linked list.

        Parameters:
            middle_leftNode (Node): The node in the middle of the linked list where the new node should be added.
            newNode (Node): The new node to be added.
        
        Returns:
            None
        
        Raises:
            ValueError("Cette Node n'est pas 'dans' la LinkedList")
        """
        if middle_leftNode.nextval ==None:
            return ValueError("Cette Node n'est pas 'dans' la LinkedList")
        
        newNode.nextval = middle_leftNode.nextval
        middle_leftNode.nextval = newNode
        
    
    def delete_node(self,to_kill):
        """
        Deletes a node from the linked list.
        
        Parameters:
            to_kill (Node): The node to be deleted.
        
        Returns:
            Node: The deleted node.
        """
        if to_kill ==self.headval:
            self.headval =to_kill.nextval
            return to_kill
        
        previous = self.headval
        while (previous.nextval):
            if previous.nextval == to_kill:
                break
            previous=previous.nextval
                
        if to_kill.nextval == None:
            previous.nextval = None
            return to_kill
        
        else:
            previous.nextval = to_kill.nextval
            return to_kill
            
            
########################
#  ADVANCED LINKED LIST
########################


class AdNode:
    def __init__(self,dataval):
        self.dataval = dataval
        self.nextval = None
        self.previous = None
    
    def __str__(self):
        return str(self.dataval)
            
class ADLinkList():
    def __init__(self):
        self.headval=None
        
    def afficher_chaine(self):
        node = self.headval
        while node is not None:
            print(node.dataval)
            node = node.nextval
            
    def add_to_head(self,node):
      
        node.nextval = self.headval #corr
        if self.headval !=None :
            #node.nextval = self.headval
            self.headval.previous =node
        self.headval = node
        
        
    def add_to_end(self,endnode):
        
        if self.headval == None:
            self.headval = endnode
            endnode.previous = None
        
        end= self.headval
        while (end.nextval):
            end = end.nextval
        
        end.nextval = endnode
        endnode.previous = end
        
    def add_to_middle(self,middle_leftNode,newNode):
        
        if middle_leftNode.nextval ==None:
            return ValueError("Cette Node n'est pas 'dans' la LinkedList")
        
        newNode.nextval = middle_leftNode.nextval
        middle_leftNode.nextval = newNode
        newNode.previous = middle_leftNode
        if newNode.nextval is not None:
            newNode.nextval.previous = newNode
        
    
    def delete_node(self,to_kill):
        
        if to_kill ==self.headval:
            
            self.headval =to_kill.nextval
            to_kill.nextval.previous = None
            
            return to_kill
        
        previous = self.headval
        while (previous.nextval):
            if previous.nextval == to_kill:
                break
            previous=previous.nextval
                
        if to_kill.nextval == None:
            previous.nextval = None
            return to_kill
        
        else:
            previous.nextval = to_kill.nextval
            if to_kill.nextval is not None:
                to_kill.nextval.previous = previous
            return to_kill
        
        
    # def find(self,to_find):
    #     """
    #     Find the given element in the linked list.

    #     Parameters:
    #         to_find (any): The element to search for in the linked list.

    #     Returns:
    #         bool: True if the element is found, False otherwise.
    #     """
    #     obj = self.headval
    #     while(obj):
    #         if obj.data == to_find:
    #             return True
    #         obj= obj.nextval
    #     return False
        
    def __str__(self):
        display = []
        suiv = self.headval
        display.append(str(suiv))
        while suiv.nextval:
            display.append(str(suiv))
            suiv = suiv.nextval
        return "\n".join(display)
        
        
            
            

########################
#  STACK
########################
            
class Stack:
    def __init__(self):
        self.stack = []

     #Use list append method to add new element on the top of the stack
    def on_top(self,value):
        """
        Adds a value to the top of the stack if it is not already in the stack.

        Parameters:
            value (any): The value to be added to the stack.

        Returns:
            bool: True if the value was added to the stack, False otherwise.
        """
        if value not in self.stack:
            self.stack.append(value)
            return True
        else:
            return False
        
    def peek(self):
        """
        Return the top element of the stack without removing it.

        Returns:
            The top element of the stack, or None if the stack is empty.
        """
        if any(self.stack):
            return self.stack.pop()
        else:
            return None
        
        
        
########################
#  QUEUE
########################
            
class Queue:
    def __init__(self):
        self.queue = list()
    
    #Add at the first place
    def push(self,value):
        """
        Push a value to the front of the queue if it is not already in the queue.

        Parameters:
            value: The value to be pushed to the front of the queue.

        Returns:
            True if the value was successfully pushed to the front of the queue, False otherwise.
        """
        if value not in self.queue:
            self.queue.insert(0,value)
            return True
        else:
            return False
        
    #Remove the first element from the Queue
    def remove(self):
        """
        Removes and returns the first element in the queue.

        Returns:
            - If the queue is not empty, the first element in the queue.
            - If the queue is empty, the string "Cannot remove from an empty queue".
        """
        if len(self.queue)>0:
            return self.queue.pop(0)
        else:
            return "Cannot remove from an empty queue"
        
    def size(self):
        return len(self.queue)            


        
########################
#  TREE
########################


class Tree:
    def __init__(self,name):
        self.name =name
        self.parent=None
        self.children= []
    
    def addchild(self,node):
        node.parent = self
        self.children.append(node)
        
        
    def _listwithlevels(self,level,trees):
        """
        Recursively lists the names of the nodes in the tree along with their level.

        Parameters:
            level (int): The current level of the node in the tree.
            trees (list): The list to store the names of the nodes.

        Returns:
            None
        """
        trees.append("==>"*level + self.name)
        for child in self.children:
            child._listwithlevels(level+1,trees)
            
    
    def _find(self,data):
        """
        Finds and returns the node with the specified data in the tree.

        Parameters:
            data (any): The data to search for in the tree.

        Returns:
            Node: The node with the specified data, if found. Otherwise, returns None.
        """
        if self.name==data:
            return self
        
        for child in self.children:
            check=child.find(data)
            if check:
                return check
        return None
  
            
            
     #le plus à gauche       
    def _most_side(self,data,pos=0):
        """
        Find the most side child node with a given data.

        Parameters:
            data (str): The data to search for.
            pos (int, optional): The position of the child node to return if found. Defaults to 0.

        Returns:
            Node or None: The child node with the given data and position, or None if not found.
        """
        if self.name ==data:
            return self.children[pos]
        for child in self.children:
            child.most_left(data,pos)
        return None
            
    def most_left(self,data):
        """
        Returns the most left side of the given data.

        Parameters:
            data: The data to find the most left side of.

        Returns:
            The most left side of the data.
        """
        return self._most_side(data)
    
    def most_right(self,data):
        """
        Returns the rightmost element in the given data.

        Parameters:
            data (list): A list of elements.

        Returns:
            The rightmost element in the data list.
        """
        return self._most_side(data,-1)
    
    def get_parent(self):
        """
        Return the name of the parent of the current object.

        :return: The name of the parent as a string, or None if there is no parent.
        """
        if self.parent:
            return self.parent.name
        return None
    
    def _siblings(self):
        """
        Return a list of siblings of the current node.

        Returns:
            list: A list of sibling nodes.
        """
        if self.parent and self.parent.children:
            index =self.parent.children.index(self)
            return self.parent.children[:index]+self.parent.children[index+1:]
        return None
    
    def siblings(self):
        """
        Returns a list of names of siblings.

        Parameters:
            None.

        Returns:
            list[str] or None: A list of names of siblings if siblings exist, or None if no siblings exist.
        """
        if self._siblings():
            sibling_list =self._siblings()
            sibling_list = sibling_list.copy()
            return [sibling.name for sibling in sibling_list]
        return None
        
    # def get_immediate(self):
    #     if self.parent and self.parent.children :
    #         children=self.parent.children.copy()
    #         index =children.index(self)
    #         immediate={'left':None,'right':None}
    #         if index-1>=0:
    #             immediate['left']=children[index-1].name
    #         if index+1<=len(children)+1:
    #             immediate['right']=children[index+1].name
            
    #         return immediate
    
    #     return None
    
    # def _get_root(self,a):
    #     a.append(self)
    #     if self.children:
            
    #         for child in self.children:
    #             child._get_root(a)
                
        
        
    # def get_root(self):
    #     a=[]
    #     self._get_root(a)
    #     return a[-1].name if a else self.name
        
        
    def delete(self,data):
        """
        Deletes a node from the tree.

        Parameters:
            data (any): The data value of the node to be deleted.

        Returns:
            str or None: The name of the deleted node if it exists, or None if the node does not exist.
        """
        if self.find(data):
            node=self.find(data)
            index=node.parent.children.index(node)
            node.parent.children.pop(index)
            node.parent = None
            return node.name
        return None
            
    def __str__(self):
        trees= []
        self._listwithlevels(0,trees)
        return "\n".join(trees)
    
    
########################
#  BINARY TREE
########################
    
    
class BTree:
    def __init__(self,data):
        self.data=data
        self.parent = None
        self.left =None
        self.right = None
        
    def insert(self,node):
        """
        Insert a node into the binary tree.

        Parameters:
        - node: The node to be inserted into the binary tree.

        Returns:
        None
        """
        if not isinstance(node,BTree):
            node = BTree(node)
            
        if node.data<self.data:
            if self.left ==None:
                self.left = node
            else:
                self.left.insert(node)
            
        elif node.data>self.data:
            if self.right ==None:
                self.right = node
            else:
                self.right.insert(node)
                
        self.data = node.data
        
        
    def printTree(self):
        """
        Prints the elements of the binary tree in an inorder traversal.

        This function recursively prints the elements of the binary tree using an inorder traversal.
        It starts by printing the elements in the left subtree (if it exists), then prints the current node's data,
        and finally prints the elements in the right subtree (if it exists).

        Parameters:
            self (TreeNode): The root of the binary tree.

        Returns:
            None
        """
        if self.left:
            self.left.printTree()
            
        print(self.data)
        if self.right:
            self.right.printTree()
            
        
        
    #Root -> Left -> Right            
    def _preorder(self,root,res):
        """
        Perform a preorder traversal on a binary tree starting from the given root node and append the values to the given result list.

        Parameters:
        - root (Node): The root node of the binary tree.
        - res (List): The list to which the values from the traversal will be appended.

        Returns:
        - None

        """
        
        if self and root:
            res.append(self.data)
            res =res +self._preorder(root.left,res)
            res += self._preorder(root.right,res)
        return res
            
    def preorder(self):
        """
        Returns a list of values obtained by performing a preorder traversal of the binary tree.

        :return: A list of values obtained by performing a preorder traversal of the binary tree.
        :rtype: list
        """
        res=[]
        self._preorder(self,res)
        return res
    
    
    def _postorder(self,root,res):
        """
        Perform a postorder traversal on a binary tree starting from the given root node and append the values to the given result list.

        Parameters:
        - root (Node): The root node of the binary tree.
        - res (List): The list to which the values from the traversal will be appended.

        Returns:
        - None

        """
        
        if self and root:
            res =res +self._postorder(root.left,res)
            res += self._postorder(root.right,res)
            res.append(self.data)
        return res
    def postorder(self):
        """
        Returns a list of values obtained by performing a postorder traversal of the binary tree.

        :return: A list of values obtained by performing a postorder traversal of the binary tree.
        :rtype: list
        """
        res=[]
        self._postorder(self,res)
        return res
    
    #Left -> Root -> Right
    def _inorder(self,root,res):
        """
        Perform an inorder traversal on a binary tree starting from the given root node and append the values to the given result list.

        Parameters:
        - root (Node): The root node of the binary tree.
        - res (List): The list to which the values from the traversal will be appended.

        Returns:
        - None

        """
        
        if self and root:
            res =res +self._inorder(root.left,res)
            res.append(self.data)
            res += self._inorder(root.right,res)
        return res
    def inorder(self):
        """
        Returns a list of values obtained by performing an inorder traversal of the binary tree.

        :return: A list of values obtained by performing an inorder traversal of the binary tree.
        :rtype: list
        """
        res=[]
        self._inorder(self,res)
        return res
    #
    def breadthfirst(self):
        """
        Perform a breadth-first search traversal on the binary tree starting from the current node.
        
        Returns:
            res (List): A list containing the values of all the nodes in the binary tree, traversed in breadth-first order.
        """
        
        res = []
        if self is None:
            return res
        
        file =[]
        file.append(self)
        while (len(file) >0):
            #consigner la valeur dans la liste res et retirer le premier ele;ent
            res.append(file[0].data)
            node = file.pop(0)
            #ajouter l enfant gauche 
            if node.left is not None:
                file.append(node.left)
            
            #ajouter l enfant droit 
            if node.right is not None:
                file.append(node.right)
        return res
    
    def sizeTree(self,root):
        """
        Calculates the size of a binary tree.

        Parameters:
            root (TreeNode): The root of the binary tree.

        Returns:
            int: The size of the binary tree.
        """
        if root is None:
            return 0
        else:
            return 1+self.sizeTree(root.left) + self.sizeTree(root.right)
        
    def height(self,root):
        """
        Calculate and return the height of a binary tree.

        Parameters:
        - root: The root node of the binary tree (Node)

        Returns:
        - The height of the binary tree (int)
        """
        if root is None:
            return 0
        else:
            return 1+max(self.height(root.left), self.height(root.right))
            
            
        
    
    def __str__(self):
        return str(self.breadthfirst())
    
    
    
    
    

