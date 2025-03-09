Reproducing experiments from https://flower.ai/docs/baselines/fedavgm.html


## Environment Setup

```bash
# Cd to your baseline directory (i.e. where the `pyproject.toml` is)
cd yourrepofolder/flower/baselines/fedavgm
# then:
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
You can run install the requirements file located in `/yourrepofolder/` or individually install the following:

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

#### Concentration levels to generate data distribution
The linear plot has been run with the following experiments (if the strategy is not specified, the default is `strategy=custom-fedavgm`):
```bash
# Modifying the concentration levels
poetry run python -m fedavgm.main dataset=cifar10 noniid.concentration=10
```
Then, transforming the results from pickle (.pkl) file to JSON file so they could be stored in a readable way at `experimentresults.md` and in their individual locations on their *outputs* folder.

Next, run the concentration plot `poetry run python -m fedavgm.utils` to observe and compare results. We have found out that we obtain the exact same results with exception to the plot with concentration levels of 1e-9. Find here the picture with reproducing results.
(Saved at /.../flower/baselines/fedavgm/_static/concentration_cifar10_v3.png)

### CIFAR-10 FedAvg vs. Custom FedAvgM
The paper we are reproducing evaluated the strategies on the CIFAR-10 dataset for 10,000 rounds. We tried executing the same command but, with our compute resources, we got to 325 rounds in 4 hours. We decided to evaluate the strategy with less rounds and see what results we got. We evaluated with 5 and 50 number of rounds, with 50 it took approximately 15 minutes per concentration level.

The results are based on the accuracy measure for every concentration level by comparing the strategies FedAvg and Custom FedAvgM. 

Since we could not run the number of rounds specified in the paper, we added a comparison of accuracy results depending on the number of evaluation round.

#### Running commands
Here are the commands used for the different number of evaluation runs. To run with different concentration levels you only need to change the `noniid.concentration=` at every run.

- Number of rounds 5:
With this command we changed the strategy to `strategy=custom-fedavgm` after running all different concentration levels with the strategy `fedavg`.
```bash
poetry run python -m fedavgm.main strategy=fedavg dataset=cifar10 noniid.concentration=10 num_rounds=5
```

- Number of rounds 50:
With this command we evaluate both methods in a single run.
```bash
poetry run python -m fedavgm.main --multirun client.local_epochs=1 noniid.concentration=0.01 strategy=custom-fedavgm,fedavg \
server.reporting_fraction=0.05 num_rounds=50 num_clients=100 \
dataset=cifar10 client.lr=0.003 server.momentum=0.9
```

#### Reading and storing results
The `fedavgm.main` implementation from the `FedAvgM` baseline of the `Flower` framework automatically saves a pickle (`.pkl`) file of every exectution using the *Hydra* library. The results are stored in the *multirun* folder using the date and time of execution. 

We implemented a *Python* script to read the pickle files into a *JSON* format, we moved them to another folder called `multirun-jsonresults` where we had two files for the two strategies (custom-fedavgm and fedavg), in there we stored all the corresponding pickle files. To run the script that transforms pickle files to JSON format go to `yourrepofolder/` run:
```bash
python3 viewpickle.py flower/baselines/fedavgm/multirun/(yourdate)/(yourtime)
```

Then, we implemented a function that reads the JSON file values, for every file located in each method folder, reads the loss and accuracy, and adds them into a list of values. This list of values is used to plot the results plots of the next subsection.
 
### Results plots
The plots compare the methods FedAvg and Custom FedAvgM with different concentration levels based on their accuracy and loss values. The paper we are reproducing does not plot the loss values, but we decided to add it to see if we could gain any insight.

#### Accuracy results
Figure 1 is the paper results comparison:

Figure 2 is the results of evaluating with 5 number of rounds:

Figure 3 is the results of evaluating with 50 number of rounds: