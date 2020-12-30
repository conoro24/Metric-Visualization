from django.shortcuts import render
from github import Github

# Create your views here.
username = 'conoro24'
g = Github()

user = g.get_user(username)
for repo in user.get_repos():
    commits = repo.get_commits().totalCount
    name = repo.full_name

def indexPage(request):
	varA = name
	varB = commits
	context = {'a':'a'}
	return render(request,'index.html', context)