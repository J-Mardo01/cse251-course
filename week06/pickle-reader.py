import pickle



with open('grades.dat', 'rb') as f:
    mydict = pickle.load(f)
    
print(mydict)

with open('person.dat', 'rb') as f:
    person = pickle.load(f)

print(person)
