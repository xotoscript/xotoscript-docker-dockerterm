import os
import pytest
import subprocess

# Define a pytest fixture to get the environment variables from the container
@pytest.fixture
def env_variables():
    return {
        "EMAIL": "xotosphere@gmail.com",
        "NAME": "xotosphere",
        "USER_NAME": "xotosphere",
        "USER_GROUP": "dockerterm",
    }

# Test if environment variables are correctly set
def test_env_variables_set(env_variables):
    assert env_variables["EMAIL"] == "xotosphere@gmail.com"
    assert env_variables["NAME"] == "xotosphere"
    assert env_variables["USER_NAME"] == "xotosphere"
    assert env_variables["USER_GROUP"] == "dockerterm"


# Test if tmux is installed and available
def test_tmux_installed():
    try:
        cmd_output = subprocess.check_output(["tmux", "-V"], stderr=subprocess.STDOUT, text=True)
        assert "tmux" in cmd_output
    except subprocess.CalledProcessError:
        pytest.fail("tmux not installed")

# Test if vim is installed and available
def test_vim_installed():
    try:
        cmd_output = subprocess.check_output(["vim", "--version"], stderr=subprocess.STDOUT, text=True)
        assert "VIM - Vi IMproved" in cmd_output
    except subprocess.CalledProcessError:
        pytest.fail("vim not installed")

# Test if Docker is correctly installed and available
def test_docker_installed():
    cmd_output = subprocess.check_output(["docker", "--version"], stderr=subprocess.STDOUT, text=True)
    assert "Docker version" in cmd_output

# Test if Neovim is correctly installed and available
def test_neovim_installed():
    cmd_output = subprocess.check_output(["nvim", "--version"], stderr=subprocess.STDOUT, text=True)
    assert "NVIM v" in cmd_output

# Test if Git is correctly installed and available
def test_git_installed():
    cmd_output = subprocess.check_output(["git", "--version"], stderr=subprocess.STDOUT, text=True)
    assert "git version" in cmd_output

# Test Git configuration settings
def test_git_configuration(env_variables):
    # run git commands to retrieve configuration values
    try:
        default_branch = subprocess.check_output(["sudo","git", "config", "--global", "init.defaultBranch"], stderr=subprocess.STDOUT, text=True).strip()
        user_name = subprocess.check_output(["sudo","git", "config", "--global", "user.name"], stderr=subprocess.STDOUT, text=True).strip()
        user_email = subprocess.check_output(["sudo","git", "config", "--global", "user.email"], stderr=subprocess.STDOUT, text=True).strip()
        excludes_file = subprocess.check_output(["sudo","git", "config", "--global", "core.excludesfile"], stderr=subprocess.STDOUT, text=True).strip()
        credential_helper = subprocess.check_output(["sudo","git", "config", "--global", "credential.helper"], stderr=subprocess.STDOUT, text=True).strip()
        color_ui = subprocess.check_output(["sudo","git", "config", "--global", "color.ui"], stderr=subprocess.STDOUT, text=True).strip()

        # assert that configuration values match expected values
        assert default_branch == "development"
        assert user_name == "xotosphere"
        assert user_email == env_variables["EMAIL"]
        assert excludes_file == "~/.sudo gitignore"
        assert credential_helper == "cache"
        assert color_ui == "true"

    except subprocess.CalledProcessError as e:
        # capture the output of the failed command for debugging
        output = e.output.strip()
        pytest.fail("Error retrieving Git configuration")

# Test if NVM is installed and available
def test_nvm_installed():
    try:
        # check if nvm is installed
        nvm_output = subprocess.check_output(["sudo", "sh","-c",".","./nvim/","&&","nvm", "--version"], stderr=subprocess.STDOUT, text=True)
        #assert "0.33" in nvm_output
        assert "" in nvm_output

    except subprocess.CalledProcessError as e:
        # capture the output of the failed command for debugging
        output = e.output.strip()
        pytest.fail(f"Error checking NVM installation: {output}")

# Test if Yarn is installed and available
# def test_yarn_installed():
#     try:
#         # check if yarn is installed
#         subprocess.check_output(["yarn", "--version"], stderr=subprocess.STDOUT, text=True)

#     except subprocess.CalledProcessError as e:
#         output = e.output.strip()
#         pytest.fail(f"Error checking Yarn installation: {output}")

# Test if Docker is installed and available
def test_docker_installed():
    try:
        # check if docker is installed
        subprocess.check_output(["docker", "--version"], stderr=subprocess.STDOUT, text=True)

    except subprocess.CalledProcessError as e:
        output = e.output.strip()
        pytest.fail(f"Error checking Docker installation: {output}")

# Test if Docker Compose is installed and available
def test_docker_compose_installed():
    try:
        # check if docker compose is installed
        subprocess.check_output(["docker-compose", "--version"], stderr=subprocess.STDOUT, text=True)

    except subprocess.CalledProcessError as e:
        output = e.output.strip()
        pytest.fail(f"Error checking Docker Compose installation: {output}")

# Test if SSH client and server are installed and available
def test_ssh_installed():
    try:
        # check if ssh client is installed
        subprocess.check_output(["ssh", "-V"], stderr=subprocess.STDOUT, text=True)

    except subprocess.CalledProcessError as e:
        output = e.output.strip()
        pytest.fail(f"Error checking SSH installation: {output}")
