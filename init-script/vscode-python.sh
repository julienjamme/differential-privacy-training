sudo apt update -y
sudo apt install tree -y

# Clone project
cd ~/work/
git clone https://github.com/julienjamme/differential-privacy-training.git
cd ~/work/differential-privacy-training/

# data 
mkdir data/
mc cp s3/julienjamme/public/population_974_filo_rebuild.gpkg data/population_974.gpkg
mc cp s3/julienjamme/public/commune_dep_974_2019.gpkg data/commune_dep_974_2019.gpkg
mc cp s3/julienjamme/public/population_974_filo_rebuild.yaml data/population_974.yaml

# Install project (requirements and main package)
pip install -e .

# Replace default flake8 linter with project-preconfigured ruff
code-server --uninstall-extension ms-python.flake8
code-server --install-extension charliermarsh.ruff

# Install the mypy type checking extension and run type checking
pip install mypy
yes | mypy --install-types .
code-server --install-extension ms-python.mypy-type-checker

# Install and setup pre-commit
pip install pre-commit
pre-commit install
pre-commit run --all-files

# Download data
# python scripts/download_FILO.py
# python scripts/download_BAN.py
