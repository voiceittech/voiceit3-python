import os
import json
import sys
import requests
from pip._internal import commands
import subprocess

#  grab the latest version number of voiceit2 package from pip
pkg_name = 'voiceit2'
search_command = commands.search.SearchCommand()
options, _ = search_command.parse_args([pkg_name])
pypi_hits = search_command.search(pkg_name, options)
hits = commands.search.transform_hits(pypi_hits)


#  assign the verison number to the variable original_version
for hit in hits:
    if hit['name'] == pkg_name:
        original_version = hit['versions'][0]

#  convert the original_version string into an array (3 items that are separated by a '.')
version_split =  original_version.split('.')
#  Increment the minor version by 1, and reassign it to the last version array
version_split[2] =  str(int(version_split[2]) + 1)
#  Concatenate the array into a single string with each section separated by '.' (just like we started out with)
new_version = '.'.join(version_split)

#  Produce the string to store in ./setup.py
setup_string = '''import setuptools
from distutils.core import setup

setup(
 name = "voiceit2",
 version = "''' + new_version + '''",
 description = "VoiceIt API 2.0 Python Wrapper",
 author = "Hassan Ismaeel",
 author_email = "hassan@voiceit.io",
 packages=setuptools.find_packages(),
 install_requires=[
     "requests",
 ],
 url = "https://github.com/voiceittech/voiceit2-python",
 download_url = "https://github.com/voiceittech/voiceit2-python/archive/''' + new_version + '''.tar.gz",
 keywords = ["biometrics", "voice verification", "voice biometrics"],
 classifiers = [
 "Programming Language :: Python :: 3",
 "License :: OSI Approved :: MIT License",
 "Operating System :: OS Independent"],
)'''

#  store string into ./setup.py
with open('./setup.py', 'w') as setup:
    setup.write(setup_string)

#  Draft new release using Github REST API
#  githubusername = os.environ['GITHUBUSERNAME']
#  githubpassword = os.environ['GITHUBPASSWORD']
#
#  release_json = {'tag_name': new_version, 'target_commitish': 'master', 'name': new_version, 'body': '', 'draft': False, 'prerelease': False}
#
#  try:
    #  response = requests.post('https://api.github.com/repos/voiceittech/voiceit2-python/releases', auth=(githubusername, githubpassword), data=json.dumps(release_json))
    #  print(response.text)
#  except  requests.exceptions.HTTPError as e:
    #  print(e.read())
    #  exit(1)

#  Update PyPi with newest package
pypiusername = os.environ['PYPIUSERNAME']
pypipassword = os.environ['PYPIPASSWORD']

pypistring = '''[distutils]
index-servers = pypi

'''
#  username:''' + pypiusername + '''
#  password:''' + pypipassword

with open(str(os.path.expanduser("~")+"/") + "/.pypirc", "w") as pypirc:
    pypirc.write(pypistring)

subprocess.call(['python3', 'setup.py', 'sdist', 'upload', '-r', 'pypi'])
