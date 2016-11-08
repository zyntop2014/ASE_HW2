
from __future__ import with_statement
from fabric.api import local, settings, abort, sudo
from fabric.contrib.console import confirm


def test():
    with settings(warn_only=True):
        result = local('python3 manage.py test polls', capture=True)
    if result.failed and not confirm("Tests failed. Continue anyway?"):
        abort("Aborting at user request.")

def pull():
    test()
    local("git pull")

def commit():
    test()
    local("git add .")
    local ("git commit -m 'testing' ")

def push():
    test()
    local("git push -u origin master")

def prepare_deploy():
    test()
    commit()
    push()

def deploy():
    test()
    local("python3 manage.py runserver")


