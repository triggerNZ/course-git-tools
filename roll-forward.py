#!/usr/bin/env python
import git
import coursetool
import sys

def main():
    branch_from = sys.argv[1]
    repo = git.Repo('.')   # Must be run from the root of a git repo
    assert not repo.bare
    settings = coursetool.load_settings('.course-branches.yml')
    coursetool.roll_forward(repo, settings['course-branches'], branch_from)

if __name__ == '__main__':
    main()#!/usr/bin/env python
