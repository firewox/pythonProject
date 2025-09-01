
# 单链表反转
class ListNode:
    def __init__(self, value=0, next=None):
        self.value = value
        self.next = next


def reverse_linked_list(head):
    stack = []
    current = head
    while current:
        stack.append(current)
        current = current.next
    while stack:
        curr_value = stack.pop()
        print(curr_value.value, end=" ")

def main_eg1():
    # 创建一个示例链表 1 -> 2 -> 3 -> 4 -> 5
    # 循环创建链表
    head = ListNode(1)
    current = head
    for i in range(2, 6):
        current.next = ListNode(i)
        current = current.next
    current.next = None    

    print("Reversed linked list:")
    reverse_linked_list(head)
    print()



# 2叉树的层序遍历
class TreeNode:
    def __init__(self, value=0, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def level_order_traversal(root):
    '''
    层序遍历二叉树
    :param root:
    :return:
    '''
    if not root:
        return

    queue = [root]
    while queue:
        current = queue.pop(0)
        print(current.value, end=" ")

        if current.left:
            queue.append(current.left)
        if current.right:
            queue.append(current.right)

# 前序遍历
def preorder_travel(root):
    '''
    前序遍历二叉树
    :param root:
    :return:
    '''
    if not root:
        return
    print(root.value, end=" ")
    preorder_travel(root.left)
    preorder_travel(root.right)

# 中序遍历
def inorder_travel(root):
    '''
    中序遍历二叉树
    :param root:
    :return:
    '''
    if not root:
        return
    inorder_travel(root.left)
    print(root.value, end=" ")
    inorder_travel(root.right)

# 后序遍历
def postorder_travel(root):
    '''
    后序遍历二叉树
    :param root:
    :return:
    '''
    if not root:
        return
    postorder_travel(root.left)
    postorder_travel(root.right)
    print(root.value, end=" ")

# 二叉树逆序
def inver_tree(root):
    '''
    逆序二叉树
    :param root:
    :return:
    '''
    if not root:
        return
    root.left, root.right = root.right, root.left
    inver_tree(root.left)
    inver_tree(root.right)

def main_eg2():
    '''
    二叉树的层序遍历
    :return:
    '''
    # 创建一个示例二叉树
    #       1
    #      / \
    #     2   3
    #    / \
    #   4   5
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)

    print("Level order traversal:")
    level_order_traversal(root)
    print()

def main_eg3():
    '''
    二叉树的前序遍历、中序遍历、后序遍历
    :return:
    '''
    # 创建一个示例二叉树
    #       1
    #      / \
    #     2   3
    #    / \
    #   4   5
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)

    print("Preorder traversal:")
    preorder_travel(root)
    print()
    print("Inorder traversal:")
    inorder_travel(root)
    print()
    print("Postorder traversal:")
    postorder_travel(root)
    print()

def main_eg4():
    '''
    二叉树的逆序
    :return:
    '''
    # 创建一个示例二叉树
    #       1
    #      / \
    #     2   3
    #    / \
    #   4   5
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)

    print("Original tree level order traversal:")
    level_order_traversal(root)
    print()

    inver_tree(root)

    print("Inverted tree level order traversal:")
    level_order_traversal(root)
    print()

if __name__ == "__main__":
    # 单链表反转
    # main_eg1()
    # 二叉树的层序遍历
    # main_eg2()
    # 二叉树的前序遍历、中序遍历、后序遍历
    # main_eg3()
    # 二叉树的逆序
    main_eg4()