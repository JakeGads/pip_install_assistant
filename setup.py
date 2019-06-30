from setuptools import setup
from distutils.core import setup

# read the contents of your README file
from os import path
this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
  name = 'pip_install_assistant',
  packages = ['pip_install_assistant'],
  install_requires = ['pip_install_assistant'],
  version = '0.2',
  license='MIT',
  description = 'Installs pip packages at runtime',
  long_description=long_description,
  long_description_content_type='text/markdown',
  author = 'Jake Gadaleta',
  author_email = 'jake.gads@gmail.com',
  url = 'https://github.com/gadzygadz/pip_install_assistant',
  download_url = 'https://github.com/gadzygadz/pip_install_assistant/archive/v0.1.2.tar.gz',
  keywords = ['pip', 'installer'],
  
  classifiers=[  
    'Intended Audience :: Developers',
    'Topic :: Software Development :: Build Tools',

    
    'License :: OSI Approved :: MIT License',

    'Programming Language :: Python :: 3',
  ],
)