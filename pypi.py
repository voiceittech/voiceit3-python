import sys
import requests

#  grab the latest version number of voiceit2 package from pip3 (passed by command line argument) and create an array by splitting the string by '.'
original_version = sys.argv[1]
version_split =  original_version.split('.')
#  Increment the minor version by 1, and reassign it to the last version array
version_split[2] =  str(int(version_split[2]) + 1)
#  Concatenate the array into a single string with each section separated by '.' (just like we started out with)
new_version = '.'.join(version_split)

#  Grab the string of './setup.py', replace the old version number with new version number

with open('./setup.py', 'r') as setup:
    old_setup_string=setup.read()

new_setup_string = old_setup_string.replace(original_version, new_version)

with open('./setup.py', 'w') as setup:
    setup.write(new_setup_string)

"""
#  Push changes back to github

githubaccesstoken = os.environ['GITHUBACCESSTOKEN']

subprocess.call(['git', 'config', '--global', 'user.email', 'andrew@voiceit.io'])
subprocess.call(['git', 'config', '--global', 'user.email', 'voiceitbot'])
subprocess.call(['git', 'remote', 'rm', 'origin'])
subprocess.call(['git', 'remote', 'add', 'origin', 'https://' + githubaccesstoken + '@github.com/voiceittech/voiceit2-python.git'])
subprocess.call(['git', 'commit', '-m', '"Update setup.py version number"'])
subprocess.call(['git', 'push', 'origin', 'master'])

#  Draft new release using Github REST API
githubusername = os.environ['GITHUBUSERNAME']
githubusername = os.environ['GITHUBPASSWORD']

release_json = {'tag_name': new_version, 'target_commitish': 'master', 'name': new_version, 'body': '', 'draft': False, 'prerelease': False}

try:
    response = requests.post('https://api.github.com/repos/voiceittech/voiceit2-python/releases', auth=(githubusername, githubpassword), params=release_json)
    print(response.text)
except  requests.exceptions.HTTPError as e:
    print(e.read())
    exit(1)

#  Update PyPi with newest package

pypiusername = os.environ['PYPIUSERNAME']
pypipassword = os.environ['PYPIPASSWORD']

pypistring = '[distutils]\nindex-servers = pypi\n\n[pypi]\nrepository = https://pypi.python.org/pypi\nusername = ' + pypiusername+ '\npassword = ' + pypipassword

with open('~/.pypirc', "w") as pypirc:
    pypirc.write(pypistring)

subprocess.call(['python3', 'setup.py', 'sdist', 'upload', '-r', 'pypi'])
"""
