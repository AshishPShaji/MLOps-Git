# 1) first commit :
# students = []
# def add_student(name):
#     students.append(name)
# add_student("Ashish")
# add_student("Francis")

# print(students)


#2) second commit (feature/student) :
students = []
def add_student(name):
    students.append(name)

def find_student(name):
    if name in students:
        print("Student found : ", name)
    else:
        print("Student Not found : ", name)

add_student("Ashish")
add_student("Francis")
add_student("Gorsa")
add_student("Kravis")

find_student("Ashish")
find_student("Gorsa")
find_student("Isac")




# git i,s,a,c,
# git - branch, ->branch develop -> checkout develop -> checkout -b feature/student