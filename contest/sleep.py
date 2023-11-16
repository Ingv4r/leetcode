class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def make_tree(node):
    i = 0
    if i < len(nodes):
        return TreeNode(
            i,
            left=make_tree(i * 2),
            right=make_tree((i * 2) + 1)
        )

def read_file():
    with open('input_tree.txt', 'r') as file:
        nodes, changes = file.readline().strip().split(' ')
        arr = list(map(int, file.readline().strip().split(' ')))
    return int(nodes), int(changes), arr


def main():
    nodes, changes, arr = read_file()
    nodes = [i + 1 for i in range(nodes)]
    make_tree(nodes)
    print(nodes, changes, arr)


if __name__ == '__main__':
    main()
