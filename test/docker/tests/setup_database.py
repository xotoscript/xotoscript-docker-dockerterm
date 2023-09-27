import subprocess
import pytest

# define a pytest fixture to get the environment variables from the container
@pytest.fixture
def env_variables():
    return {
        "POSTGRES_VERSION": "12"  # update this with the correct version
    }

# test if mongodb is installed and available
def test_mongodb_installed():
    try:
        # check if mongodb is installed
        subprocess.check_output(["mongod", "--version"], stderr=subprocess.STDOUT, text=True)
    except subprocess.CalledProcessError as e:
        output = e.output.strip()
        pytest.fail(f"Error checking MongoDB installation: {output}")

# test if postgres is installed and available
def test_postgres_installed():
    try:
        # check if postgres is installed
        cmd_output = subprocess.check_output(["psql", "--version"], stderr=subprocess.STDOUT, text=True)
    except subprocess.CalledProcessError as e:
        output = e.output.strip()
        pytest.fail(f"Error checking Postgres installation: {output}")
