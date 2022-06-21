"""
This class contains the possible test cases
for adding and removing nodes from the
priority queue
"""
import unittest
from priorityqueue import PriorityQueue

# SAMPLE COMMANDS
COMMANDS = [
    {'command': 'echo "HelloWorld"', 'priority': 1},
    {'command': 'cp /bin/images/* .', 'priority': 0},
    {'command': 'ls media', 'priority': 10},
    {'command': 'cd bin', 'priority': 5},
    {'command': 'open *.exr', 'priority': 4},
    {'command': 'open ref_pic.jpg', 'priority': 7},
    {'command': 'htop', 'priority': 9}]

SAME_PRIO_COMMANDS = [
    {'command': 'cd bin', 'priority': 5},
    {'command': 'cd lib', 'priority': 5},
    {'command': 'echo "HelloWorld"', 'priority': 1},
    {'command': 'cd out', 'priority': 5},
    {'command': 'cp /bin/images/* .', 'priority': 0}]

EMPTY_COMMAND = {'command': '', 'priority': 3}
INVALID_PRIO_COMMAND1 = {'command': 'ls', 'priority': 11}
INVALID_PRIO_COMMAND2 = {'command': 'ls', 'priority': -1}

class PriorityQueueTest(unittest.TestCase):

    def test_enqueue(self):
        p_queue = PriorityQueue()
        for cmd in COMMANDS:
            p_queue.enQueue(cmd)
        self.assertEqual(len(COMMANDS), p_queue.getQueueSize())

    def test_enqueue_empty_command(self):
        p_queue = PriorityQueue()
        self.assertRaises(ValueError, p_queue.enQueue, EMPTY_COMMAND)

    def test_enqueue_invalid_priority(self):
        p_queue = PriorityQueue()
        self.assertRaises(ValueError, p_queue.enQueue, INVALID_PRIO_COMMAND1)
        self.assertRaises(ValueError, p_queue.enQueue, INVALID_PRIO_COMMAND2)

    def test_dequeue(self):
        p_queue = PriorityQueue()
        for cmd in COMMANDS:
            p_queue.enQueue(cmd)
        highest_prio = p_queue.deQueue()
        self.assertEqual(10, highest_prio.priority())
        self.assertEqual('ls media', highest_prio.command())

    def test_dequeue_same_prio(self):
        p_queue = PriorityQueue()
        for cmd in SAME_PRIO_COMMANDS:
            p_queue.enQueue(cmd)
        next_prio = p_queue.deQueue()
        self.assertEqual(5, next_prio.priority())
        self.assertEqual('cd bin', next_prio.command())
        next_prio = p_queue.deQueue()
        self.assertEqual(5, next_prio.priority())
        self.assertEqual('cd lib', next_prio.command())
        next_prio = p_queue.deQueue()
        self.assertEqual(5, next_prio.priority())
        self.assertEqual('cd out', next_prio.command())

    def test_dequeue_empty_queue(self):
        p_queue = PriorityQueue()
        self.assertRaises(IndexError, p_queue.deQueue)

if __name__ == '__main__':
    unittest.main()
