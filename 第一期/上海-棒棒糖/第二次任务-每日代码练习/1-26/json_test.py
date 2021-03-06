import json
class Student(object):
    def __init__(self, name, age, score):
        self.name = name
        self.age = age
        self.score = score

def student2dict(Student):
    return {
        'name': Student.name,
        'age': Student.age,
        'score': Student.score
            }
s = Student('Bob', 20, 88)
#print(json.dumps(s, default=student2dict))
print(json.dumps(s, default=lambda obj: obj.__dict__))



import json
class Student(object):
    def __init__(self, name, age, score):
        self.name = name
        self.age = age
        self.score = score

s = Student('Bob', 20, 88)
print(json.dumps(s, default=lambda obj: obj.__dict__))

def dict2student(d):
    return Student(d['name'], d['age'], d['score'])

json_str = '{"age": 20, "score": 88, "name": "Bob"}'
print(json.loads(json_str, object_hook=dict2student))

