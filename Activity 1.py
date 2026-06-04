class IOString():
    def __init__(self):
        self.str1=""
    def get(self):
        self.str1=input("Enter a string in lowercase.")
    def uppercase(self):
        print("result is",self.str1.upper())
str1=IOString()
str1.get()
str1.uppercase()
