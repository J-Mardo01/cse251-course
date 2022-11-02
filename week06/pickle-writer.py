import pickle
from MyClass import Person

grades = {'Aaron': 85, 'Brandon': 100, 'Ryan': 75}

with open('grades.dat', 'wb') as f:
    pickle.dump(grades, f)

person = Person("Brandon", "1234 Main Street", "1234567890")

with open('person.dat', 'wb') as f:
    pickle.dump(person, f)
