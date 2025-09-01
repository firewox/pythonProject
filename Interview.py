
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


#LCR 023. 相交链表
def getIntersectionNode(headA, headB):
    '''
    相交链表
    :param headA:
    :param headB:
    :return:
    '''
    if not headA or not headB:
        return None
    
    pointerA = headA
    pointerB = headB
    while pointerA != pointerB:
        if pointerA:
            pointerA = pointerA.next
        else:
            pointerA = headB
        if pointerB:
            pointerB = pointerB.next
        else:
            pointerB = headA
    return pointerA


def quickSort(arr, low, high):
    '''
    快速排序
    :param arr:
    :param low:
    :param high:
    :return:
    '''
    if low < high:
        pivot_index = partition(arr, low, high)
        quickSort(arr, low, pivot_index - 1)
        quickSort(arr, pivot_index + 1, high)

def partition(arr, low, high):
    '''
    分区函数
    :param arr:
    :param low:
    :param high:
    :return:
    '''
    pivot = arr[high]
    i = low - 1
    for j in range(low, high):
        if arr[j] < pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1

# LCR 077. 排序链表
def sortLinkedList(head):
    '''
    排序链表
    :param head:
    :return:
    '''
    if not head or not head.next:
        return head

    # 将链表节点值存入数组
    values = []
    current = head
    while current:
        values.append(current.value)
        current = current.next
    
    # 使用快速排序对数组进行排序
    quickSort(values, 0, len(values) - 1)
    
    # 将排序后的值重新赋给链表节点
    current = head
    for val in values:
        current.value = val
        current = current.next
    
    return head

    
def mainEg6():
    '''
    排序链表
    :return:
    '''
    # 创建一个示例链表 4 -> 2 -> 1 -> 3
    head = ListNode(4)
    head.next = ListNode(2)
    head.next.next = ListNode(1)
    head.next.next.next = ListNode(3)

    print("Original linked list:")
    current = head
    while current:
        print(current.value, end=" ")
        current = current.next
    print()

    sorted_head = sortLinkedList(head)

    print("Sorted linked list:")
    current = sorted_head
    while current:
        print(current.value, end=" ")
        current = current.next
    print()


def main_eg5():
    '''
    相交链表
    :return:
    '''
    # 创建两个示例链表
    # 链表A: 1 -> 2 -> 3 \
    #                    -> 6 -> 7
    # 链表B:       4 -> 5 /
    headA = ListNode(1)
    headA.next = ListNode(2)
    headA.next.next = ListNode(3)
    intersection = ListNode(6)
    intersection.next = ListNode(7)
    headA.next.next.next = intersection

    headB = ListNode(4)
    headB.next = ListNode(5)
    headB.next.next = intersection

    result = getIntersectionNode(headA, headB)
    if result:
        print(f"Intersection at node with value: {result.value}")
    else:
        print("No intersection")



if __name__ == "__main__":
    # 单链表反转
    # main_eg1()
    # 二叉树的层序遍历
    # main_eg2()
    # 二叉树的前序遍历、中序遍历、后序遍历
    # main_eg3()
    # 二叉树的逆序
    # main_eg4()
    # 相交链表
    # main_eg5()
    # 排序链表
    mainEg6()