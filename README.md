# BruteForceDB

BruteForceDB is a simple Python application that attempts to connect to a MySQL database using a list of passwords, effectively functioning as a basic brute force password attack. This tool can be used for testing the strength of your database passwords or for educational purposes.

## Prerequisites

- Python 3 and above
- [Poetry](https://python-poetry.org/docs/)

## Setting Up

1. Clone this repository onto your local machine:

   ```sh
   git clone https://github.com/AiWaldoh/ccnb-brute
   ```

2. Navigate to the cloned repository:

   ```sh
   cd ccnb-brute
   ```

3. Install all python dependencies with Poetry:

   ```sh
   poetry install
   ```

4. Create a `.env` file in the root directory with the following variables:

   ```
   DB_HOST=your_database_host
   DB_USERNAME=your_database_username
   ```

5. Create a `password_list.txt` file in the root directory. This text file should contain a list of passwords, one password per line.

**Important:** Be sure to properly secure your .env and password_list.txt files to prevent leakage of sensitive data.

## Running the Tool

To start the brute force attack, simply run brute_forcer.py:

```sh
poetry run python3 brute_forcer.py
```

The script will attempt to connect to the database using each password in the list. The results of each attempt are printed to the console.

## Disclaimer

This tool is provided for educational purposes only. It is illegal to use this tool for unauthorized attempts to access any database systems. We are not responsible for any misuse or damage caused by this tool. Please use responsibly.
