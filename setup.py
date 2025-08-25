from setuptools import find_packages, setup
from typing import List

HYPEN_E_DOT = '-e .'

def get_requirements(file_path: str) -> List[str]:
    '''
    This function will return a list of requirements from the requirements.txt file.
    '''
    requirements = []
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        # Remove newline characters from each requirement
        requirements = [req.replace('\n', '') for req in requirements]

        # Remove the '-e .' entry if it exists
        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)
            
    return requirements

setup(
    name='MLproject',
    version='0.0.1',
    author='Mahesh',
    author_email='ardhimahesh96@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')
)