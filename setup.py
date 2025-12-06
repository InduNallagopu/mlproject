from __future__ import annotations
from setuptools import find_packages,setup
from typing import List

HYPEN_E_DOT='-e .'
def get_requirements(file_path:str)->list[str]:
    '''
    this function returns a list of requirements
    '''

    requirements=[]
    with open(file_path) as file_obj:
        requirements=file_obj.readlines()
        requirements=[req.replace("\n"," ") for req in requirements]  #readlines by default add \n to new line ..to replace that we use replace method
        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)

    return requirements
setup(
    name="mlproject",
    version='0.0.1',
    author='indu',
    author_email='indunallagopu@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')
)