from __future__ import with_statement
from fabric.api import *
from fabric.contrib.console import confirm

def test():
    print "running all test cases"
    with settings(warn_only=True):
        result = local('python manage.py test polls', capture=True)
    if result.failed:
        abort("Testing failed, aborting......")
    else:
        if confirm("Tests succeeded. Continue to static testing?"):
            static_test()

def static_test():
    with settings(warn_only=True):
	   local("pylint polls")

def pull():
    local("git pull")
    test()

def push():
    test()
    local("git push -u origin master")

def commit():
    test()
    local("git add --all")
    local ("git commit -m 'testing' ")

def deploy():
    test()
    local("python manage.py runserver")


