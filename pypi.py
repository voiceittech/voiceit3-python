import os
import json
import sys
import requests
import subprocess

#  Get the new version number as command line argument
new_version = sys.argv[1]

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
 url = "https://github.com/voiceittech/VoiceIt2-Python",
 download_url = "https://github.com/voiceittech/VoiceIt2-Python/archive/''' + new_version + '''.tar.gz",
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
gh_token = os.environ['GH_TOKEN']

release_json = {'tag_name': new_version, 'target_commitish': 'master', 'name': new_version, 'body': '', 'draft': False, 'prerelease': False}

try:
    response = requests.post('https://api.github.com/repos/voiceittech/VoiceIt2-Python/releases', headers={'Authorization': 'token ' + gh_token}, data=json.dumps(release_json))
    print(response.text)
except  requests.exceptions.HTTPError as e:
    print(e.read())
    exit(1)

#  Update PyPi with newest package
pypiusername = os.environ['PYPIUSERNAME']
pypipassword = os.environ['PYPIPASSWORD']

pypistring = '''[distutils]
index-servers = pypi

[pypi]
username:''' + pypiusername + '''
password:''' + pypipassword

with open(str(os.path.expanduser("~")+"/") + "/.pypirc", "w") as pypirc:
    pypirc.write(pypistring)

subprocess.call(['python3', 'setup.py', 'sdist', 'upload', '-r', 'pypi'])
