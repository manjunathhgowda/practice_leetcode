# Definition for Linked List Node
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val      # stores digit
        self.next = next    # pointer to next node

# Solution Class
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        # Dummy head to simplify list creation
        temp = ListNode(0)
        current = temp
        carry = 0

        # Loop until both lists and carry are exhausted
        while l1 is not None or l2 is not None or carry:
            num1 = l1.val if l1 else 0
            num2 = l2.val if l2 else 0

            total = num1 + num2 + carry
            carry = total // 10
            digit = total % 10

            # Create new node for the digit
            current.next = ListNode(digit)
            current = current.next

            # Move input pointers
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None

        return temp.next

# Helper: Python List -> Linked List
def list_to_linkedlist(arr):
    dummy = ListNode(0)
    current = dummy
    for num in arr:
        current.next = ListNode(num)
        current = current.next
    return dummy.next

# Helper: Linked List -> Python List
def linkedlist_to_list(node):
    result = []
    while node:
        result.append(node.val)
        node = node.next
    return result

# Main Execution (TEST CASES)
if __name__ == "__main__":

    # Example 1
    l1 = list_to_linkedlist([2, 4, 3])
    l2 = list_to_linkedlist([5, 6, 4])
    result = Solution().addTwoNumbers(l1, l2)
    print("Example 1 Output:", linkedlist_to_list(result))  # [7,0,8]

    # Example 2
    l1 = list_to_linkedlist([0])
    l2 = list_to_linkedlist([0])
    result = Solution().addTwoNumbers(l1, l2)
    print("Example 2 Output:", linkedlist_to_list(result))  # [0]

    # Example 3
    l1 = list_to_linkedlist([9,9,9,9,9,9,9])
    l2 = list_to_linkedlist([9,9,9,9])
    result = Solution().addTwoNumbers(l1, l2)
    print("Example 3 Output:", linkedlist_to_list(result))  # [8,9,9,9,0,0,0,1]
