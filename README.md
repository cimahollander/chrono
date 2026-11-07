# ChronoRisk

ChronoRisk provides research components for longitudinal risk-tier modelling, biosensor fusion, offline reinforcement learning, and evaluation of chronic conditions after spinal-cord injury.

## Installation

```bash
pip install -e ".[dev]"
```

## Data and execution

Patient records, biosensor data, and trained weights are not included. Dataset-specific loaders must be implemented before training, evaluation, inference, or export can use patient records. These workflows currently stop with an error when the data are unavailable. The manuscript's reported results have not been reproduced using this repository.

`charts` defines data structures and batching; `reckoning` contains the temporal encoder; `bearings` and `fix` contain biosensor and fusion components; `conn` contains the policy; `passageplan` contains training; `soundingcheck` contains evaluation metrics. Configurations are in `legs/`.

The dataset registry is available via `python -m chronorisk.bridge chart`; each source's access and usage terms apply.

```bash
make test
```

This is research software and has not been validated for clinical use.
