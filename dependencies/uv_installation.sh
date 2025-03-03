echo 'Installing uv...'
curl -LsSf https://astral.sh/uv/install.sh | sh

echo 'Installing Python 3.12 with uv...'
uv python install 3.12

echo 'Initializing uv project...'
echo "3.12" > .python-version
python convert_requirements.py

echo 'Creating a uv venv virtual environment with Python 3.12...'
uv venv --python=3.12 .venv

echo 'Activating the venv virtual environment...'
source .venv/bin/activate

echo 'Installing Python dependencies with uv...'
uv sync

echo 'Creating a Jupyter notebook kernel using the uv venv...'
python -m ipykernel install --user --name 'dkhundley_venv' --display-name 'dkhundley_venv'

echo 'uv installation complete!'
