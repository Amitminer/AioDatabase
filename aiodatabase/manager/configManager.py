import yaml
from typing import Optional


class ConfigManager:
    """A class to manage configuration settings loaded from a YAML file."""

    def __init__(self, file_path: str = "config.yml") -> None:
        """Initialize the ConfigManager with the path to the configuration file.

        Args:
            file_path (str, optional): The path to the YAML configuration file.
                Defaults to "config.yml".
        """
        self.config = self.load_config(file_path)

    def load_config(self, file_path: str) -> dict:
        """Load the YAML configuration file.

        Args:
            file_path (str): The path to the YAML configuration file.

        Returns:
            dict: The parsed configuration settings as a dictionary.
        """
        with open(file_path, "r") as file:
            return yaml.safe_load(file)

    def get_database_config(self) -> dict:
        """Get the database configuration settings.

        Returns:
            dict: The database configuration settings.
        """
        return self.config.get("database", {})

    def get_database_type(self) -> Optional[str]:
        """Get the type of database being used.

        Returns:
            str: The type of database ("sqlite" or "mysql").
        """
        return self.config["database"].get("type")

    def get_sqlite_file_path(self) -> Optional[str]:
        """Get the file path for SQLite database.

        Returns:
            str: The file path for the SQLite database.
        """
        return self.config["database"]["sqlite"].get("file")

    def get_mysql_host(self) -> Optional[str]:
        """Get the MySQL host address.

        Returns:
            str: The MySQL host address.
        """
        return self.config["database"]["mysql"].get("host")

    def get_mysql_username(self) -> Optional[str]:
        """Get the MySQL username.

        Returns:
            str: The MySQL username.
        """
        return self.config["database"]["mysql"].get("username")

    def get_mysql_password(self) -> Optional[str]:
        """Get the MySQL password.

        Returns:
            str: The MySQL password.
        """
        return self.config["database"]["mysql"].get("password")

    def get_mysql_schema(self) -> Optional[str]:
        """Get the MySQL schema name.

        Returns:
            str: The MySQL schema name.
        """
        return self.config["database"]["mysql"].get("schema")
