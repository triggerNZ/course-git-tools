#!/usr/bin/env python
import git
import coursetool

def main():
    repo = git.Repo('.')   # Must be run from the root of a git repo
    assert not repo.bare
    settings = coursetool.load_settings('.course-branches.yml')
    coursetool.write_to(repo, settings['course-branches'], settings['target-branch'])

if __name__ == '__main__':
    main()
