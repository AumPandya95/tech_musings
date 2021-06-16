# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def print_output(self, ll):
        itr = ll
        out_str = ''
        while itr:
            out_str += str(itr.val) + '--->'
            itr = itr.next

        return out_str[:-4]

    def reverse_numbers_from_linked_list(self, linked_list):
        itr = linked_list
        reverse_list = []
        while itr.next:
            reverse_list.insert(0, itr.val)
            itr = itr.next

        if not itr.next:
            reverse_list.insert(0, itr.val)

        return reverse_list

    def make_linked_list(self, data_list):
        linked_list = None
        for data in data_list[::-1]:
            node = ListNode(data, linked_list)
            linked_list = node

        return linked_list

    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        self.head = l1

        # Extracting values in reverse order in a list
        reversed_list1 = self.reverse_numbers_from_linked_list(l1)
        reversed_list2 = self.reverse_numbers_from_linked_list(l2)

        # Adding numbers in two lists

        num1 = int(''.join(str(x) for x in reversed_list1))
        num2 = int(''.join(str(x) for x in reversed_list2))
        fin = num1 + num2
        output = [int(i) for i in list(str(fin))[::-1]]
        # Returning output as a linked_list
        linkedlist = self.make_linked_list(output)

        return linkedlist


if __name__ == "__main__":
    link_list = Solution()
    l1 = link_list.make_linked_list([9, 9, 9, 9, 9, 9, 9])
    l2 = link_list.make_linked_list([9, 9, 9, 9])
    print(f'Linked list 1 -> {Solution().print_output(l1)}')
    print(f'Linked list 2 -> {Solution().print_output(l2)}')
    Solution().print_output(l1)
    Solution().print_output(l2)

    added_list = Solution().addTwoNumbers(l1, l2)
    print(f'Solution -> {Solution().print_output(added_list)}')
