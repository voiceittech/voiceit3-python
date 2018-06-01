from distutils.core import setup
setup(
 name = 'voiceit2',
 packages = ['voiceit2'], # this must be the same as the name above
 version = '1.0.1',
 description = 'VoiceIt API 2.0 Python Wrapper',
 author = 'Hassan Ismaeel',
 author_email = 'hassan@voiceit.io',
 url = 'https://github.com/voiceittech/voiceit2-python', # use the URL to the github repo
 download_url = 'https://github.com/voiceittech/voiceit2-python/archive/1.0.1.tar.gz', # I'll explain this in a second
 keywords = ['biometrics', 'voice verification', 'voice biometrics'], # arbitrary keywords
 classifiers = [
 "Programming Language :: Python :: 3",
 "License :: OSI Approved :: MIT License",
 "Operating System :: OS Independent"],
)
