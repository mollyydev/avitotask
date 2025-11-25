# Avito Python Trainee Assignment

This project is a solution to the Avito Python Trainee assignment. It provides a library to fetch a square matrix from a URL, parse it, and return a list of integers representing a counter-clockwise spiral traversal of the matrix.

## Features

- Asynchronously fetches a matrix from a URL using `aiohttp`.
- Parses the matrix from a string format.
- Traverses the matrix in a counter-clockwise spiral pattern.
- Handles network and HTTP errors gracefully.
- Includes a test case for verification.

## Requirements

- Python 3.7+
- aiohttp
- pytest-asyncio

## Installation

1.  Clone the repository:
    ```bash
    git clone https://github.com/mollyydev/avitotask.git 
    cd AvitoTask
    ```
2.  Install the dependencies:
    ```bash
    pip install aiohttp
    ```
    Or install use poetry:
    ```bash
    poetry install
    ```

## Usage

The main functionality is provided by the `get_matrix` function in `main.py`.

```python
import asyncio
from src.main import get_matrix


async def main():
    url = 'https://raw.githubusercontent.com/avito-tech/python-trainee-assignment/main/matrix.txt'
    traversal = await get_matrix(url)
    print(traversal)


if __name__ == "__main__":
    asyncio.run(main())
```
Or run
```bash
  cd src && python example.py
  ```

### Running the Test

To run the included test case, simply execute the `test_main.py` file:

```bash
cd src/tests && python test_main.py
```

This will fetch the matrix from the `SOURCE_URL`, perform the spiral traversal, and print the result, comparing it against the expected output.
