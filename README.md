# LLM-Solutions-Playbook

[![Python code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
[![license: MIT](https://img.shields.io/badge/License-MIT-purple.svg)](LICENSE)

Unlock the potential of AI-driven solutions and delve into the world of Large Language Models. Explore cutting-edge concepts, real-world applications, and best practices to build powerful systems with these state-of-the-art models.

This repository showcases the transformative capabilities of Large Language Models and LangChain. Dive into a curated collection of Jupyter notebooks that demonstrate:
- the practical applications of these technologies, highlighting their time-saving potential and the power of AI-driven solutions.
- cutting-edge concepts and best practices to build powerful systems with these state-of-the-art models.

Unleash your creativity and explore the included resources to kickstart your journey and delve deeper into these groundbreaking technologies.

## Requirements
Python 3.11
Dependencies (listed in [requirements.txt](./requirements.txt))

## Installation
Clone this repository to your local machine.
Install the required dependencies by running `pip install -r requirements.txt`.

## Usage
The [notebooks](./notebooks/) directory is organized into sub-directories, each dedicated to a specific topic. You can explore these sub-directories in any order based on your interests. Each sub-directory contains a collection of Jupyter notebooks that delve into the concepts related to its respective topic. The notebooks are sequentially ordered within each sub-directory, so it is recommended to follow the suggested order. The notebooks are designed to be self-contained, allowing you to run them independently without dependencies on other notebooks.

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

### Get Activeloop API Key
- Signup/Login to [Activeloop](https://www.activeloop.ai/).
- Create API token from the home page.
- Copy the API token and paste it in the .env file like this `ACTIVELOOP_TOKEN="<token>"`.
- Use the similar code as shown above to load your API token from the `.env` file.

## Contributing
Contributions are welcome! If you have any suggestions, bug reports, or feature requests, please open an issue or submit a pull request. See the [CONTRIBUTING.md](./CONTRIBUTING.md) file for more information.

## License
This project is licensed under the [MIT License](./LICENSE).

## Disclaimer
Please note that this software is provided as-is, and the author and contributors shall not be held responsible for any consequences or damages arising from its use. Refer to the [DISCLAIMER.md](./DISCLAIMER.md) file for more information.

## Additional Resources
- [The Novice's LLM Training Guide](https://rentry.org/llm-training)
- [Mastering LLM Techniques: Inference Optimization](https://developer.nvidia.com/blog/mastering-llm-techniques-inference-optimization)
- [LLM Patterns](https://eugeneyan.com/writing/llm-patterns/)
- [Deep Dive into evals](https://eugeneyan.com/writing/abstractive/)
- [Design Patterns in Machine Learning Code and Systems](https://eugeneyan.com/writing/design-patterns/)
- [More Design Patterns For Machine Learning Systems](https://eugeneyan.com/writing/more-patterns/)