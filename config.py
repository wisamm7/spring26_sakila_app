# Configuration updated by Wisam Alam and Team Member
# Date: 25-06-2026
# Change: Resolved merge conflict by keeping sakila-db-server as MYSQL_HOST
# and adding both CONNECTION_TIMEOUT and HEALTH_CHECK_INTERVAL.

import os


class Config:
    """Base configuration class for the Sakila Flask application."""

    MYSQL_HOST = os.environ.get('MYSQL_HOST', 'sakila-db-server')
    MYSQL_USER = os.environ.get('MYSQL_USER', 'root')
    MYSQL_PASSWORD = os.environ.get('MYSQL_PASSWORD', 'admin')
    MYSQL_DB = os.environ.get('MYSQL_DB', 'sakila')

    CONNECTION_TIMEOUT = int(os.environ.get('CONNECTION_TIMEOUT', '30'))
    HEALTH_CHECK_INTERVAL = int(os.environ.get('HEALTH_CHECK_INTERVAL', '10'))

    SECRET_KEY = os.environ.get(
        'SECRET_KEY',
        'your-secret-key-here-change-this-in-production'
    )


MYSQL_HOST = Config.MYSQL_HOST
MYSQL_USER = Config.MYSQL_USER
MYSQL_PASSWORD = Config.MYSQL_PASSWORD
MYSQL_DB = Config.MYSQL_DB
CONNECTION_TIMEOUT = Config.CONNECTION_TIMEOUT
HEALTH_CHECK_INTERVAL = Config.HEALTH_CHECK_INTERVAL
SECRET_KEY = Config.SECRET_KEY
