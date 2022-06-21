"""
Main class that instantiates a priority queue, adds commands
with priority to the queue and pops them. The popped command
will be the next highest priority from the queue
"""

import logging
import sys
logging.basicConfig(
    stream=sys.stdout,
    level=logging.DEBUG)
logger = logging.getLogger('PriorityQueue')

from priorityqueue import PriorityQueue

# SAMPLE COMMANDS
COMMANDS = [
    {'command': 'echo "HelloWorld"', 'priority': 1},
    {'command': 'ls media', 'priority': 0},
    {'command': 'cp /bin/images/* .', 'priority': 10},
    {'command': 'cd bin', 'priority': 5},
    {'command': 'open *.exr', 'priority': 4},
    {'command': 'open ref_pic.jpg', 'priority': 7},
    {'command': 'cat .conf | grep preference', 'priority': 6},
    {'command': 'cd lib', 'priority': 5},
    {'command': 'cd out', 'priority': 5},
    {'command': 'htop', 'priority': 9},
    {'command': 'cd ref', 'priority': 5}]

def main():
    p_queue = PriorityQueue()
    # Add commands to the priority queue
    for cmd in COMMANDS:
        try:
            pass
            p_queue.enQueue(cmd)
        except ValueError as e:
            logger.warning(e)
        except Exception as e:
            logger.error(e)

    # Dequeue the priority queue by popping the
    # command with highest priority
    print ('\nDequeueing by priority:')
    for _ in range(p_queue.getQueueSize()):
        try:
            next_prio = p_queue.deQueue()
        except IndexError as e:
            logger.warning(e)
        except Exception as e:
            logger.error(e)
        else:
            print(
                'Priority:', next_prio.priority(),
                'Command:',next_prio.command())

if __name__ == '__main__':
    main()
