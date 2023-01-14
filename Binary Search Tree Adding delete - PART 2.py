print(f'{"*** Programmed by ***": ^40}')
print(f'{"*** Nicolas Fabillar ***": ^40}')

class BinarySearchTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def add_child(self, data):
        if data == self.data:
            return # node already exist

        if data < self.data:
            if self.left:
                self.left.add_child(data)
            else:
                self.left = BinarySearchTreeNode(data)
        else:
            if self.right:
                self.right.add_child(data)
            else:
                self.right = BinarySearchTreeNode(data)


    def search(self, val):
        if self.data == val:
            return True

        if val < self.data:
            if self.left:
                return self.left.search(val)
            else:
                return False

        if val > self.data:
            if self.right:
                return self.right.search(val)
            else:
                return False

    def in_order_traversal(self):
        elements = []
        if self.left:
            elements += self.left.in_order_traversal()

        elements.append(self.data)

        if self.right:
            elements += self.right.in_order_traversal()

        return elements

    def find_min(self): #finds minimum element in entire binary tree.
        if self.left is None:
            return self.data
        return self.left.find_min()

    def find_max(self): # finds maximum element in entire binary tree.
        if self.right is None:
            return self.data
        return self.right.find_max()

    def calculate_sum(self): # calcualtes sum of all elements
        elements = self.in_order_traversal()
        Total_Value = 0
        for i in range(len(elements)):
            Total_Value += elements[i]

        return Total_Value

    def post_order_traversal(self): #performs post order traversal of a binary tree
        elements = []
        # Visit the left side first.
        if self.left:
            elements += self.left.post_order_traversal()

        # Visit the right side second.
        if self.right:
            elements += self.right.post_order_traversal()

        # Visit the node last.
        elements.append(self.data)

        return elements

    def pre_order_traversal(self): #performs pre order traversal of a binary tree
        elements = []

        # Visit the node first.
        elements.append(self.data)

        # Visit the left side second.
        if self.left:
            elements += self.left.pre_order_traversal()

        # Visit the right side last.
        if self.right:
            elements += self.right.pre_order_traversal()

        return elements

    def delete(self, val):
        if val < self.data:
            if self.left:
                self.left = self.left.delete(val)
        elif val > self.data:
            if self.right:
                self.right = self.right.delete(val)
        else:
            if self.left is None and self.right is None:
                return None
            elif self.left is None:
                return self.right
            elif self.right is None:
                return self.left

            max_val = self.left.find_max()
            self.data = max_val
            self.left = self.left.delete(max_val)

        return self

def build_tree(elements):
    print("Building tree with these elements:",elements)
    root = BinarySearchTreeNode(elements[0])

    for i in range(1,len(elements)):
        root.add_child(elements[i])

    return root

if __name__ == '__main__':
    name_tree = build_tree(["n", "i", "c", "o", "l", "a", "s", "a", "l", "e", "x", "a",
                           "n", "d", "e", "r", "a", "f", "a", "b", "i", "l", "l", "a", "r"])
    print("\nIn order traversal gives this sorted list:", name_tree.in_order_traversal())
    name_tree.delete("a")
    print("After deleting a ", name_tree.in_order_traversal()) # a should be removed
    name_tree.delete("d")
    print("After deleting d ", name_tree.in_order_traversal())  # d should be removed
    name_tree.delete("x")
    print("After deleting x ", name_tree.in_order_traversal())  # x should be removed


    print()
    numbers_tree = build_tree([17, 4, 3, 20, 18, 30, 29, 9, 23, 18, 34, 55, 70])
    print("\nIn order traversal gives this sorted list:", numbers_tree.in_order_traversal())
    numbers_tree.delete(17)
    print("After deleting 17", numbers_tree.in_order_traversal())  # 17 should be removed
    numbers_tree.delete(3)
    print("After deleting 3 ", numbers_tree.in_order_traversal())  # 3 should be removed
    numbers_tree.delete(34)
    print("After deleting 34", numbers_tree.in_order_traversal())  # 70 should be removed
