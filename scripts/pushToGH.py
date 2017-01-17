"""Take incremental changes and push them to GitHub."""
from git import *
from config import settings

gh_user = settings["github"]["user"]
gh_password = settings["github"]["password"]
gh_repo = settings["github"]["repo"]

repo = Repo(gh_repo)
print(repo.commits())