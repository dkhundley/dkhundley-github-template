# Importing the necessary Python libraries
import re

# Read requirements.txt
with open("dependencies/requirements.txt", "r") as f:
    lines = f.readlines()

# Initializing pyproject.toml content
pyproject_toml = """[tool.uv.dependencies]
"""

# Setting the Regex pattern for package extraction
pattern = re.compile(r"^([a-zA-Z0-9_\-]+)([>=<]=?[\d\.\*]+)?")

# Extracting package and version from requirements.txt
for line in lines:
    line = line.strip()
    if not line or line.startswith("#"):  # Skip empty lines and comments
        continue

    match = pattern.match(line)
    if match:
        package, version = match.groups()
        version_str = f' = "{version}"' if version else ' = "*"'
        pyproject_toml += f'{package}{version_str}\n'

# Writing to pyproject.toml
with open("pyproject.toml", "w") as f:
    f.write(pyproject_toml)
