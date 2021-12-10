class Protected:
    def __init__(self):
        self._protectedVar = 0  # This is creating a protected method
                                # It is prefixed by a single underscore
obj = Protected()
obj._protectedVar = 34
print(obj._protectedVar)
