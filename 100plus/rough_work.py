class Stringer(object):
    def __init__self(self):
        self.s = ""
    
    def getInput(self):
        self.s = input("Enter string: ")
    
    def putOutput(self):
        print("Your string was: ",self.s)

strg = Stringer()

strg.getInput()
strg.putOutput()

    