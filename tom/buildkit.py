import subprocess as sb
import click as cl
import os
import datetime
from licenses import *

currentDateTime = datetime.datetime.now()
date = currentDateTime.date()
year = date.strftime("%Y")


def buildPython(name, uname, ghname, ulic):
    pwd = os.getcwd()
    os.mkdir(pwd+f'/{name}')
    os.chdir((os.getcwd())+'/'+name)
    os.mkdir((os.getcwd())+f'/{name}')
    os.mkdir((os.getcwd())+f'/tests')
    with open(f'{name}/main.py', 'w') as f:
        f.write(f"""# {name}""")
    with open(f'{name}/__init__.py', 'w') as f:
        f.write("""__version__ = '0.1.0'""")
    with open(f'tests/__init__.py', 'w') as f:
        f.write("""""")
    with open(f'tests/test_{name}.py', 'w') as f:
        f.write("""from lolacli import __version__

def test_version():
    assert __version__=='0.2.3'""")
    with open('setup.py', 'w') as f:
        f.write(f'''from setuptools import find_packages, setup

VERSION = '0.1.0'
with open("README.md") as f:
    README = f.read()

setup(
    name = "{name}",
    version = VERSION,
    description = "**Enter project Description here**",
    long_description_content_type = "text/markdown",
    long_description = README,
    url = "https://github.com/{ghname}/{name}",
    author = "{uname}",
    author_email = "Your email here",
    packages = find_packages(),
    install_requires = [],
    license = '{ulic}',
    keywords = ['{name}', "project_{name}" ],
    classifiers = []
)
''')
        f.close()
    with open('README.md', 'w') as f:
        f.write(f'''# {name}
## Version: 0.1.0

### Introductiom

### Installation

### Usage

### Dependencies

### Snapshots

### Developer Tools

### Our Team

### Licensing

{ulic.upper()} License

{checkLicense(ulic.lower())}

### Special Notes (optional)
''')

def buildPython(name, uname, ghname, ulic):
    pwd = os.getcwd()
    os.mkdir(pwd+f'/{name}')
    os.chdir((os.getcwd())+'/'+name)
    os.mkdir((os.getcwd())+f'/{name}')
    os.mkdir((os.getcwd())+f'/tests')
    with open(f'{name}/main.py', 'w') as f:
        f.write(f"""# {name}""")
    with open(f'{name}/__init__.py', 'w') as f:
        f.write("""__version__ = '0.1.0'""")
    with open(f'tests/__init__.py', 'w') as f:
        f.write("""""")
    with open(f'tests/test_{name}.py', 'w') as f:
        f.write("""from lolacli import __version__

def test_version():
    assert __version__=='0.2.3'""")
    with open('setup.py', 'w') as f:
        f.write(f'''from setuptools import find_packages, setup

VERSION = '0.1.0'
with open("README.md") as f:
    README = f.read()

setup(
    name = "{name}",
    version = VERSION,
    description = "**Enter project Description here**",
    long_description_content_type = "text/markdown",
    long_description = README,
    url = "https://github.com/{ghname}/{name}",
    author = "{uname}",
    author_email = "Your email here",
    packages = find_packages(),
    install_requires = [],
    license = '{ulic}',
    keywords = ['{name}', "project_{name}" ],
    classifiers = []
)
''')
        f.close()
    with open('README.md', 'w') as f:
        f.write(f'''# {name}
## Version: 0.1.0

### Introductiom

### Installation

### Usage

### Dependencies

- pygame

### Snapshots

### Developer Tools

### Our Team

### Licensing

{ulic.upper()} License

{checkLicense(ulic.lower())}

### Special Notes (optional)
''')
