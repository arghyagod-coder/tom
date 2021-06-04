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
    os.system('git init')
    with open(f'{name}/main.py', 'w') as f:
        f.write(f"""# {name}""")
    with open(f'{name}/__init__.py', 'w') as f:
        f.write("""__version__ = '0.1.0'""")
    with open(f'tests/__init__.py', 'w') as f:
        f.write("""""")
    with open(f'tests/test_{name}.py', 'w') as f:
        f.write("""from lolacli import __version__

def test_version():
    assert __version__=='0.1.0'""")
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
    with open('.gitignore', 'w') as f:
        f.write('''# Byte-compiled / optimized / DLL files
__pycache__/
*.py[cod]
*$py.class

# C extensions
*.so

# Distribution / packaging
.Python
build/
develop-eggs/
dist/
downloads/
eggs/
.eggs/
lib/
lib64/
parts/
sdist/
var/
wheels/
share/python-wheels/
*.egg-info/
.installed.cfg
*.egg
MANIFEST

# PyInstaller
#  Usually these files are written by a python script from a template
#  before PyInstaller builds the exe, so as to inject date/other infos into it.
*.manifest
*.spec

# Installer logs
pip-log.txt
pip-delete-this-directory.txt

# Unit test / coverage reports
htmlcov/
.tox/
.nox/
.coverage
.coverage.*
.cache
nosetests.xml
coverage.xml
*.cover
*.py,cover
.hypothesis/
.pytest_cache/
cover/

# Translations
*.mo
*.pot

# Django stuff:
*.log
local_settings.py
db.sqlite3
db.sqlite3-journal

# Flask stuff:
instance/
.webassets-cache

# Scrapy stuff:
.scrapy

# Sphinx documentation
docs/_build/

# PyBuilder
.pybuilder/
target/

# Jupyter Notebook
.ipynb_checkpoints

# IPython
profile_default/
ipython_config.py

# pyenv
#   For a library or package, you might want to ignore these files since the code is
#   intended to run in multiple environments; otherwise, check them in:
# .python-version

# pipenv
#   According to pypa/pipenv#598, it is recommended to include Pipfile.lock in version control.
#   However, in case of collaboration, if having platform-specific dependencies or dependencies
#   having no cross-platform support, pipenv may install dependencies that don't work, or not
#   install all needed dependencies.
#Pipfile.lock

# PEP 582; used by e.g. github.com/David-OConnor/pyflow
__pypackages__/

# Celery stuff
celerybeat-schedule
celerybeat.pid

# SageMath parsed files
*.sage.py

# Environments
.env
.venv
env/
venv/
ENV/
env.bak/
venv.bak/

# Spyder project settings
.spyderproject
.spyproject

# Rope project settings
.ropeproject

# mkdocs documentation
/site

# mypy
.mypy_cache/
.dmypy.json
dmypy.json

# Pyre type checker
.pyre/

# pytype static type analyzer
.pytype/

# Cython debug symbols
cython_debug/''')
    with open('LICENSE', 'w') as f:
        f.write(f'''{checkLicense(ulic.lower())}''')

def buildPygame(name, uname, ghname, ulic):
    pwd = os.getcwd()
    os.mkdir(pwd+f'/{name}')
    os.chdir((os.getcwd())+'/'+name)
    os.mkdir((os.getcwd())+f'/data')
    os.mkdir((os.getcwd())+f'/static')
    os.mkdir((os.getcwd())+f'/static/images')
    os.mkdir((os.getcwd())+f'/static/audio')
    os.mkdir((os.getcwd())+f'/static/sprites')
    os.mkdir((os.getcwd())+f'/static/animated')
    os.system('git init')
    with open(f'data/main.py', 'w') as f:
        f.write("""import pygame, sys
from pygame.locals import *

pygame.init()

DISPLAYSURF = pygame.display.set_mode((400, 300))

pygame.display.set_caption('Hello World!')

while True: 
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
             sys.exit()
    pygame.display.update()
""")
    with open(f'data/__init__.py', 'w') as f:
        f.write("")

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
    install_requires = ['pygame',],
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

