import setuptools
from distutils.core import setup

setup(
 name = 'voiceit2',
 version = '1.0.3',
 description = 'VoiceIt API 2.0 Python Wrapper',
 author = 'Hassan Ismaeel',
 author_email = 'hassan@voiceit.io',
 packages=setuptools.find_packages(),
 install_requires=[
     'requests',
 ],
 url = 'https://github.com/voiceittech/voiceit2-python', # use the URL to the github repo
 download_url = 'https://github.com/voiceittech/voiceit2-python/archive/1.0.3.tar.gz', # I'll explain this in a second
 keywords = ['biometrics', 'voice verification', 'voice biometrics'], # arbitrary keywords
 classifiers = [
 "Programming Language :: Python :: 3",
 "License :: OSI Approved :: MIT License",
 "Operating System :: OS Independent"],
)
