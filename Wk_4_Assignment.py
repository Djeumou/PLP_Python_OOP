class Person:
    def __init__(self, name, age, gender) :
        self.name = name
        self.age = age
        self.gender = gender
    
    def introduce(self):
        return f'Hello {self.name}, you are {self.age} years old and you are a {self.gender} gender'
        
Me = Person('Marc', 19, 'Male')
print(Me.introduce())