class Animal:
    def __init__(self):
        self.num_eyes = 2

    def breathe(self):
        print("Inhale, exhale")


class Fish(Animal):  # Animal is the class to be inherited
    def __init__(self):
        super().__init__()  # super() allows to inherit init from class Animal. Recommended but not required!

    def swim(self):
        print("moving in water.")

    def breathe(self):
        super().breathe()
        print("doing this underwater.")


nemo = Fish()
nemo.swim()
nemo.breathe()
print(nemo.num_eyes)