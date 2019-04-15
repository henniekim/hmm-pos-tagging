class Set:
    def __init__(self):
        self.contents = []
        pass

    def addElement(self, newValue):
        if self.isElement(newValue) is False:
            self.contents.append(newValue)
        else:
            pass

    def isElement(self, key):
        if key in self.contents:
            return True
        else:
            return False