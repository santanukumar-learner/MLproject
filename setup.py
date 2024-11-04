from setuptools import find_packages, setup
from typing import List


def get_requirements(file_path:str) -> List[str]:
    requirements = []
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        [req.replace("\n", "") for req in requirements]
        
        if "-e ." in requirements:
            requirements.remove("-e .")
    return requirements 
  
setup( 
    name = "mlproject",
    version = "0.0.1",
    author = "Santanu",
    author_email = "santanukumaradhikari07@gmail.com",
    package = find_packages(),
    install_requirement = get_requirements("Requirement.txt") 
    
)