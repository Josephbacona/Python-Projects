class Protected:
    def __init__(self):
        self.__privateVar = 12

    def getPrivate(self):
        print(self.__privateVar)    # private is denoted by a double underscore prefix
                                    
    def setPrivate(self, private):
        self.__privateVar = private

obj = Protected()           # obj gets the data of the private variable
obj.getPrivate()
obj.setPrivate(23)
obj.getPrivate()
