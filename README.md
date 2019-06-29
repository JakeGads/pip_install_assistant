# pip_install_assistant
A python script to handle pip installs during compile time


## Installation [Coming Soon]

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install pipper.

```bash
pip install pip-install-assistant
```


## Usage

```bash
from pip-install-assistant import installer
try:
    import packagex # this is not a real package
except
    install(packages = ['packagex', 'packagey'], pythons = ['python', 'python3'], pips = ['pip', 'pip3'])
    import packagex
    import packagey
```

### Params

packages - non-null list of packages that you wish to install <br />
pythons - a nullable list of the python command ie ```python``` or ```python3``` these are also the default cases <br />
pips - a nullable list of the pip commands ie ```pip``` or ```pip3``` these are also the default cases <br/>