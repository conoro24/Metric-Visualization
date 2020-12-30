from django.shortcuts import render
from github import Github

# Create your views here.
username = 'conoro24'
g = Github()
user = g.get_user(username)

lstA = []
lstB = []

for repo in user.get_repos():
    name = repo.name
    commits = repo.get_commits().totalCount
  
    lstA.append(name)
    lstB.append(commits)

def indexPage(request):
	varA = lstA
	varB = lstB
	context = {'varA':varA,'varB':varB}
	return render(request,'index.html', context)