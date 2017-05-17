import yaml
import git

def load_settings(path):
    return yaml.load(open(path))

def write_to(repo, branches, target_branch):
    current_parent = []

    for branch in branches:
        branch_head_tree = repo.commit(branch).tree
        commit_for_branch = git.Commit.create_from_tree(repo, branch_head_tree, "Commit from " + branch, current_parent)
        current_parent = [commit_for_branch]

    repo.create_head(target_branch, current_parent[0], True)


def roll_forward(repo, branches, branch_from):
    print(repo.git)
    idx = branches.index(branch_from)
    branches_to = branches[(idx + 1):]

    for branch_to in branches_to:
        print ("Cherry-picking from " + branch_from + " to " + branch_to)
        #TODO handle more than one commit (right now we can just squash (or something))
        repo.git.cherry_pick(branch_from, branch_to)
        branch_from = branch_to