### Player Guide

### Dependencies

- pygame

### Snapshots

### Our Team

### Licensing

{ulic.upper()} License

{checkLicense(ulic.lower())}

### Special Notes (optional)
''')
    with open('.gitignore', 'w') as f:
        f.write('''# Byte-compiled / optimized / DLL files
__pycache__/
*.py[cod]
*$py.class

# C extensions
*.so

# Distribution / packaging
.Python
build/
develop-eggs/
dist/
downloads/
eggs/
.eggs/
lib/
lib64/
parts/
sdist/
var/
wheels/
share/python-wheels/
*.egg-info/
.installed.cfg
*.egg
MANIFEST

# PyInstaller
#  Usually these files are written by a python script from a template
#  before PyInstaller builds the exe, so as to inject date/other infos into it.
*.manifest
*.spec

# Installer logs
pip-log.txt
pip-delete-this-directory.txt

# Unit test / coverage reports
htmlcov/
.tox/
.nox/
.coverage
.coverage.*
.cache
nosetests.xml
coverage.xml
*.cover
*.py,cover
.hypothesis/
.pytest_cache/
cover/

# Translations
*.mo
*.pot

# Django stuff:
*.log
local_settings.py
db.sqlite3
db.sqlite3-journal

# Flask stuff:
instance/
.webassets-cache

# Scrapy stuff:
.scrapy

# Sphinx documentation
docs/_build/

# PyBuilder
.pybuilder/
target/

# Jupyter Notebook
.ipynb_checkpoints

# IPython
profile_default/
ipython_config.py

# pyenv
#   For a library or package, you might want to ignore these files since the code is
#   intended to run in multiple environments; otherwise, check them in:
# .python-version

# pipenv
#   According to pypa/pipenv#598, it is recommended to include Pipfile.lock in version control.
#   However, in case of collaboration, if having platform-specific dependencies or dependencies
#   having no cross-platform support, pipenv may install dependencies that don't work, or not
#   install all needed dependencies.
#Pipfile.lock

# PEP 582; used by e.g. github.com/David-OConnor/pyflow
__pypackages__/

# Celery stuff
celerybeat-schedule
celerybeat.pid

# SageMath parsed files
*.sage.py

# Environments
.env
.venv
env/
venv/
ENV/
env.bak/
venv.bak/

# Spyder project settings
.spyderproject
.spyproject

# Rope project settings
.ropeproject

# mkdocs documentation
/site

# mypy
.mypy_cache/
.dmypy.json
dmypy.json

# Pyre type checker
.pyre/

# pytype static type analyzer
.pytype/

# Cython debug symbols
cython_debug/''')
    with open('LICENSE', 'w') as f:
        f.write(f'''{checkLicense(ulic.lower())}''')

def buildFlask(name, uname, ghname, ulic):
    pwd = os.getcwd()
    os.mkdir(pwd+f'/{name}')
    os.chdir((os.getcwd())+'/'+name)
    os.mkdir((os.getcwd())+f'/templates')
    os.mkdir((os.getcwd())+f'/static')
    os.mkdir((os.getcwd())+f'/static/images')
    os.mkdir((os.getcwd())+f'/static/styles')
    os.mkdir((os.getcwd())+f'/static/scripts')
    os.system('git init')
    with open(f'app.py', 'w') as f:
        f.write("""from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
	return render_template('index.html')

if __name__=='__main__':
	app.run(debug=True, port=8000)
""")
    with open(f'templates/index.html', 'w') as f:
        f.write(f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{name}</title>
	<link rel="stylesheet" href="./css/style.css">
</head>

<body>
    <h1>Hello World</h1>

	<script src="./js/script.js"> </script>
</body>
</html>""")
        f.close()
    with open('README.md', 'w') as f:
        f.write(f'''# {name}

### Introductiom

### Link

### User Guide

### Snapshots

### Our Team

### Licensing

{ulic.upper()} License

{checkLicense(ulic.lower())}

### Special Notes 
''')
    with open('.gitignore', 'w') as f:
        f.write('''# Byte-compiled / optimized / DLL files
