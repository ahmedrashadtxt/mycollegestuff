class Dog:

    def __init__(self, breed, color, name):
        self.breed = breed
        self.color = color
        self.name = name

    def run(self):
        print(self.name,"is running")

    def bark(self):
        print(self.name, "is barking")

tommy = Dog("Bull","brown","Tommy")
tommy.run()
tommy.bark()