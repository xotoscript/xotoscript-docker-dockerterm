import os
import platform
import subprocess
import pytest


# test if the package is installed and the version is correct
def test_java_version(host):
    expected_version = 'openjdk 11'
    cmd_output = subprocess.check_output(['java', '--version'], stderr=subprocess.STDOUT, text=True)
    java_version = cmd_output.splitlines()[0].strip()
    assert java_version.startswith(expected_version)

# Test if Go is correctly installed and available
def test_go_installed():
    try:
        cmd_output = subprocess.check_output(["go", "version"], stderr=subprocess.STDOUT, text=True)
        #assert "go1.16.7" in cmd_output
    except subprocess.CalledProcessError:
        pytest.fail("Go not installed")

# Test if Python is correctly installed and available
def test_python_installed():
    try:
        cmd_output = subprocess.check_output(["python3", "--version"], stderr=subprocess.STDOUT, text=True)
        assert "Python 3" in cmd_output
    except subprocess.CalledProcessError:
        pytest.fail("Python not installed")

# Test if Ruby is correctly installed and available
# def test_ruby_installed():
#     try:
#         #cmd_output = subprocess.check_output(["ruby", "--version"], stderr=subprocess.STDOUT, text=True)
#         cmd_output = subprocess.check_output(["rbenv", "version"], stderr=subprocess.STDOUT, text=True)
#         assert "system" in cmd_output
#     except subprocess.CalledProcessError:
#         pytest.fail("Ruby not installed")


# Test if Fira Code fonts have been successfully installed
def test_fira_code_fonts_installed():
    font_dir = "/usr/local/share/fonts"
    expected_fonts = [
        "Fura Code Light Nerd Font Complete.ttf",
        # Add more font filenames
    ]
    for font in expected_fonts:
        font_path = os.path.join(font_dir, font)
        assert os.path.exists(font_path)

# Test if exa has been successfully installed
def test_exa_installed():
    assert os.path.exists("/usr/local/bin/exa")

# Test if fzf has been successfully installed
def test_fzf_installed():
    assert os.path.exists("/usr/local/bin/fzf")

# Test if autojump has been successfully installed
def test_autojump_installed():
    assert os.path.exists("/usr/bin/autojump")
