import asyncio

from src import get_matrix

# Test case data
SOURCE_URL = 'https://raw.githubusercontent.com/avito-tech/python-trainee-assignment/main/matrix.txt'
EXPECTED_TRAVERSAL = [
    10, 50, 90, 130,
    140, 150, 160, 120,
    80, 40, 30, 20,
    60, 100, 110, 70,
]


async def matrix():
    traversal = await get_matrix(SOURCE_URL)
    print(traversal)

if __name__ == '__main__':
    asyncio.run(matrix())