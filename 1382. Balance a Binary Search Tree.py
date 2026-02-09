from collections import deque

class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def balanceBST(self, root):
        arr = []

        def inorder(node):
            if not node:
                return
            inorder(node.left)
            arr.append(node.val)
            inorder(node.right)

        def build(l, r):
            if l > r:
                return None
            m = (l + r) // 2
            node = TreeNode(arr[m])
            node.left = build(l, m - 1)
            node.right = build(m + 1, r)
            return node

        inorder(root)
        return build(0, len(arr) - 1)


def build_tree(level_order):
    if not level_order:
        return None

    root = TreeNode(level_order[0])
    q = deque([root])
    i = 1

    while q and i < len(level_order):
        node = q.popleft()

        if i < len(level_order) and level_order[i] is not None:
            node.left = TreeNode(level_order[i])
            q.append(node.left)
        i += 1

        if i < len(level_order) and level_order[i] is not None:
            node.right = TreeNode(level_order[i])
            q.append(node.right)
        i += 1

    return root


def level_order(root):
    if not root:
        return []
    res = []
    q = deque([root])
    while q:
        node = q.popleft()
        if node:
            res.append(node.val)
            q.append(node.left)
            q.append(node.right)
        else:
            res.append(None)
    while res and res[-1] is None:
        res.pop()
    return res


if __name__ == "__main__":
    sol = Solution()

    tests = [
        [1, None, 2, None, 3, None, 4],
        [2, 1, 3]
    ]

    for t in tests:
        root = build_tree(t)
        new_root = sol.balanceBST(root)
        print(level_order(new_root))
