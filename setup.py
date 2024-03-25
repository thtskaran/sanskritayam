from setuptools import setup, find_packages
import codecs
import os

here = os.path.abspath(os.path.dirname(__file__))

with codecs.open(os.path.join(here, "README.md"), encoding="utf-8") as fh:
    long_description = "\n" + fh.read()

VERSION = '0.0.23'
DESCRIPTION = 'Sanskritayam to Python translator'
LONG_DESCRIPTION = 'sanskritayam is a programming language that uses Sanskrit words instead of English keywords. This package translates Sanskritayam code to Python code.'

# Setting up
setup(
    name="sanskritayam",
    version=VERSION,
    author="thtskaran",
    author_email="<hello@karanprasad.com>",
    description=DESCRIPTION,
    long_description_content_type="text/markdown",
    long_description=long_description,
    packages=find_packages(),
    install_requires=[],  
    keywords=['python', 'sanskritayam', 'skm', 'skt', 'thtskaran', 'sabskrit', 'language', 'transpiler'],
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ],
    
)