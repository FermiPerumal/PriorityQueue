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
