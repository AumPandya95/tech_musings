class Node:
    def __init__(self,
                 data=None,
                 next_element=None):
        self.data = data
        self.next_element = next_element


class LinkedList:
    def __init__(self):
        self.head = None

    def print(self):
        if not self.head:
            print("Linked list is empty!")
            return

        itr = self.head
        liststr = ''
        while itr:
            liststr += str(itr.data) + '--->'
            itr = itr.next_element
        print(liststr)

    def get_length(self):
        count = 1
        itr = self.head
        while itr.next_element:
            count += 1
            itr = itr.next_element

        return count

    def insert_at_beginning(self, data):
        node = Node(data, self.head)
        self.head = node

    def insert_at_end(self, data):
        if not self.head:
            self.head = Node(data, None)
            return

        itr = self.head
        while itr.next_element:  # Will continue executing unless itr.next_element is None
            itr = itr.next_element
        itr.next_element = Node(data, None)

    def insert_values(self, data_list):
        self.head = None
        # for _data in data_list[::-1]:  # One way
        #     node = Node(_data, self.head)
        #     self.head = node
        for _data in data_list:  # Second way
            self.insert_at_end(_data)
        return

    def remove_element_at_position(self, position):
        if position < 0 or position >= self.get_length():
            raise IndexError('Invalid position')

        if position == 0:
            self.head = self.head.next_element
            return

        itr = self.head
        index = 0
        while index <= position:
            if index == position - 1:
                itr.next_element = itr.next_element.next_element
                break
            index += 1
            itr = itr.next_element

        return

    def insert_at(self, position, data):
        if (position < 0 and position != -1) or position > self.get_length():
            raise IndexError('Invalid Position')

        if position == self.get_length() or position == -1:
            self.insert_at_end(data)
        elif position == 0:
            self.insert_at_beginning(data)
        else:
            itr = self.head
            count = 0
            while itr.next_element:
                if count == position - 1:
                    itr.next_element = Node(data, itr.next_element)
                    break
                count += 1
                itr = itr.next_element

    def insert_after_value(self, data_after, data_to_insert):
        itr = self.head
        while itr.next_element:
            if data_after == str(itr.data):
                itr.next_element = Node(data_to_insert, itr.next_element)
                return
            itr = itr.next_element

        self.insert_at_end(data_to_insert)

    def remove_by_value(self, data_to_remove):
        itr = self.head
        count = 0
        while itr.next_element:
            if str(itr.data) == data_to_remove:
                self.remove_element_at_position(count)
            count += 1
            itr = itr.next_element

        if (count == self.get_length() - 1) and (itr.data == data_to_remove):
            self.remove_element_at_position(self.get_length() - 1)


if __name__ == "__main__":
    l1 = LinkedList()
    # l1.insert_at_beginning(5)
    # l1.insert_at_beginning(89)
    # l1.insert_at_end(79)
    # l1.insert_at_end(799)
    # l1.insert_at_end(98)
    l1.insert_values(['Aum', 'Pandya', 'is', 'the', 'best', '!'])
    l1.insert_at(0, "friggin'")
    l1.print()
    print(f"length of the linkedlist is {l1.get_length()}")
    l1.remove_element_at_position(6)
    print('After removing element at position ->')
    l1.print()
    l1.insert_after_value('!', 'OG')
    l1.print()
    l1.remove_by_value("friggin'")
    l1.print()
