# version-control
Repository to store the Version Control Exercise for OPAN 3244
#example running code
```bash
python example.py

## Usage
Unemployment report:
```sh
Stocks report:
```sh
python -m app.stocks
```

## Setup

Create virtual environment:
```sh
conda create -n ump-env python=3.11
```
Activate the environment:
```sh
conda activate ump-env
```
Install packages:
```sh
#pip install requests
#pip install plotly
#pip install python-dotenv
# best practice to list the packages in the requirements.txt file:
pip install -r requirements.txt
```
## Testing
Run tests:
```sh
pytest
```

## Running Tests
After installing the dependencies, you can run tests with the following command:
```bash
pytest

## Commit 12
Run the web app (then view in the browser at http://localhost:5000/):
```sh

FLASK_APP=web_app flask run
