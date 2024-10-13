class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


# Функция добавление нового узла в дерево
def insert(root, node):
    if root is None:
        root = node
    else:
        if root.data < node.data:
            if root.right is None:
                root.right = node
            else:
                insert(root.right, node)
        else:
            if root.left is None:
                root.left = node
            else:
                insert(root.left, node)
    return root

# Функция для вывода на печать всего дерева
def print_tree(node):
    if node is not None:
        print_tree(node.left)
        print(node.data)
        print_tree(node.right)

# Пример использования
root = Node(55)
insert(root, Node(30))
insert(root, Node(70))
insert(root, Node(5))
insert(root, Node(15))
insert(root, Node(25))
insert(root, Node(80))

print_tree(root)
