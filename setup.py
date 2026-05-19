
from setuptools import find_packages,setup

from typing import List

def getrequirements() -> List[str]:
    """
       This function will return list of requirements from requirements.txt file
    """

    requirements_lst:List[str] = []
    try:
        with open("requirements.txt", "r") as file:
            # read line from the file 
            lines = file.readlines()
            for line in lines:
                requirement = line.strip()
                ## ignore empty lines and -e .
                if requirement and requirement != '-e .':
                    requirements_lst.append(requirement)    
    except FileNotFoundError:
        print("requirements.txt file not found")                

    return requirements_lst




setup(
    name = "Network_Secuarity",
    version = "0.0.1",
    author = "Puneet Chhonker",
    author_email = "puneetchhonker513@gmail.com",
    packages = find_packages(),
    install_requires = getrequirements()
)
