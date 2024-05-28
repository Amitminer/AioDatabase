"""
This module provides the Database class for managing database operations.
"""

from typing import Optional, Any, Dict, Union, Tuple, List
from .sqlite3.sqlLoader import SqlLoader
from .dataConnector import DataConnector


class Database:
    """
    A class to manage database operations.

    Attributes:
        configPath (str): The path to the configuration file.
        sqlFile (str): The path to the SQL file.
        sql_loader (SqlLoader): An instance of SqlLoader for loading SQL queries.
        conn: The database connection.
        cursor: The database cursor.
    """

    def __init__(self) -> None:
        """
        Initializes the Database class.
        """
        self.configPath: Optional[str] = None
        self.sqlFile: Optional[str] = None
        self.sql_loader: Optional[SqlLoader] = None
        self.conn: Optional[Any] = None
        self.cursor: Optional[Any] = None

    async def connect(self, configPath: str, sqlFile: str) -> None:
        """
        Connects to the database.

        Args:
            configPath (str): The path to the configuration file.
            sqlFile (str): The path to the SQL file.
        """
        self.configPath = configPath
        self.sqlFile = sqlFile
        await DataConnector.connect(configPath)
        self.conn = DataConnector.conn
        self.cursor = await DataConnector.get_cursor()
        self.sql_loader = SqlLoader(sqlFile)
        await self.create_table("create_table")

    async def close(self) -> None:
        """
        Closes the database connection.
        """
        if self.conn:
            await self.conn.close()

    async def commit(self) -> None:
        """
        Commits the current transaction.
        """
        if self.conn:
            await self.conn.commit()

    async def execute(
        self, query_key: str, params: Optional[Union[Tuple, Dict[str, Any]]] = None
    ) -> None:
        """
        Executes a SQL query.

        Args:
            query_key (str): The key of the SQL query.
            params (Optional[Union[Tuple, Dict[str, Any]]]): The parameters to be passed to the query.
        """
        query = self.sql_loader.queries.get(query_key)
        if not query:
            raise ValueError(f"No query found for key '{query_key}'")
        if params is None:
            await self.cursor.execute(query)
        else:
            await self.cursor.execute(query, params)
        await self.commit()

    async def fetchall(
        self, query_key: str, params: Optional[Union[Tuple, Dict[str, Any]]] = None
    ) -> List[Tuple]:
        """
        Fetches all rows resulting from a SQL query.

        Args:
            query_key (str): The key of the SQL query.
            params (Optional[Union[Tuple, Dict[str, Any]]]): The parameters to be passed to the query.

        Returns:
            List[Tuple]: A list of tuples representing the fetched rows.
        """
        query = self.sql_loader.queries.get(query_key)
        if not query:
            raise ValueError(f"No query found for key '{query_key}'")
        if params is None:
            await self.cursor.execute(query)
        else:
            await self.cursor.execute(query, params)
        return await self.cursor.fetchall()

    async def fetchone(
        self, query_key: str, params: Optional[Union[Tuple, Dict[str, Any]]] = None
    ) -> Tuple:
        """
        Fetches one row resulting from a SQL query.

        Args:
            query_key (str): The key of the SQL query.
            params (Optional[Union[Tuple, Dict[str, Any]]]): The parameters to be passed to the query.

        Returns:
            Tuple: A tuple representing the fetched row.
        """
        query = self.sql_loader.queries.get(query_key)
        if not query:
            raise ValueError(f"No query found for key '{query_key}'")
        if params is None:
            await self.cursor.execute(query)
        else:
            await self.cursor.execute(query, params)
        return await self.cursor.fetchone()

    async def create_table(self, query_key: str) -> None:
        """
        Creates a table in the database.

        Args:
            query_key (str): The key of the SQL query for creating the table.
        """
        query = self.sql_loader.queries.get(query_key)
        if not query:
            raise ValueError(f"No query found for key '{query_key}'")
        await self.cursor.execute(query)
        await self.commit()
