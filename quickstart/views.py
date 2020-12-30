from django.shortcuts import render
from github import Github

# Create your views here.
username = 'conoro24'
g = Github()

lstA = []
lstB = []

user = g.get_user(username)
for repo in user.get_repos():
    name = repo.full_name
    commits = repo.get_commits().totalCount
  
    lstA.append(name)
    lstB.append(commits)

def indexPage(request):
	varA = lstA
	varB = lstB
	context = {'varA':varA,'VarB':varB}
	return render(request,'index.html', context)