# Dummy Ci
Sample CI created by Krishna Pandian

# GitHooks
## Installation
```git config core.hookspath "./.githooks```

## Sample Hooks
- commit-msg
    * This githook is designed to validate commit messages to include insightful keywords
- pre-commit
    * This githooks validates you are adhering to valid branch naming

# Local Development
## Virtual Environment
- Virtual Environements are highly encouraged for maintainence of this project (Any virtualenv should work but this demo will use venv)
- Install [python 3.7](https://www.python.org/downloads/) and [pip](https://pip.pypa.io/en/stable/installation/)
- Once pip is installed run `pip3 install venv`
- From the main directory of this repo run `python3 -m venv <venv_name>`
- Finally run `source <venv_name>/Scripts/activate` to activate the virtual environment

## Dependencies
### Installing New Dependencies
- To install all the dependencies from your main directory of this repo run `pip3 install -r requirements.txt`
- To install packages created in this project run `pip3 install -e .`

### Adding New Dependencies
- To add a new dependency `pip3 install <dependency_name>`
- To add a new dependency to requirements.txt run `pip freeze > requirements.txt` in the main directory of this repo

### Creating Local Packages
- When creating packages for local access, update [setup.py](./setup.py) as necessary

# Testing
- This application utilizes pytest to provide unit tests, integration test, and coverage
- To run all the unit tests run `pytest tests/` from the home directory of this repository

# Linting
- This application code standards are maintained with pylint
- To run a lint of the entire repository run `pylint` from the home directory of this repository
