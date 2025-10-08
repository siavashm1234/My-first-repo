class person:
    def __init__(self,name):
        self.name = name
    def talk(self):
        print(f"hello i am {self.name}")


John = person("john")
John.talk()
