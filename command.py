from datetime import datetime

class Command():
    """
    Command class that contains the command to be
    executed and its priority and timestamp
    """
    def __init__(self, command, priority):
        self.__command = command
        self.__priority = priority
        self.__timestamp = datetime.now()

    def command(self):
        return self.__command

    def priority(self):
        return self.__priority

    def timestamp(self):
        return self.__timestamp

    def isOlderThan(self, other):
        return self.timestamp() < other.timestamp()

    def setCommand(self, command):
        self.__command = command

    def setPriority(self, priority):
        self.__priority = priority
