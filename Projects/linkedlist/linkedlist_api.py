#!/usr/bin/env python3


class LinkedList(object):
    '''
    A linked list implementation that holds arbitrary objects.
    '''
    
    def __init__(self):
        '''Creates a linked list.'''
        self.head = None
        self.size = 0
        
    def debug_print(self):
        '''Prints a representation of the entire list.'''
        values = []
        n = self.head
        while n != None:
            values.append(str(n.value))
            n = n.next
        print('{} >>> {}'.format(self.size, ', '.join(values))) 
        
        
    def _get_node(self, index):
        '''Retrieves the Node object at the given index.  Throws an exception if the index is not within the bounds of the linked list.'''
        try:
            if 0 <= index < self.size:
                n = self.head
                for x in range(index):
                    n = n.next
                return n
        except:
            print('Error: Out of Bounds')
        
    def add(self, item):
        '''Adds an item to the end of the linked list.'''
        if self.head is not None:
            last_node = self._get_node(self.size-1)
            last_node.next = Node(item)
            self.size += 1
        else:
            self.head = Node(item)
            self.size += 1
        
    def insert(self, index, item):
        '''Inserts an item at the given index, shifting remaining items right.'''
        if index <= self.size:
            new_item = Node(item)
            n = self._get_node(index)
            prev_val = self._get_node(index - 1)
            
            prev_val.next = new_item
            new_item.next = n
            
            self.size += 1
        else:
            print('Error: Out of Bounds')

    
    def set(self, index, item):
        '''Sets the given item at the given index.  Throws an exception if the index is not within the bounds of the linked list.'''
        if index < self.size:
            node = self._get_node(index)
            node.value = item
        else:
            print('Error: Out of Bounds')
        
    def get(self, index):
        '''Retrieves the item at the given index.  Throws an exception if the index is not within the bounds of the linked list.'''
        if index < self.size:
            node = self._get_node(index)
            print(node.value)
        else:
            print('Error: Out of Bounds')
    def delete(self, index):
        '''Deletes the item at the given index. Throws an exception if the index is not within the bounds of the linked list.'''
        if index < self.size:
            if index is not 0:
                prev_val = self._get_node(index-1)
                prev_val.next = self._get_node(index+1)
            else:
                self.head = self._get_node(index+1)

            self.size -= 1
        else:
            print('Error: Out of Bounds')
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
            print('Error: Out of Bounds')
        
        
        
        
        
        
######################################################
###   A node in the linked list
        
class Node(object):
    '''A node on the linked list'''
    
    def __init__(self, value):
        self.value = value
        self.next = None
        
    def __str__(self):
        return '<Node: {}>'.format(self.value)
