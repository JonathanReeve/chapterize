from distutils.core import setup
from sys import version_info as ver

if ver[0] < 3:
    version = str(ver[0]) + '.' + str(ver[1])
    sys.exit("""
    Error: your Python version is %s, but chapterize requires at least
    Python 3. Please upgrade your Python installation, or try using pip3
    instead of pip.""" % version)

setup(
    name = 'chapterize',
    packages = ['chapterize'], 
    version = '0.1.6',
    description = 'A tool for breaking etexts into chapters.',
    author = 'Jonathan Reeve',
    author_email = 'jon.reeve@gmail.com',
    url = 'https://github.com/JonathanReeve/chapterize', 
    download_url = 'https://github.com/JonathanReeve/chapterize/tarball/0.1.6',
    install_requires = ['Click'],
    keywords = ['NLP', 'text', 'chapters'],
    entry_points='''
    [console_scripts]
    chapterize = chapterize.chapterize:cli''',
)
