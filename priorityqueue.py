"""
This class contains an implementation of a simple priority queue
using a max heap
"""
from command import Command

class PriorityQueue():
    """
    This class implements a simple priority queue
    as a linked (using a python list)

    An item inserted to the queue will look like:
    {
        priority: 4,
        command: 'ls'
    }
    The higher the number, the higher the priority
    ie: 10 - highest priority; 0 - lowest priority
    """
    def __init__(self, min_priority=0, max_priority=10):
        # The first node is left empty to make tree traversal easier
        self.heap = [None]
        self.size = 0
        self.min_priority = min_priority
        self.max_priority = max_priority

    def deQueue(self):
        """
        Function that removes the root node from the max heap
        """
        # Perform prechecks
        if self.size < 1:
            raise IndexError('Cannot dequeue. Queue is empty')

        # Move the last leaf node to the root node in the heap
        root_node = self.heap[1]
        self.heap[1] = self.heap[self.size]
        self.size -= 1
        self.heap.pop()

        # Heapify the data structure by checking if the parent node's
        # priority is higher than its children nodes
        i = 1
        while i <= self.size//2:
            swap_left = swap_right = False
            li = i*2 # Index of left child
            ri = i*2 + 1 # Index of right child

            # If either of the child node priorities are higher than the
            # parent node, then swap with the child with higher priority
            curr_prio = self.heap[i].priority()
            left_prio = self.heap[li].priority()
            # Assign a dummy low priority if right child is not present
            right_prio = self.heap[ri].priority() if ri <= self.size else -1

            if (curr_prio < left_prio or curr_prio < right_prio):
                if (left_prio > right_prio or
                   (left_prio == right_prio and # handle same priority nodes
                    self.heap[li].isOlderThan(self.heap[ri]))):
                    swap_left = True
                else:
                    swap_right = True
            # Handle same priorities between nodes
            elif (curr_prio == left_prio == right_prio):
                # If current node is older than left and right,
                # we will leave it as is
                if (self.heap[i].isOlderThan(self.heap[li]) and
                    self.heap[i].isOlderThan(self.heap[ri])):
                    break
                elif self.heap[li].isOlderThan(self.heap[ri]):
                    swap_left = True
                else:
                    swap_right = True
            else:
                break

            # Make the swap to heapify the binary tree data structure
            if swap_left:
                self.heap[i], self.heap[li] = self.heap[li], self.heap[i]
                i = li
            elif swap_right:
                self.heap[i], self.heap[ri] = self.heap[ri], self.heap[i]
                i = ri

        return root_node

    def enQueue(self, item):
        """
        Function that inserts a node to the max heap
        """
        # Perform prechecks
        if (not item['command'] or
            (isinstance(item['command'], str) and
             not item['command'].strip())):
            raise ValueError('Cannot add empty command to queue.')

        if (item['priority'] < self.min_priority or
            item['priority'] > self.max_priority):
            raise ValueError(
                'Cannot add command "{cmd}" to queue. ' \
                'Priority must be between {min} and {max}'.format(
                    cmd=item['command'],
                    min=self.min_priority,
                    max=self.max_priority))

        # Insert the node as a leaf to the heap
        self.size += 1
        self.heap.append(Command(item['command'], item['priority']))

        if self.size == 1:
            return

        # Heapify the data structure by checking if the child node's
        # priority is lower than its parent node
        i = self.size
        while i > 1:
            swap = False
            if self.heap[i].priority() > self.heap[i//2].priority():
                swap = True
            # If same priority, check which node is older
            elif (self.heap[i].priority() == self.heap[i//2].priority() and
                  self.heap[i].isOlderThan(self.heap[i//2])):
                swap = True

            if swap == True:
                # Swap the parent and child nodes to keep it a max heap
                self.heap[i], self.heap[i//2] = self.heap[i//2], self.heap[i]
            i = i//2

    def getQueue(self):
        """
        Function that returns the queue as a list
        """
        return self.heap

    def getQueueSize(self):
        """
        Function that returns the current queue size
        """
        return self.size

    def peekQueue(self):
        """
        Function that returns the root node of the heap
        ie: the node with the highest priority
        """
        return self.heap[1]

    def printQueue(self):
        """
        Function that prints all nodes in the heap by
        traversing through each level
        """
        for node in self.heap[1:]:
            print (node.command(), node.priority())
