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
Make sure that you are on the correct directory of the `flower` repository: `cd /.../flower/baselines/fedavgm` and that the Poetry environment is activated `poetry shell` from this directory.

Then, run:
```python
# this will run with the default setting
poetry run python -m fedavgm.main 
```

The linear plot has been run with the following experiments (if the strategy is not specified, the default is `strategy=custom-fedavgm`):
```bash
# Modifying the concentration levels
poetry run python -m fedavgm.main dataset=cifar10 noniid.concentration=10
```
Then, transforming the results from pickle (.pkl) file to JSON file so they could be stored in a readable way at `experimentresults.md` and in their individual locations on their *outputs* folder.

Next, run the concentration plot `poetry run python -m fedavgm.utils` to observe and compare results. We have found out that we obtain the exact same results with exception to the plot with concentration levels of 1e-9. Find here the picture with reproducing results.
(Saved at /.../flower/baselines/fedavgm/_static/concentration_cifar10_v3.png)

After that, used the accuracy results for plotting with respect to the method FedAvgM using the following commmand line:
```bash
poetry run python -m fedavgm.main strategy=fedavg dataset=cifar10 noniid.concentration=10
```