__pycache__/
*.py[cod]
*$py.class

# C extensions
*.so

# Distribution / packaging
.Python
build/
develop-eggs/
dist/
downloads/
eggs/
.eggs/
lib/
lib64/
parts/
sdist/
var/
wheels/
share/python-wheels/
*.egg-info/
.installed.cfg
*.egg
MANIFEST

# PyInstaller
#  Usually these files are written by a python script from a template
#  before PyInstaller builds the exe, so as to inject date/other infos into it.
*.manifest
*.spec

# Installer logs
pip-log.txt
pip-delete-this-directory.txt

# Unit test / coverage reports
htmlcov/
.tox/
.nox/
.coverage
.coverage.*
.cache
nosetests.xml
coverage.xml
*.cover
*.py,cover
.hypothesis/
.pytest_cache/
cover/

# Translations
*.mo
*.pot

# Django stuff:
*.log
local_settings.py
db.sqlite3
db.sqlite3-journal

# Flask stuff:
instance/
.webassets-cache

# Scrapy stuff:
.scrapy

# Sphinx documentation
docs/_build/

# PyBuilder
.pybuilder/
target/

# Jupyter Notebook
.ipynb_checkpoints

# IPython
profile_default/
ipython_config.py

# pyenv
#   For a library or package, you might want to ignore these files since the code is
#   intended to run in multiple environments; otherwise, check them in:
# .python-version

# pipenv
#   According to pypa/pipenv#598, it is recommended to include Pipfile.lock in version control.
#   However, in case of collaboration, if having platform-specific dependencies or dependencies
#   having no cross-platform support, pipenv may install dependencies that don't work, or not
#   install all needed dependencies.
#Pipfile.lock

# PEP 582; used by e.g. github.com/David-OConnor/pyflow
__pypackages__/

# Celery stuff
celerybeat-schedule
celerybeat.pid

# SageMath parsed files
*.sage.py

# Environments
.env
.venv
env/
venv/
ENV/
env.bak/
venv.bak/

# Spyder project settings
.spyderproject
.spyproject

# Rope project settings
.ropeproject

# mkdocs documentation
/site

# mypy
.mypy_cache/
.dmypy.json
dmypy.json

# Pyre type checker
.pyre/

# pytype static type analyzer
.pytype/

# Cython debug symbols
cython_debug/''')
    with open('LICENSE', 'w') as f:
        f.write(f'''{checkLicense(ulic.lower())}''')

def buildCLICK(name, uname, ghname, ulic):
    pwd = os.getcwd()
    os.mkdir(pwd+f'/{name}')
    os.chdir((os.getcwd())+'/'+name)
    os.mkdir((os.getcwd())+f'/{name}')
    os.mkdir((os.getcwd())+f'/tests')
    os.system('pip3 install poetry')
    os.system('git init')
    with open(f'{name}/{name}.py', 'w') as f:
        f.write(f"""import click

@click.group()
@click.version_option('0.1.0', prog_name='{name}')
def main():
    '''Project {name}'''
    pass

if __name__=='__main__':
    main()
""")
    with open(f'{name}/__init__.py', 'w') as f:
        f.write("""__version__ = '0.1.0'""")
    with open(f'tests/__init__.py', 'w') as f:
        f.write("""""")
    with open(f'tests/test_{name}.py', 'w') as f:
        f.write("""from lolacli import __version__

def test_version():
    assert __version__=='0.1.0'""")
        f.close()

    with open('pyproject.toml', 'w') as f:
        f.write(f'''[tool.poetry]
name = "{name}"
version = "0.1.0"
description = "Description here!"
authors = ["{uname} <your email here>"]
license="{ulic.upper()}"
readme="README.md"
homepage= "https://github.com/{ghname}/{name}"
repository = "https://github.com/{ghname}/{name}"
keywords = ["{name}"]

classifiers=[
        "License :: OSI Approved :: {ulic.upper()} License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Operating System :: OS Independent",
    ]


[tool.poetry.dependencies]
python = "^3.8"
click = "^8.0.1"

[tool.poetry.scripts]
{name} = "{name}.{name}:main"

