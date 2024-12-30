class A:
    def setMessage(self,m):
        self.message = m

    def printMessage(self):
        print(self.message)


# Una classe può ereditare n superclassi
class B(A):

    def __init__(self,message):
        super().__init__(message)
