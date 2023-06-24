# LLM-Solutions-Playbook

[![Python code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
[![license: MIT](https://img.shields.io/badge/License-MIT-purple.svg)](LICENSE)

Explore real-world applications, save time, and unlock the potential of AI-driven solutions with Large Language Models!

This repository showcases the transformative capabilities of Large Language Models and LangChain. Dive into a collection of Jupyter notebooks that demonstrate the practical applications of these technologies, highlighting their time-saving potential and the power of AI-driven solutions.


## Requirements
Python 3.x
Dependencies (listed in [requirements.txt](./requirements.txt))

## Installation
Clone this repository to your local machine.
Install the required dependencies by running `pip install -r requirements.txt`.

## Usage
The [notebooks](./notebooks/) directory contains a set of Jupyter notebooks that demonstrate the functionality of this repository. The notebooks are organized by topic and can be run in any order. The notebooks are designed to be self-contained and can be run independently of each other.

### Get OpenAI API Key
To use the OpenAI API, you will need to create an account and obtain an API key. You can create an account [here](https://platform.openai.com/). Once you have created an account, you can find your API key on the [API Keys page](https://platform.openai.com/account/api-keys).

### Use OpenAI API Key
Follow the instructions below to use your OpenAI API Key securely within code:
1. Create a file named `.env` in the root directory of this repository.
2. Define the environment variable `OPENAI_API_KEY` in the `.env` file and set it equal to your OpenAI API key. For example, if your API key is `abc123`, then the contents of the `.env` file should be `OPENAI_API_KEY="abc123"`.
3. Use the following code to load your API key from the `.env` file:
```python
import os
from dotenv import load_dotenv
import openai

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")
```

## Contributing
Contributions are welcome! If you have any suggestions, bug reports, or feature requests, please open an issue or submit a pull request. See the [CONTRIBUTING.md](./CONTRIBUTING.md) file for more information.

## License
This project is licensed under the [MIT License](./LICENSE).

## Disclaimer
Please note that this software is provided as-is, and the author and contributors shall not be held responsible for any consequences or damages arising from its use. Refer to the [DISCLAIMER.md](./DISCLAIMER.md) file for more information.