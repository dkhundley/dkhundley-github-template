# Importing the necessary Python libraries
import re

# Reading requirements.txt
with open("dependencies/requirements.txt", "r") as f:
    lines = f.readlines()

# Initializing pyproject.toml content
pyproject_toml = """[project]
name = "my_project"
version = "0.0.1"
description = "Add your description here"
readme = "README.md"
requires-python = ">=3.12"
dependencies = [
"""

# Defining regex pattern for extracting package names and versions
pattern = re.compile(r"^([a-zA-Z0-9_\-]+)([>=<]=?[\d\.\*]+)?")

dependencies = []

# Processing each line in requirements.txt
for line in lines:
    line = line.strip()
    if not line or line.startswith("#"):  # Skipping empty lines and comments
        continue

    match = pattern.match(line)
    if match:
        package, version = match.groups()
        version_str = f'"{package}{version}"' if version else f'"{package}"'
        dependencies.append(version_str)

# Formatting dependencies into the TOML file
pyproject_toml += ",\n    ".join(dependencies) + "\n]\n"

# Writing to pyproject.toml
with open("pyproject.toml", "w") as f:
    f.write(pyproject_toml)
