"""Take incremental changes and push them to GitHub."""
import sh
from config import settings

gh_user = settings["github"]["user"]
gh_password = settings["github"]["password"]
gh_repo = settings["github"]["repo"]
git = sh.git.bake(_cwd=gh_repo)


def setBranch(branch):
    git.checkout(branch)


def commitToGH(branch, identifier):
    git.add('.')
    msg = "Committing %s to GH %s branch." % (identifier, branch)
    git.commit(m=msg)
    git.push("origin", branch)
