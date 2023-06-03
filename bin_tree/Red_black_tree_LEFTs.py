class Node:
    def __init__(self, value: int):
        self.value = value
        self.color = True  # True = RED, False = BLACK
        self.left = self.right = None


class RedBlackTree:
    def __init__(self):
        self.root = None

    def insert(self, value: int) -> None:
        self.root = self.__insert(self.root, value)
        self.root.color = False  # Корень всегда черный

    def __insert(self, root: Node, value: int) -> Node:
        if root is None:
            return Node(value)

        if value < root.value:
            root.left = self.__insert(root.left, value)
        elif value > root.value:
            root.right = self.__insert(root.right, value)
        else:
            root.value = value

        if self.is_red(root.right) and not self.is_red(root.left):
            root = self.rotate_left(root)
        if self.is_red(root.left) and self.is_red(root.left.left):
            root = self.rotate_right(root)
        if self.is_red(root.left) and self.is_red(root.right):
            self.flip_color(root)

        return root

    @staticmethod
    def is_red(node: Node) -> bool:
        if node is None:
            return False
        return node.color

    def flip_color(self, node: Node) -> None:
        node.color = True
        node.left.color = False
        node.right.color = False

    def rotate_left(self, node: Node) -> Node:
        new_root = node.right
        node.right = new_root.left
        new_root.left = node

        new_root.color = node.color
        node.color = True

        return new_root

    def rotate_right(self, node: Node) -> Node:
        new_root = node.left
        node.left = new_root.right
        new_root.right = node

        new_root.color = node.color
        node.color = True

        return new_root

    def print_tree(self) -> None:
        self.__print_tree_recursive(self.root, "", True)

    def __print_tree_recursive(self, node: Node, indent: str, is_left: bool) -> None:
        if node is None:
            return

        marker = "L-- "
        if not is_left:
            marker = "`-- "

        color = " (R)" if node.color else " (B)"
        print(indent + marker + str(node.value) + color)

        self.__print_tree_recursive(node.left, indent + "|   ", True)
        self.__print_tree_recursive(node.right, indent + "    ", False)


def main():
    tree = RedBlackTree()
    tree.insert(1)
    tree.insert(5)
    tree.insert(30)
    tree.insert(2)
    tree.insert(53)
    tree.insert(25)
    tree.print_tree()


if __name__ == "__main__":
    main()
