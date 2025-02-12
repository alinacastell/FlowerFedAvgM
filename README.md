Reproducing experiments from https://flower.ai/docs/baselines/fedavgm.html


## Environment Setup

```bash
# Cd to your baseline directory (i.e. where the `pyproject.toml` is), then
pyenv local 3.10.6

# Set that version for poetry
poetry env use 3.10.6

# Install the base Poetry environment
poetry install

# Install the `shell` plugin via Poetry
poetry self add poetry-plugin-shell

# Activate the environment
poetry shell

# To deactivate environment
exit
```

Check that environment is activated
```bash
# Command line should start with
(fedavgm-py3.10) (base) user@name fedavgm % 
``` 

## Installation
```bash
python -m pip install flwr
pip install hydra-core --upgrade

# Install correct version of numpy
# First uninstall previous version
pip uninstall numpy
pip install numpy==1.26.4

# Install TensorFlow
pip install tensorflow
```

Ensure that there are no conflicts with the libraries by running `pip check`. Solve if any conflicts arise.

## Running the Experiments
Make sure that you are on the correct directory of the `flower` repository: `cd /.../flower/baselines/fedavgm` and that the Poetry environment is activated from this directory `poetry shell`
