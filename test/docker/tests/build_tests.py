import os
import platform
import subprocess
import pytest

# env
HOME_PATH = os.environ['HOME']
ROOT = 'root'
USER_NAME = 'xotosphere'
USER_GROUP = 'dockerterm'
FONTS_PATH = '/usr/local/share/fonts'
OH_MY_ZSH_PATH = HOME_PATH + '/.oh-my-zsh'

# sample data from the .env file
env_data = {
    'NEOVIM_VERSION': '0.9.0',
    'YARN_VERSION': '1',
    'POSTGRES_VERSION': '12',
    'RUBBY_VERSION': '2.1.1',
    'NERDS_FONT_VERSION': '2.1.0',
    'FZF_VERSION': '0.21.1',
    'GITSTATUS_VERSION': '1.0.0',
}

# test if the package is installed and the version is correct
@pytest.mark.parametrize('package,expected_version', [
    ('nvim', env_data['NEOVIM_VERSION']),
    ('fzf', env_data['FZF_VERSION']),
])

# test if the package is installed and the version is correct
def test_nvm_version(host, package, expected_version):
    try:
        cmd = f'{package} --version' # source the environment in a subshell and run the --version command
        cmd_output = subprocess.run(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        if cmd_output.returncode == 0: # check if the command was successful and capture the output
            nvm_version = cmd_output.stdout.strip()  # remove leading/trailing spaces and newlines
            assert expected_version in nvm_version
        else:
            pytest.fail(f"error executing {cmd}. is installed?")
    except FileNotFoundError:
        pytest.fail("executable not found. is properly sourced?")

# test if maven is installed
def test_maven_installed():
    try:
        # run the 'mvn --version' command and capture the output
        cmd_output = subprocess.check_output(['mvn', '--version'], stderr=subprocess.STDOUT, text=True)
        # check if the output contains information about maven
        assert "Apache Maven" in cmd_output
    except subprocess.CalledProcessError:
        pytest.fail("Maven not installed")
