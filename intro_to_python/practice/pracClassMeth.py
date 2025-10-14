class Dog:
    total_dogs = 0

    def __init__(self, name, breed):
        self.name = name
        self.breed = breed
        Dog.total_dogs += 1

    @classmethod
    def reset_dog_count(cls):
        cls.total_dogs = 0

    @classmethod
    def from_string(cls, dog_str):
        name, breed = dog_str.split("-")
        return cls(name, breed)

# Test the class
dog1 = Dog("Rex", "German Shepherd")
dog2 = Dog.from_string("Buddy-Golden Retriever")

print(Dog.total_dogs)   # Should print 2

Dog.reset_dog_count()
print(Dog.total_dogs)   # Should print 0
