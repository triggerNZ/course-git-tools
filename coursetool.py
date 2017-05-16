import yaml
import git

def load_settings(path):
    return yaml.load(open(path))

def write_to(repo, branches, target):
    for branch in branches:
        branch_commit = repo.commit(branch)
        print(branch_commit)
