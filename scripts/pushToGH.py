"""Take incremental changes and push them to GitHub."""
from github import Github
from config import settings

gh_user = settings["github"]["user"]
gh_password = settings["github"]["password"]
gh_repo = settings["github"]["repo"]

g = Github(gh_user, gh_password)