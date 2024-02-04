# Build your entire ML & PythonPyPl

from setuptools import find_packages, setup
from typing import List

HYPHEN_E_DOT = '-e .'

def get_requirements(file_path:str)->List[str]:
    '''
    This function will return the list of requirements.
    '''
    requirements = []
    with open(file_path) as file_obj:
        requirements = file_obj.readlines() # this will get '\n'
        requirements = [req.replace("\n", "") for req in requirements]

        # NOTICE THAT WE NEED -e ., but it should not be included later
        if HYPHEN_E_DOT in requirements:
            requirements.remove(HYPHEN_E_DOT)
    print(requirements)
    return requirements

# Every time you install, comment out the -e . otherwise the packages of the entire project will keep rebuilding over and over.
# Remember, this just tells pip to install the requirements specified in setup.py (which is this)
# -e . flag in requirements.txt means that it is editable(?) - but basically connects it to setup.py

# By writing words such as pandas, numpy, and seaborn before the flag
# Run pip install -r requirements.txt to start download the packages

setup(
    name='mlproject',
    version='0.0.1',
    author='Ethan Tran',
    author_email='e.tran.8714@gmail.com',
    packages=find_packages(), # this is essentially looking for __init__.py
    install_requires=get_requirements('requirements.txt')
)