from setuptools import setup,find_packages
from typing import List

HYPHEN_E = "-e ."

def get_requiremnts(file_path:str)->List[str]:
    '''
    return the list of requirements
    '''
    requirements = []
    with open(file_path) as file_obj:
        requirements= file_obj.readlines()
        requirements= [req.replace("\n", " ") for req in requirements] #replace \n with blank for each line in  requirements.txt file
        if HYPHEN_E in requirements:
               requirements.remove(HYPHEN_E)




setup( 
name="MLProjects",
version='0.0.1',
author="Parveen-Lehal",
author_email= "parveen.lehal.kaur@gmail.com",
packages=find_packages(),
install_requires = get_requiremnts('requirements.txt') #get_requiremnts is a function that fetch all the package or libraries mentiones in requirements.txt file
)