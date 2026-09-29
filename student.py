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
        print("Student Not found")

add_student("Ashish")
add_student("Francis")
add_student("Gorsa")
add_student("Kravis")

find_student("Ashish")
find_student("Gorsa")
find_student("Isac")





# git i,s,a,c,
# git - branch, ->branch develop -> checkout develop -> checkout -b feature/student ===== b,d,cd,cf
#git s,d, remote add origin(no -u/-b/anything) link(guthub link)
#git remote -v
#git push -u origin feature/student

# """
# PS C:\Users\ASUS\Desktop\mlops-git> git init
# Initialized empty Git repository in C:/Users/ASUS/Desktop/mlops-git/.git/
# PS C:\Users\ASUS\Desktop\mlops-git> git status
# On branch master

# No commits yet

# Untracked files:
#   (use "git add <file>..." to include in what will be committed)
#         student.py

# nothing added to commit but untracked files present (use "git add" to track)

# PS C:\Users\ASUS\Desktop\mlops-git> git add student.py

# PS C:\Users\ASUS\Desktop\mlops-git> git status
# On branch master

# No commits yet

# Changes to be committed:
#   (use "git rm --cached <file>..." to unstage)
#         new file:   student.py

# PS C:\Users\ASUS\Desktop\mlops-git> git add .

# PS C:\Users\ASUS\Desktop\mlops-git> git commit -m "First Changes - student.py"

# [master (root-commit) ab49069] First Changes - student.py
#  1 file changed, 7 insertions(+)
#  create mode 100644 student.py
# PS C:\Users\ASUS\Desktop\mlops-git> git status
# On branch master
# nothing to commit, working tree clean
# PS C:\Users\ASUS\Desktop\mlops-git> git branch
# * master
# PS C:\Users\ASUS\Desktop\mlops-git> git branch develop
# PS C:\Users\ASUS\Desktop\mlops-git> git checkout develop
# Switched to branch 'develop'
# PS C:\Users\ASUS\Desktop\mlops-git> git checkout -b feature/student
# Switched to a new branch 'feature/student'
# PS C:\Users\ASUS\Desktop\mlops-git> git branch
#   develop
# * feature/student
#   master
# PS C:\Users\ASUS\Desktop\mlops-git> git status
# On branch feature/student
# Changes not staged for commit:
#   (use "git add <file>..." to update what will be committed)
#   (use "git restore <file>..." to discard changes in working directory)
#         modified:   student.py

# no changes added to commit (use "git add" and/or "git commit -a")
# PS C:\Users\ASUS\Desktop\mlops-git> git diff

# PS C:\Users\ASUS\Desktop\mlops-git> git add student.py
# PS C:\Users\ASUS\Desktop\mlops-git> git commit -m "Second Changes - searching in student.py"
# [feature/student 7726f31] Second Changes - searching in student.py
#  1 file changed, 29 insertions(+), 1 deletion(-)


# PS C:\Users\ASUS\Desktop\mlops-git> git remote add origin https://github.com/AshishPShaji/MLOps-Git

# PS C:\Users\ASUS\Desktop\mlops-git> git remote -v
# origin  https://github.com/AshishPShaji/MLOps-Git (fetch)
# origin  https://github.com/AshishPShaji/MLOps-Git (push)



# PS C:\Users\ASUS\Desktop\mlops-git> git push -u origin feature/student
# info: please complete authentication in your browser...
# Enumerating objects: 6, done.
# Counting objects: 100% (6/6), done.
# Delta compression using up to 20 threads
# Compressing objects: 100% (4/4), done.
# Writing objects: 100% (6/6), 765 bytes | 765.00 KiB/s, done.
# Total 6 (delta 1), reused 0 (delta 0), pack-reused 0 (from 0)
# remote: Resolving deltas: 100% (1/1), done.
# To https://github.com/AshishPShaji/MLOps-Git
#  * [new branch]      feature/student -> feature/student
# branch 'feature/student' set up to track 'origin/feature/student'.


# PS C:\Users\ASUS\Desktop\mlops-git> git branch
#   develop
# * feature/student
#   master
# PS C:\Users\ASUS\Desktop\mlops-git> git checkout master
# Switched to branch 'master'
# PS C:\Users\ASUS\Desktop\mlops-git> git checkout develop
# Switched to branch 'develop'
# PS C:\Users\ASUS\Desktop\mlops-git> git push -u origin develop
# Total 0 (delta 0), reused 0 (delta 0), pack-reused 0 (from 0)
# remote:
# remote: Create a pull request for 'develop' on GitHub by visiting:
# remote:      https://github.com/AshishPShaji/MLOps-Git/pull/new/develop
# remote:
# To https://github.com/AshishPShaji/MLOps-Git
#  * [new branch]      develop -> develop
# branch 'develop' set up to track 'origin/develop'.
# PS C:\Users\ASUS\Desktop\mlops-git> git checkout master
# Switched to branch 'master'
# PS C:\Users\ASUS\Desktop\mlops-git> git push -u origin master
# Total 0 (delta 0), reused 0 (delta 0), pack-reused 0 (from 0)
# remote:
# remote: Create a pull request for 'master' on GitHub by visiting:
# remote:      https://github.com/AshishPShaji/MLOps-Git/pull/new/master
# remote:
# To https://github.com/AshishPShaji/MLOps-Git
#  * [new branch]      master -> master
# branch 'master' set up to track 'origin/master'.


# PS C:\Users\ASUS\Desktop\mlops-git> git checkout feature/student
# Switched to branch 'feature/student'
# Your branch is up to date with 'origin/feature/student'.\
# PS C:\Users\ASUS\Desktop\mlops-git>

# """