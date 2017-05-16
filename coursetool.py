import yaml
import git

def load_settings(path):
    return yaml.load(open(path))

def write_to(repo, branches, target):

    current_parent = []

    for branch in branches:
        branch_head_tree = repo.commit(branch).tree
        commit_for_branch = git.Commit.from_tree(repo, branch_head_tree, "Commit from " + branch, current_parent)
        current_parent = [commit_for_branch]

    print(current_parent)    
