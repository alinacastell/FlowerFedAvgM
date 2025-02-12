# Experiment results

## Specifying parameters, command line runs and results

Results for `CustomFedAvgM_cifar10_clients=10_rounds=5_C=0.05_E=1_alpha=0.1_server-momentum=0.9_client-lr=0.01_acc=0.1000` are:
```
{'history': History (loss, centralized):
    round 5: nan
    History (metrics, centralized):
        {'accuracy': [(5, 0.10000000149011612)]}
        }
```

Results for `CustomFedAvgM_fmnist_clients=10_rounds=5_C=0.05_E=1_alpha=10_server-momentum=0.9_client-lr=0.01_acc=0.6613` are:
```
{'history': History (loss, centralized):
    round 5: 4.052677154541016
    History (metrics, centralized):
        {'accuracy': [(5, 0.661300003528595)]}
        }
```

Results for `CustomFedAvgM_fmnist_clients=10_rounds=5_C=0.05_E=1_alpha=1_server-momentum=0.9_client-lr=0.01_acc=0.7594` are:
```
{'history': History (loss, centralized):
    round 5: 3.8018031120300293
    History (metrics, centralized):
        {'accuracy': [(5, 0.7594000101089478)]}
        }
```

#### CIFAR-10

Results for Concentration=1e-9 `CustomFedAvgM_cifar10_clients=10_rounds=5_C=0.05_E=1_alpha=1e-09_server-momentum=0.9_client-lr=0.01_acc=0.1000` are:
```
{'history': History (loss, centralized):
    round 5: nan
    History (metrics, centralized):
        {'accuracy': [(5, 0.10000000149011612)]}
        }
```

Results for Concentration=1e-5 `CustomFedAvgM_cifar10_clients=10_rounds=5_C=0.05_E=1_alpha=1e-05_server-momentum=0.9_client-lr=0.01_acc=0.1000` are:
```
{'history': History (loss, centralized):
    round 5: nan
    History (metrics, centralized):
        {'accuracy': [(5, 0.10000000149011612)]}
        }
```

Results for Concentration=0.01 `CustomFedAvgM_cifar10_clients=10_rounds=5_C=0.05_E=1_alpha=0.01_server-momentum=0.9_client-lr=0.01_acc=0.1258` are:
```
{'history': History (loss, centralized):
    round 5: 12.464190483093262
    History (metrics, centralized):
        {'accuracy': [(5, 0.1257999986410141)]}
        }
```

Results for Concentration=0.1 `CustomFedAvgM_cifar10_clients=10_rounds=5_C=0.05_E=1_alpha=0.1_server-momentum=0.9_client-lr=0.01_acc=0.1000` are:
```
{'history': History (loss, centralized):
    round 5: nan
    History (metrics, centralized):
        {'accuracy': [(5, 0.10000000149011612)]}
        }
```

Results for Concentration=1 `CustomFedAvgM_cifar10_clients=10_rounds=5_C=0.05_E=1_alpha=1_server-momentum=0.9_client-lr=0.01_acc=0.3448` are:
```
{'history': History (loss, centralized):
    round 5: 5.396591663360596
    History (metrics, centralized):
        {'accuracy': [(5, 0.3447999954223633)]}
}
```

Results for Concentration=10 `CustomFedAvgM_cifar10_clients=10_rounds=5_C=0.05_E=1_alpha=10_server-momentum=0.9_client-lr=0.01_acc=0.4238` are:
```
{'history': History (loss, centralized):
        round 5: 4.822487831115723
History (metrics, centralized):
{'accuracy': [(5, 0.423799991607666)]}}
```