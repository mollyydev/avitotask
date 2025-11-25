from typing import List

import aiohttp


async def get_matrix(url: str) -> List[int]:
    """
    Fetches a matrix from a URL, traverses it in a counter-clockwise spiral,
    and returns the result as a list of integers.

    Args:
        url: The URL to fetch the matrix from.

    Returns:
        A list of integers representing the spiral traversal of the matrix.
        Returns an empty list if an error occurs or the matrix is invalid.
    """
    try:
        async with aiohttp.ClientSession() as session:
            async with session.get(url) as response:
                response.raise_for_status()  # Raises HTTPError for 4xx/5xx responses
                matrix_str = await response.text()
    except aiohttp.ClientError as e:
        print(f"A network or HTTP error occurred: {e}")
        return []

    try:
        # Parse the matrix string into a 2D list of integers
        rows = matrix_str.strip().split('\n')
        matrix = []
        for row_str in rows:
            if row_str.startswith('+'):
                continue
            # Clean the row, split by '|', filter empty strings, and convert to int
            cleaned_row = [int(num.strip()) for num in row_str.split('|') if num.strip()]
            if cleaned_row:
                matrix.append(cleaned_row)

        if not matrix or not all(len(row) == len(matrix) for row in matrix):
            print("Invalid or non-square matrix.")
            return []
    except (ValueError, TypeError):
        print("Failed to parse matrix content.")
        return []


    # Perform counter-clockwise spiral traversal
    result = []
    n = len(matrix)
    top, bottom, left, right = 0, n - 1, 0, n - 1

    while left <= right and top <= bottom:
        # 1. Traverse down the left column
        for i in range(top, bottom + 1):
            result.append(matrix[i][left])
        left += 1

        # 2. Traverse right across the bottom row
        for i in range(left, right + 1):
            result.append(matrix[bottom][i])
        bottom -= 1

        # 3. Traverse up the right column
        if top <= bottom:
            for i in range(bottom, top - 1, -1):
                result.append(matrix[i][right])
            right -= 1

        # 4. Traverse left across the top row
        if left <= right:
            for i in range(right, left - 1, -1):
                result.append(matrix[top][i])
            top += 1

    return result
