"""
This module provides the DataConnector class for connecting to different types of databases.
"""

from typing import Optional
import aiosqlite
import aiomysql
from .manager.configManager import ConfigManager


class DataConnector:
    """
    The DataConnector class provides methods to connect to, disconnect from,
    and interact with different types of databases.
    """

    conn: Optional[object] = None

    @staticmethod
    async def connect(configPath: str) -> None:
        """
        Connect to the database using the configuration file path.

        Args:
            configPath (str): The path to the configuration file.
        """
        config = ConfigManager(configPath)
        db_type = config.get_database_type()

        if db_type == "sqlite":
            sqliteDataFile = config.get_sqlite_file_path()
            DataConnector.conn = await aiosqlite.connect(sqliteDataFile)
            print("Connected to SQLite database")
        elif db_type == "mysql":
            DataConnector.conn = await aiomysql.connect(
                host=config.get_mysql_host(),
                user=config.get_mysql_username(),
                password=config.get_mysql_password(),
                db=config.get_mysql_schema(),
            )
            print("Connected to MySQL database")
        else:
            print("Invalid database type")

    @staticmethod
    async def get_cursor() -> Optional[object]:
        """
        Get the database cursor.

        Returns:
            object: The database cursor.
        """
        return await DataConnector.conn.cursor()

    @staticmethod
    async def disconnect() -> None:
        """
        Disconnect from the database.
        """
        if DataConnector.conn:
            await DataConnector.conn.close()