[build-system]
requires = ["poetry-core>=1.0.0"]
build-backend = "poetry.core.masonry.api"''')

    with open('README.md', 'w') as f:
        f.write(f'''# {name}

### Introductiom

### Installation

### User Guide

### Dependencies

- click

### Snapshots

### Our Team

### Licensing

{ulic.upper()} License

{checkLicense(ulic.lower())}

### Special Notes 
''')
    with open('.gitignore', 'w') as f:
        f.write('''# Byte-compiled / optimized / DLL files
__pycache__/
*.py[cod]
*$py.class

# C extensions
*.so

# Distribution / packaging
.Python
build/
develop-eggs/
dist/
downloads/
eggs/
.eggs/
lib/
lib64/
parts/
sdist/
var/
wheels/
share/python-wheels/
*.egg-info/
.installed.cfg
*.egg
MANIFEST

# PyInstaller
#  Usually these files are written by a python script from a template
#  before PyInstaller builds the exe, so as to inject date/other infos into it.
*.manifest
*.spec

# Installer logs
pip-log.txt
pip-delete-this-directory.txt

# Unit test / coverage reports
htmlcov/
.tox/
.nox/
.coverage
.coverage.*
.cache
nosetests.xml
coverage.xml
*.cover
*.py,cover
.hypothesis/
.pytest_cache/
cover/

# Translations
*.mo
*.pot

# Django stuff:
*.log
local_settings.py
db.sqlite3
db.sqlite3-journal

# Flask stuff:
instance/
.webassets-cache

# Scrapy stuff:
.scrapy

# Sphinx documentation
docs/_build/

# PyBuilder
.pybuilder/
target/

# Jupyter Notebook
.ipynb_checkpoints

# IPython
profile_default/
ipython_config.py

# pyenv
#   For a library or package, you might want to ignore these files since the code is
#   intended to run in multiple environments; otherwise, check them in:
# .python-version

# pipenv
#   According to pypa/pipenv#598, it is recommended to include Pipfile.lock in version control.
#   However, in case of collaboration, if having platform-specific dependencies or dependencies
#   having no cross-platform support, pipenv may install dependencies that don't work, or not
#   install all needed dependencies.
#Pipfile.lock

# PEP 582; used by e.g. github.com/David-OConnor/pyflow
__pypackages__/

# Celery stuff
celerybeat-schedule
celerybeat.pid

# SageMath parsed files
*.sage.py

# Environments
.env
.venv
env/
venv/
ENV/
env.bak/
venv.bak/

# Spyder project settings
.spyderproject
.spyproject

# Rope project settings
.ropeproject

# mkdocs documentation
/site

# mypy
.mypy_cache/
.dmypy.json
dmypy.json

# Pyre type checker
.pyre/

# pytype static type analyzer
.pytype/

# Cython debug symbols
cython_debug/''')
    with open('LICENSE', 'w') as f:
        f.write(f'''{checkLicense(ulic.lower())}''')

def buildWebDev(name, uname, ghname, ulic):
    pwd = os.getcwd()
    os.mkdir(pwd+f'/{name}')
    os.chdir((os.getcwd())+'/'+name)
    os.mkdir((os.getcwd())+f'/images')
    os.mkdir((os.getcwd())+f'/styles')
    os.mkdir((os.getcwd())+f'/scripts')
    os.mknod('scripts/script.js')
    os.mknod('styles/style.css')
    os.system('git init')
    with open(f'index.html', 'w') as f:
        f.write(f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{name}</title>
	<link rel="stylesheet" href="./css/style.css">
</head>

<body>
    <h1>Hello World</h1>

	<script src="./js/script.js"> </script>
</body>
</html>""")
        f.close()
    with open('README.md', 'w') as f:
        f.write(f'''# {name}

### Introductiom

### Link

### User Guide

### Snapshots

### Our Team

### Licensing

{ulic.upper()} License

{checkLicense(ulic.lower())}

### Special Notes 
''')
    with open('LICENSE', 'w') as f:
        f.write(f'''{checkLicense(ulic.lower())}''')


if __name__=='__main__':
    pass