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
        return self.in_order_traversal()[0]

    def find_max(self): # finds maximum element in entire binary tree.
        return self.in_order_traversal()[-1]

    def calculate_sum(self): # calcualtes sum of all elements
        elements = self.in_order_traversal()
        Total_Value = 0
        for i in range(len(elements)):
            Total_Value += elements[i]

        return Total_Value


def build_tree(elements):
    print("Building tree with these elements:",elements)
    root = BinarySearchTreeNode(elements[0])

    for i in range(1,len(elements)):
        root.add_child(elements[i])

    return root

if __name__ == '__main__':
    numbers_tree = build_tree([17, 4, 3, 20, 18, 30, 29, 9, 23, 18, 34, 55, 70])
    print("\nIn order traversal gives this sorted list:",numbers_tree.in_order_traversal())
    print("The minimum element in the list is:",numbers_tree.find_min())
    print("The maximum element in the list is:", numbers_tree.find_max())
    print("The total value of the elemets are:", numbers_tree.calculate_sum())