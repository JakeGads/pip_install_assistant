from setuptools import setup

from distutils.core import setup
setup(
  name = 'pip_install_assistant',
  packages = ['pip_install_assistant'],
  version = '0.1.0',
  license='MIT',
  description = 'Installs pip packages at runtime',
  author = 'Jake Gadaleta',
  author_email = 'jake.gads@gmail.com',
  url = 'https://github.com/gadzygadz/pip_install_assistant',
  download_url = 'https://github.com/gadzygadz/pip_install_assistant/archive/v01.tar.gz'
  keywords = ['pip', 'installer'],
  
  classifiers=[  
    'Development Status :: 2 - Beta',

    
    'Intended Audience :: Developers',
    'Topic :: Software Development :: Build Tools',

    
    'License :: OSI Approved :: MIT License',

    'Programming Language :: Python :: 3',
  ],
)