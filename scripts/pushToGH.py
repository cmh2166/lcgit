"""Take incremental changes and push them to GitHub."""
import sh
gh_repo = "/Users/Christina/Projects/lcgit"
git = sh.git.bake(_cwd=gh_repo)


def setBranch(branch):
    git.checkout(branch)


def commitToGH(branch, identifier):
    git.add('.')
    msg = "Committing %s to GH %s branch." % (identifier, branch)
    git.commit(m=msg)
    git.push("origin", branch)
