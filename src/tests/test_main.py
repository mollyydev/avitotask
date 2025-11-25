import pytest

from src import get_matrix

# Test case data
SOURCE_URL = 'https://raw.githubusercontent.com/avito-tech/python-trainee-assignment/main/matrix.txt'
EXPECTED_TRAVERSAL = [
    10, 50, 90, 130,
    140, 150, 160, 120,
    80, 40, 30, 20,
    60, 100, 110, 70,
]


@pytest.mark.asyncio
async def test_get_matrix_success():
    """
    Tests the successful fetching and traversal of the matrix.
    """
    traversal = await get_matrix(SOURCE_URL)
    assert traversal == EXPECTED_TRAVERSAL


@pytest.mark.asyncio
async def test_get_matrix_invalid_url():
    """
    Tests the function's behavior with an invalid URL.
    """
    traversal = await get_matrix("https://invalid-url-that-does-not-exist.com")
    assert traversal == []


@pytest.mark.asyncio
async def test_get_matrix_server_error():
    """
    Tests the function's behavior when a server error occurs.
    """
    # This URL will return a 500 error
    error_url = "http://httpstat.us/500"
    traversal = await get_matrix(error_url)
    assert traversal == []
