class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None


def search(root, key):
    while root is not None:

        if key > root.key:
            root = root.right
        elif key < root.key:
            root = root.left

        else:
            return root

    return None


if __name__ == "__main__":
    root = Node(50)
    root.left = Node(30)
    root.right = Node(70)
    root.left.left = Node(20)
    root.left.right = Node(40)
    root.right.left = Node(60)
    root.right.right = Node(80)

    print("Found" if search(root, 19) else "Not Found")
    print("Found" if search(root, 80) else "Not Found")
