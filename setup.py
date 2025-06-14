from setuptools import find_packages, setup
from typing import List

# just a variable
hyphen_e_dot = "-e."

def get_requirements(file_path: str) -> List[str]:
    """
    This will return list of requirements
    """
    requirements = []
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.replace("\n", "") for req in requirements]
        if hyphen_e_dot in requirements:
            requirements.remove(hyphen_e_dot)
    return requirements

setup(
    name="sampleml",
    version='0.0.1',
    author='skx',
    author_email="sonukmr0147@gmail.com",
    packages=find_packages(),
    install_requires=get_requirements("requirements.txt")
)
