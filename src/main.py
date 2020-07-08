import subprocess
import os
from datetime import datetime

from random import randrange
from datetime import timedelta
def random_date(start, end):
    delta = end - start
    int_delta = (delta.days * 24 * 60 * 60) + delta.seconds
    random_second = randrange(int_delta)
    return start + timedelta(seconds=random_second)

d1 = datetime.strptime('1/1/2020 1:30 PM', '%m/%d/%Y %I:%M %p')
d2 = datetime.strptime('1/1/2022 4:50 AM', '%m/%d/%Y %I:%M %p')
print(random_date(d1, d2))  
getVersion =  subprocess.Popen("git status", shell=True, stdout=subprocess.PIPE).stdout
version =  getVersion.read().decode()
bashCommand = "git init"
os.system(bashCommand)
bashCommand = "git config --global user.name chzuhadulhadi"
os.system(bashCommand)
bashCommand = "git config --global user.email chzuhadulhadi@gmail.com"
os.system(bashCommand)
bashCommand = "git config --global user.password pucitf19"
os.system(bashCommand)
Toadd=(" ".join(version.split("\n\n")[1].split("\n\t")[1:])).split("new file:")[1:]
if len(Toadd)==0:
    Toadd = os.listdir()
print(Toadd)
dates=[]
for i in range(0,len(Toadd)):
    dates.append(random_date(d1, d2).strftime('%a %d %b %Y %X')+" BST")      #"Mon 20 Aug 2018 20:19:19 BST"
    dates.sort()
print(dates)
for i in  range(0,len(Toadd)):
    bashCommand="git add "+Toadd[i]
    print(bashCommand)
    os.system(bashCommand)
    bashCommand="set GIT_COMMITTER_DATE=\""+dates[i]+"\""
    print(bashCommand)
    bashCommand="set GIT_AUTHOR_DATE=\""+dates[i]+"\""
    print(bashCommand)
    # bashCommand="GIT_COMMITTER_DATE=\""+dates[i]+"\" git commit --amend --no-edit --date \""+dates[i]+"\""
    # print(bashCommand)
    bashCommand="git commit --amend --no-edit -m \"initial comms\""
    print(bashCommand)
    os.system(bashCommand)
    bashCommand="git branch -M main"
    os.system(bashCommand)
    bashCommand="git remote add origin https://github.com/chzuhadulhadi/Againntesting.git"
    os.system(bashCommand)
    bashCommand="git push -u origin main"
    os.system(bashCommand)