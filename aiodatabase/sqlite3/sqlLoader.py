"""
A module to load SQL queries from a file.
"""

from typing import Dict, Optional


class SqlLoader:
    """
    A class to load SQL queries from a file.
    """

    def __init__(self, file_path: str) -> None:
        """
        Initialize the SqlLoader with the file path.

        Args:
            file_path (str): The path to the SQL file.
        """
        self.file_path = file_path
        self.queries = self.load_sql_queries(file_path)

    def load_sql_queries(self, file_path: str) -> Dict[str, str]:
        """
        Load SQL queries from a file.

        Args:
            file_path (str): The path to the SQL file.

        Returns:
            dict: A dictionary containing SQL queries.
        """
        queries: Dict[str, str] = {}
        with open(file_path, "r", encoding="utf-8") as file:
            query = ""
            key: Optional[str] = None
            for line in file:
                if line.startswith("-- #{"):
                    key = line.strip().split()[2]
                    query = ""
                elif line.startswith("-- #}"):
                    queries[key] = query.strip()
                    query = ""
                    key = None
                else:
                    query += line
        return queries
