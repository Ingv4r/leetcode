class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def make_tree(i, nodes):
    if i <= nodes:
        return TreeNode(
            i,
            left=make_tree(i * 2, nodes),
            right=make_tree((i * 2) + 1, nodes)
        )


def preorder(node):
    if node is None:
        return
    yield node.val
    for v in preorder(node.left):
        yield v
    for v in preorder(node.right):
        yield v


def read_file():
    with open('input_tree.txt', 'r') as file:
        nodes, changes = file.readline().strip().split(' ')
        arr = list(map(int, file.readline().strip().split(' ')))
    return int(nodes), int(changes), arr


def main():
    nodes, changes, arr = read_file()
    root = make_tree(1, nodes)
    nodes = list(preorder(root))




if __name__ == '__main__':
    main()
