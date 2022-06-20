"""
This class contains an implementation of a simple priority queue
"""

import logging
import sys
logging.basicConfig(stream=sys.stdout, level=logging.DEBUG)

class Command():
    """
    Command class that contains the command to be
    executed and its priority
    """
    def __init__(self, command, priority):
        self.__command = command
        self.__priority = priority

    def command(self):
        return self.__command

    def priority(self):
        return self.__priority

    def setCommand(self, command):
        self.__command = command

    def setPriority(self, priority):
        self.__priority = priority

class PriorityQueue():
    MIN_PRIORITY = 0
    MAX_PRIORITY = 10
    """
    This class implements a simple priority queue
    as a max heap data structure(using a python list)

    An item inserted to the queue will look like:
    {
        priority: 4,
        command: 'ls'
    }
    The higher the number, the higher the priority
    ie: 10 - highest priority; 1 - lowest priority
    """
    def __init__(self):
        # The first node is left empty to make tree traversal easier
        self.heap = [None]
        self.size = 0

        self.logger = logging.getLogger('PriorityQueue')

    def deQueue(self):
        """
        Function that removes the root node from the max heap
        """
        # Perform prechecks
        if self.size < 1:
            self.logger.warning('Cannot dequeue. Queue is empty')
            return

        # Move the last leaf node to the root node in the heap
        root_node = self.heap[1] = self.heap[self.size]
        self.size -= 1
        self.heap.pop()

        # Heapify the data structure by checking if the parent node's
        # priority is higher than its children nodes
        i = 1
        while i <= self.size//2:
            li = i*2 # Index of left child
            ri = i*2 + 1 # Index of right child

            # If either of the child node priorities are higher than the
            # parent node, then swap with the child with higher priority
            curr_priority = self.heap[i].priority()
            left_priority = self.heap[li].priority()
            # Assign a dummy low priority if right child is not present
            right_priority = self.heap[ri].priority() \
                             if ri <= self.size else -1
            if (curr_priority < left_priority or
                curr_priority < right_priority):
                if left_priority > right_priority:
                    self.heap[i], self.heap[li] = self.heap[li], self.heap[i]
                    i = li
                else:
                    self.heap[i], self.heap[ri] = self.heap[ri], self.heap[i]
                    i = ri
            else:
                break
        return root_node

    def enQueue(self, item):
        """
        Function that inserts a node to the max heap
        """
        # Perform prechecks
        if (not item['command'] or
            (isinstance(item['command'], str) and
             not item['command'].strip())):
            self.logger.warning('Cannot add empty command to queue.')
            return

        if (item['priority'] < self.MIN_PRIORITY or
            item['priority'] > self.MAX_PRIORITY):
            self.logger.warning(
                'Cannot add command {cmd} to queue. ' \
                'Priority must be between {min} and {max}'.format(
                    cmd=item['command'],
                    min=self.MIN_PRIORITY,
                    max=self.MAX_PRIORITY))
            return

        # Insert the node as a leaf to the heap
        self.size += 1
        self.heap.append(Command(item['command'], item['priority']))

        if self.size == 1:
            return

        # Heapify the data structure by checking if the child node's
        # priority is lower than its parent node
        i = self.size
        while (i > 1 and
               self.heap[i].priority() > self.heap[i//2].priority()):
            # Swap the parent and child nodes to keep it a max heap
            self.heap[i], self.heap[i//2] = self.heap[i//2], self.heap[i]
            i = i//2

    def getQueueSize(self):
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
