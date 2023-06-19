# Contributing

This repository is entirely open source and welcomes contributions! Please read through the contributing guide below to avoid frustration!

## Issues

All forms of feedback are welcome through [issues](https://github.com/iamrk04/<repo_name>/issues/new)

## Repository Structure

The [`notebooks`](./notebooks/) directory is intended for iterative, interactive code development examples. The notebooks are organized by topic and can be run in any order. The notebooks are designed to be self-contained and can be run independently of each other. Each notebook **must** contain `Troubleshooting` section at the end of the notebook. This section should contain the common errors that can occur while running the notebook and their solutions.

## Pull Requests

Pull requests are welcome! Please follow the guidelines below to ensure that your pull request is accepted.

### Set up

Clone the repository and install the required Python packages for contributing:

```terminal
git clone https://github.com/iamrk04/<repo_name>.git
cd <repo_name>
pip install -r requirements.txt
```

Before opening a PR, format all Python code and notebooks:

```terminal
black .
black-nb .
```