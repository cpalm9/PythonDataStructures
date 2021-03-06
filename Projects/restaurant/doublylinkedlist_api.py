#!/usr/bin/env python3


class DoublyLinkedList(object):
    '''
    A doubly-linked list implementation that holds arbitrary objects.
    '''
    
    def __init__(self):
        '''Creates a linked list.'''
        self.head = None
        self.tail = None
        self.size = 0
        
    def debug_print(self):
        '''Prints a representation of the entire list.'''
        values = []
        # reverse = []
        # print(reverse)
        output = str(self.size) + ' >>> '
        n = self.head
        r = self._get_node(self.size - 1)

        while (n != None):
            values.append(str(n.value))
            output += str(n.value)
            if n.next is not None:
                output += ", "
            n = n.next
        n = r
        output += ' >>> '
        while (n != None):
            values.append(str(n.value))
            output += str(n.value)
            if n.prev is not None:
                output += ", "
            n = n.prev
        print(output)
        # for x in range(self.size):
        #     values.append(str(n.value))
        #     n = n.next
        # for x in range(self.size - 1, 0,-1):
        #     reverse.append(str(r.value))
        #     r = r.prev
        # print('{} >>> {} >>> {}'.format(self.size, ', '.join(values), ', '.join(reverse)))
        
    def _get_node(self, index):
        '''Retrieves the Node object at the given index.  Throws an exception if the index is not within the bounds of the linked list.'''
        try:
            if 0 <= index < self.size:
                n = self.head
                for x in range(index):
                    n = n.next
                return n
        except:
            raise IndexError('The given index is not within the bounds of the current list.')
    
    def check_value(self, value):
        n = self.head
        while n != None:
            if n.value == value:
                return True
            n = n.next

    def check_index(self, value):
        n = self.head
        i = 0
        while n != None:
            if n.value == value:
                return i
            n = n.next
            i +=1
        
    def add(self, item):
        '''Adds an item to the end of the linked list.'''
        if self.head is not None:
            last_node = self._get_node(self.size-1)
            last_node.next = Node(item)
            last_node.next.prev = last_node
            self.size += 1
        else:
            self.head = Node(item)
            self.size += 1
        
    def insert(self, index, item):
        '''Inserts an item at the given index, shifting remaining items right.'''
        if self._get_node(index):
            if index == 0:
                temp_val = self.head
                self.head = Node(item)
                self.head.next = temp_val
                temp_val.prev = self.head
                self.size += 1

            else:
                prev_val = self._get_node(index-1)
                follow_val = self._get_node(index)
                prev_val.next = Node(item)
                prev_val.next.prev = prev_val
                prev_val.next.next = follow_val
                prev_val.next.next.prev = prev_val.next
                self.size += 1
    
    def set(self, index, item):
        '''Sets the given item at the given index.  Throws an exception if the index is not within the bounds of the linked list.'''
        if index < self.size:
            node = self._get_node(index)
            node.value = item
        else:
            raise IndexError('The given index is not within the bounds of the current list.')
        
    def get(self, index):
        '''Retrieves the item at the given index.  Throws an exception if the index is not within the bounds of the linked list.'''
        if index < self.size:
            node = self._get_node(index)
            print('{}'.format(node.value))
            return node.value
        else:
            raise IndexError('The given index is not within the bounds of the current list.')
    
    def delete(self, index):
        '''Deletes the item at the given index. Throws an exception if the index is not within the bounds of the linked list.'''
        if self._get_node(index):
            if index is not 0:
                prev_val = self._get_node(index-1)
                prev_val.next = self._get_node(index+1)
                if self._get_node(index + 1) is not None:
                    prev_val.next.prev = prev_val
            else:
                if self.head == None:
                    raise IndexError('The given index is not within the bounds of the current list.') 
                self.head = self._get_node(index+1)
                self.head.prev = None
            self.size -= 1
        
    def swap(self, index1, index2):
        '''Swaps the values at the given indices.'''
        if (index2 <= self.size):
            if index1 is not 0:
                swap_node = self._get_node(index1).value
                self._get_node(index1).value = self._get_node(index2).value
                self._get_node(index2).value = swap_node
            else:
                swap_node = self._get_node(index1).value
                self._get_node(index1).value = self._get_node(index2).value
                self._get_node(index2).value = swap_node
                
        else:
            raise IndexError('The given index is not within the bounds of the current list.')
        
        
######################################################
###   A node in the linked list
        
class Node(object):
    '''A node on the linked list'''
    
    def __init__(self, value):
        self.value = value
        self.prev = None
        self.next = None
        
    def __str__(self):
        return '<Node: {}>'.format(self.value)
