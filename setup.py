import setuptools
from distutils.core import setup

setup(
 name = 'voiceit2',
 version = '1.0.5',
 description = 'VoiceIt API 2.0 Python Wrapper',
 author = 'Hassan Ismaeel',
 author_email = 'hassan@voiceit.io',
 packages=setuptools.find_packages(),
 install_requires=[
     'requests',
 ],
 url = 'https://github.com/voiceittech/voiceit2-python',
 download_url = 'https://github.com/voiceittech/voiceit2-python/archive/1.0.5.tar.gz',
 keywords = ['biometrics', 'voice verification', 'voice biometrics'],
 classifiers = [
 "Programming Language :: Python :: 3",
 "License :: OSI Approved :: MIT License",
 "Operating System :: OS Independent"],
)
